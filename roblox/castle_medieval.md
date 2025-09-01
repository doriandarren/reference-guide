# Catillo medieval


```sh 


-- === Medieval Wall Builder (Edit Mode via Command Bar) ===
local cfg = {
    name         = "Fortaleza01",
    center       = Vector3.new(0, 0, 0),
    width        = 60,     -- igual que antes
    depth        = 40,     -- igual que antes
    wallHeight   = 12,
    wallThick    = 2,
    material     = Enum.Material.Slate,
    color        = Color3.fromRGB(145, 145, 145),

    battlement = {         -- merlones / almenas
        merlonWidth  = 2.5,
        merlonHeight = 1.5,
        merlonDepth  = 1.25,
        gap          = 1.25
    },

    towers = {
        shape   = "square", -- "square" | "cylinder"
        size    = 8,        -- ancho (o diámetro si cylinder)
        height  = 16,       -- más altas que el muro
        rim     = 0.75      -- pequeño vuelo de las almenas hacia afuera
    },

    gate = {
        enabled        = true,
        side           = "Front",   -- "Front" | "Back" | "Left" | "Right"
        width          = 10,
        height         = 9,
        offset         = 0,         -- desplazamiento de la puerta
        gatehouseDepth = 5,         -- casamata saliente
        portcullis     = true,      -- reja
        bars           = 9          -- nº barras verticales
    }
}

-- ========== Utils ==========
local function makePart(size, cframe, parent, color, material)
    local p = Instance.new("Part")
    p.Size = size
    p.CFrame = cframe
    p.Anchored = true
    p.CanCollide = true
    p.TopSurface = Enum.SurfaceType.Smooth
    p.BottomSurface = Enum.SurfaceType.Smooth
    p.Material = material
    p.Color = color
    p.Parent = parent
    return p
end

local function makeWall(model, length, height, thick, centerPos, yaw, color, material)
    local size = Vector3.new(length, height, thick)
    local cf = CFrame.new(centerPos) * CFrame.Angles(0, yaw or 0, 0)
    local part = makePart(size, cf, model, color, material)
    return part
end

-- Almenas sobre un tramo de muro
local function addBattlements(sideName, alongX, wallPart, battlement, color, material)
    local size = wallPart.Size
    local cf   = wallPart.CFrame
    local L    = (alongX and size.X) or size.Z
    local topY = size.Y/2 + battlement.merlonHeight/2

    -- Offset local hacia el exterior (borde del muro)
    local outX, outZ = 0, 0
    if alongX then
        if sideName == "Front" then
            outZ =  size.Z/2 - battlement.merlonDepth/2
        else -- Back
            outZ = -size.Z/2 + battlement.merlonDepth/2
        end
    else
        if sideName == "Right" then
            outX =  size.X/2 - battlement.merlonDepth/2
        else -- Left
            outX = -size.X/2 + battlement.merlonDepth/2
        end
    end

    local step = battlement.merlonWidth + battlement.gap
    local start = -L/2 + battlement.merlonWidth/2
    while start <= L/2 - battlement.merlonWidth/2 + 0.001 do
        local localPos
        if alongX then
            localPos = Vector3.new(start, topY, outZ)
        else
            localPos = Vector3.new(outX, topY, start)
        end
        local worldCF = cf * CFrame.new(localPos)
        makePart(
            Vector3.new(
                (alongX and battlement.merlonWidth) or battlement.merlonDepth,
                battlement.merlonHeight,
                (alongX and battlement.merlonDepth) or battlement.merlonWidth
            ),
            worldCF,
            wallPart.Parent,
            color, material
        )
        start = start + step
    end
end

-- ========== Construcción principal ==========
local function buildFort(c)
    local model = Instance.new("Model")
    model.Name = c.name
    model.Parent = workspace

    local halfW, halfD = c.width/2, c.depth/2
    local yMid = c.center.Y + c.wallHeight/2

    local sides = {
        Front = {center = Vector3.new(c.center.X, yMid, c.center.Z + halfD), yaw = 0,            alongX = true,  length = c.width},
        Back  = {center = Vector3.new(c.center.X, yMid, c.center.Z - halfD), yaw = 0,            alongX = true,  length = c.width},
        Right = {center = Vector3.new(c.center.X + halfW, yMid, c.center.Z), yaw = math.rad(90), alongX = false, length = c.depth},
        Left  = {center = Vector3.new(c.center.X - halfW, yMid, c.center.Z), yaw = math.rad(90), alongX = false, length = c.depth},
    }

    local createdWalls = {}

    local function buildSide(name)
        local s = sides[name]
        local hasGate = c.gate.enabled and (c.gate.side == name)
        if not hasGate then
            local part = makeWall(model, s.length, c.wallHeight, c.wallThick, s.center, s.yaw, c.color, c.material)
            table.insert(createdWalls, {part = part, name = name, alongX = s.alongX})
            return
        end

        -- División para puerta
        local L = s.length
        local dw = math.clamp(c.gate.width, 1, L - 2)
        local dh = math.clamp(c.gate.height, 1, c.wallHeight - 1)
        local off = c.gate.offset

        local leftLen  = math.max(0, (L/2) + off - (dw/2))
        local rightLen = math.max(0, (L/2) - off - (dw/2))
        local lintelH  = math.max(0, c.wallHeight - dh)

        local function alongDelta(delta)
            if s.alongX then
                return Vector3.new(delta, 0, 0)
            else
                return Vector3.new(0, 0, delta)
            end
        end

        if leftLen > 0 then
            local pos = s.center - alongDelta((L/2) - (leftLen/2))
            local part = makeWall(model, leftLen, c.wallHeight, c.wallThick, pos, s.yaw, c.color, c.material)
            table.insert(createdWalls, {part = part, name = name, alongX = s.alongX})
        end
        if rightLen > 0 then
            local pos = s.center + alongDelta((L/2) - (rightLen/2))
            local part = makeWall(model, rightLen, c.wallHeight, c.wallThick, pos, s.yaw, c.color, c.material)
            table.insert(createdWalls, {part = part, name = name, alongX = s.alongX})
        end
        if lintelH > 0 then
            -- Tramo superior sobre la puerta
            local posTop = Vector3.new(s.center.X, c.center.Y + dh + (lintelH/2), s.center.Z)
            local part = makeWall(model, dw, lintelH, c.wallThick, posTop, s.yaw, c.color, c.material)
            table.insert(createdWalls, {part = part, name = name, alongX = s.alongX})
        end

        -- Gatehouse (casamata) saliente
        local ghDepth = c.gate.gatehouseDepth
        if ghDepth and ghDepth > 0 then
            local forward
            if name == "Front" then forward = Vector3.new(0, 0, 1)
            elseif name == "Back" then forward = Vector3.new(0, 0, -1)
            elseif name == "Right" then forward = Vector3.new(1, 0, 0)
            else forward = Vector3.new(-1, 0, 0) end

            local ghCenter = s.center + forward * (c.wallThick/2 + ghDepth/2)
            local gh = makePart(
                Vector3.new(dw + 4, c.wallHeight + 2, ghDepth),
                CFrame.new(ghCenter) * CFrame.Angles(0, s.yaw, 0),
                model, c.color, c.material
            )
            -- Almenas en la cara frontal del gatehouse
            addBattlements(name, s.alongX, gh, c.battlement, c.color, c.material)
        end

        -- Portcullis (reja)
        if c.gate.portcullis then
            local bars = math.max(3, c.gate.bars or 7)
            local step = dw / bars
            for i = 0, bars do
                local localPos
                if s.alongX then
                    localPos = Vector3.new(-dw/2 + i*step, dh/2, 0) -- en el plano del muro
                else
                    localPos = Vector3.new(0, dh/2, -dw/2 + i*step)
                end
                local barCF = (CFrame.new(s.center) * CFrame.Angles(0, s.yaw, 0)) * CFrame.new(localPos)
                makePart(
                    Vector3.new(0.25, dh, 0.25),
                    barCF,
                    model,
                    Color3.fromRGB(90,90,90),
                    Enum.Material.Metal
                )
            end
        end
    end

    buildSide("Front"); buildSide("Back"); buildSide("Left"); buildSide("Right")

    -- Almenas en todos los tramos de muro
    for _, w in ipairs(createdWalls) do
        addBattlements(w.name, w.alongX, w.part, c.battlement, c.color, c.material)
    end

    -- Torres en las 4 esquinas
    local function placeTower(xSign, zSign)
        local cx = c.center.X + xSign * halfW
        local cz = c.center.Z + zSign * halfD
        local ch = c.center.Y + c.towers.height/2

        local size = c.towers.size
        local tower
        if c.towers.shape == "cylinder" then
            tower = Instance.new("Part")
            tower.Shape = Enum.PartType.Cylinder
            tower.Size = Vector3.new(size, c.towers.height, size) -- por defecto el eje mayor es X; rotamos para que quede vertical
            tower.CFrame = CFrame.new(Vector3.new(cx, ch, cz)) * CFrame.Angles(0, 0, math.rad(90))
            tower.Anchored = true; tower.Material = c.material; tower.Color = c.color
            tower.TopSurface = Enum.SurfaceType.Smooth; tower.BottomSurface = Enum.SurfaceType.Smooth
            tower.Parent = model
        else
            tower = makePart(Vector3.new(size, c.towers.height, size), CFrame.new(cx, ch, cz), model, c.color, c.material)
        end

        -- Almenas alrededor del borde superior de la torre (cuatro lados simples)
        local topY = c.towers.height/2 + c.battlement.merlonHeight/2
        local mW, mH, mD, rim = c.battlement.merlonWidth, c.battlement.merlonHeight, c.battlement.merlonDepth, c.towers.rim
        local function edgeRow(alongX, length, localOffsetX, localOffsetZ)
            local step = mW + c.battlement.gap
            local start = -length/2 + mW/2
            while start <= length/2 - mW/2 + 0.001 do
                local localPos
                if alongX then
                    localPos = Vector3.new(start + localOffsetX, topY, localOffsetZ)
                else
                    localPos = Vector3.new(localOffsetX, topY, start + localOffsetZ)
                end
                local worldCF = tower.CFrame * CFrame.new(localPos)
                makePart(
                    Vector3.new((alongX and mW) or mD, mH, (alongX and mD) or mW),
                    worldCF,
                    model, c.color, c.material
                )
                start = start + step
            end
        end

        local L = size + 2*rim
        -- Frente y atrás (a lo largo de X)
        edgeRow(true,  L, 0,  size/2 + rim - mD/2)
        edgeRow(true,  L, 0, -size/2 - rim + mD/2)
        -- Derecha e izquierda (a lo largo de Z)
        edgeRow(false, L,  size/2 + rim - mD/2, 0)
        edgeRow(false, L, -size/2 - rim + mD/2, 0)
    end

    placeTower( 1,  1) -- Front-Right
    placeTower(-1,  1) -- Front-Left
    placeTower( 1, -1) -- Back-Right
    placeTower(-1, -1) -- Back-Left

    return model
end

buildFort(cfg)




```