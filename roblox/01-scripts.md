
01 Estrucura y carpetas

```sh

-- 🚀 Script para crear la estructura base del proyecto medieval
-- Ejecuta esto una sola vez (puedes borrarlo después de que cree las carpetas).

local function ensureFolder(parent, name)
	local f = parent:FindFirstChild(name)
	if not f then
		f = Instance.new("Folder")
		f.Name = name
		f.Parent = parent
	end
	return f
end

-- ServerStorage > VillageKit
local ServerStorage = game:GetService("ServerStorage")
local villageKit = ensureFolder(ServerStorage, "VillageKit")

-- Prefabs esperados (puedes crear modelos y meterlos aquí después)
local prefabs = { "House_A", "House_B", "Tower", "Market_Stall", "Barrel", "Crate", "Rock_A", "Rock_B", "LampPost", "Bush" }
for _, name in ipairs(prefabs) do
	ensureFolder(villageKit, name) -- de momento crea carpetas vacías, luego puedes reemplazar por Models reales
end

-- ReplicatedStorage > Waypoints
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local waypoints = ensureFolder(ReplicatedStorage, "Waypoints")

-- Crear algunos puntos de ejemplo
for i = 1, 3 do
	if not waypoints:FindFirstChild("P"..i) then
		local p = Instance.new("Part")
		p.Name = "P"..i
		p.Size = Vector3.new(1,1,1)
		p.Anchored = true
		p.Transparency = 0.5
		p.Color = Color3.fromRGB(255, 200, 0)
		p.Parent = waypoints
	end
end

-- Workspace > Village (contenedor para el pueblo generado)
local workspaceVillage = ensureFolder(workspace, "Village")

-- ServerScriptService > scripts base
local ServerScriptService = game:GetService("ServerScriptService")
local scriptsNeeded = { "GenerateVillage", "ScatterProps", "PathBuilder" }
for _, sName in ipairs(scriptsNeeded) do
	if not ServerScriptService:FindFirstChild(sName) then
		local s = Instance.new("Script")
		s.Name = sName
		s.Source = "-- TODO: añade aquí el código de "..sName
		s.Parent = ServerScriptService
	end
end

print("✅ Estructura base creada. Ahora puedes meter tus modelos en ServerStorage/VillageKit")



```





2) Ajustes de iluminación (look cálido de tarde)

```sh 

En Lighting:

ClockTime = 15

Brightness = 2

EnvironmentDiffuseScale = 0.6

EnvironmentSpecularScale = 0.5

Inserta Atmosphere: Density=0.35, Haze=1.0, Color=(255,245,230)

ColorCorrectionEffect: TintColor=(255,240,220), Saturation=-0.05, Contrast=0.08

BloomEffect: Intensity=0.3, Size=24

SunRaysEffect: Intensity=0.15, Spread=0.8

En Workspace:

StreamingEnabled = true (mejor rendimiento)

ModelStreamingMode = Atomic

````




3) en el Command Bar

```sh

-- ✅ COMMAND BAR V3 — Repara prefabs (Folder→Model) y genera el pueblo en EDITOR

local RunService = game:GetService("RunService")
if RunService:IsRunning() then
	warn("Detén el juego (Stop). Este script es para EDIT (no Play).")
	return
end

-- ---------- utilidades ----------
local function ensureFolder(parent, name)
	local f = parent:FindFirstChild(name)
	if not f then f = Instance.new("Folder"); f.Name = name; f.Parent = parent end
	return f
end

local function anchorAll(model)
	for _,d in ipairs(model:GetDescendants()) do
		if d:IsA("BasePart") then
			d.Anchored = true
			d.TopSurface = Enum.SurfaceType.Smooth
			d.BottomSurface = Enum.SurfaceType.Smooth
		end
	end
end

-- ---------- factories: crea MODELS si faltan ----------
local function prefab_House_A()
	local m = Instance.new("Model"); m.Name = "House_A"
	local walls = Instance.new("Part"); walls.Name="Walls"; walls.Size=Vector3.new(12,8,10)
	walls.Color=Color3.fromRGB(235,230,220); walls.Material=Enum.Material.SmoothPlastic; walls.Parent=m; walls.Anchored=true
	local roofL = Instance.new("WedgePart"); roofL.Size=Vector3.new(12,3,10); roofL.Color=Color3.fromRGB(180,80,50); roofL.Parent=m
	roofL.CFrame = walls.CFrame * CFrame.new(0, (8/2)+(3/2), 0) * CFrame.Angles(0,0,math.rad(180))
	local roofR = Instance.new("WedgePart"); roofR.Size=Vector3.new(12,3,10); roofR.Color=Color3.fromRGB(180,80,50); roofR.Parent=m
	roofR.CFrame = walls.CFrame * CFrame.new(0, (8/2)+(3/2), 0)
	m.PrimaryPart = walls; anchorAll(m); return m
end

local function prefab_House_B()
	local m = Instance.new("Model"); m.Name = "House_B"
	local walls = Instance.new("Part"); walls.Name="Walls"; walls.Size=Vector3.new(10,7,10)
	walls.Color=Color3.fromRGB(235,230,220); walls.Material=Enum.Material.SmoothPlastic; walls.Parent=m; walls.Anchored=true
	local roof = Instance.new("Part"); roof.Name="Roof"; roof.Size=Vector3.new(11,1,11)
	roof.Color=Color3.fromRGB(150,140,130); roof.Material=Enum.Material.Slate; roof.Parent=m
	roof.CFrame = walls.CFrame * CFrame.new(0, (7/2)+0.5, 0)
	m.PrimaryPart = walls; anchorAll(m); return m
end

local function prefab_Tower()
	local m = Instance.new("Model"); m.Name = "Tower"
	local body = Instance.new("Part"); body.Name="Body"; body.Size=Vector3.new(10,24,10)
	body.Color=Color3.fromRGB(150,140,130); body.Material=Enum.Material.Slate; body.Parent=m; body.Anchored=true
	local top = Instance.new("Part"); top.Shape=Enum.PartType.Cylinder; top.Size=Vector3.new(10,2,10)
	top.Color=Color3.fromRGB(130,120,110); top.Material=Enum.Material.Slate; top.Parent=m; top.Anchored=true
	top.CFrame = body.CFrame * CFrame.new(0, (24/2)+1, 0) * CFrame.Angles(0,0,math.rad(90))
	m.PrimaryPart = body; anchorAll(m); return m
end

local function prefab_Market_Stall()
	local m = Instance.new("Model"); m.Name = "Market_Stall"
	local tableP = Instance.new("Part"); tableP.Name="Table"; tableP.Size=Vector3.new(6,1,3)
	tableP.Color=Color3.fromRGB(138,90,54); tableP.Material=Enum.Material.Wood; tableP.Parent=m; tableP.Anchored=true
	local canopy = Instance.new("Part"); canopy.Name="Canopy"; canopy.Size=Vector3.new(6,0.5,3)
	canopy.Color=Color3.fromRGB(200,190,170); canopy.Material=Enum.Material.SmoothPlastic; canopy.Parent=m; canopy.Anchored=true
	canopy.CFrame = tableP.CFrame * CFrame.new(0, 3, 0)
	m.PrimaryPart = tableP; anchorAll(m); return m
end

local function prefab_Rock_A()
	local m = Instance.new("Model"); m.Name = "Rock_A"
	local p = Instance.new("Part"); p.Size=Vector3.new(3,2,3); p.Material=Enum.Material.Slate; p.Color=Color3.fromRGB(120,110,100); p.Parent=m; p.Anchored=true
	m.PrimaryPart = p; anchorAll(m); return m
end

local function prefab_Rock_B()
	local m = Instance.new("Model"); m.Name = "Rock_B"
	local p = Instance.new("Part"); p.Size=Vector3.new(2,1.5,2); p.Material=Enum.Material.Slate; p.Color=Color3.fromRGB(110,100,90); p.Parent=m; p.Anchored=true
	m.PrimaryPart = p; anchorAll(m); return m
end

local function prefab_Barrel()
	local m = Instance.new("Model"); m.Name = "Barrel"
	local p = Instance.new("Part"); p.Shape=Enum.PartType.Cylinder; p.Size=Vector3.new(2,3,2)
	p.Material=Enum.Material.Wood; p.Color=Color3.fromRGB(138,90,54); p.Parent=m; p.Anchored=true
	p.CFrame = p.CFrame * CFrame.Angles(0,0,math.rad(90))
	m.PrimaryPart = p; anchorAll(m); return m
end

local function prefab_Crate()
	local m = Instance.new("Model"); m.Name = "Crate"
	local p = Instance.new("Part"); p.Size=Vector3.new(2.5,2.5,2.5); p.Material=Enum.Material.Wood; p.Color=Color3.fromRGB(120,80,40); p.Parent=m; p.Anchored=true
	m.PrimaryPart = p; anchorAll(m); return m
end

local function prefab_LampPost()
	local m = Instance.new("Model"); m.Name = "LampPost"
	local pole = Instance.new("Part"); pole.Size=Vector3.new(0.3,6,0.3); pole.Material=Enum.Material.Metal; pole.Color=Color3.fromRGB(50,50,50); pole.Parent=m; pole.Anchored=true
	local head = Instance.new("Part"); head.Size=Vector3.new(0.8,0.8,0.8); head.Material=Enum.Material.Neon; head.Color=Color3.fromRGB(255,230,180); head.Parent=m; head.Anchored=true
	head.CFrame = pole.CFrame * CFrame.new(0, (6/2)+0.6, 0)
	m.PrimaryPart = pole; anchorAll(m); return m
end

local function prefab_Bush()
	local m = Instance.new("Model"); m.Name = "Bush"
	local p = Instance.new("Part"); p.Shape=Enum.PartType.Ball; p.Size=Vector3.new(2.5,2.5,2.5); p.Material=Enum.Material.Grass; p.Color=Color3.fromRGB(70,120,70); p.Parent=m; p.Anchored=true
	m.PrimaryPart = p; anchorAll(m); return m
end

local factories = {
	House_A = prefab_House_A,
	House_B = prefab_House_B,
	Tower = prefab_Tower,
	Market_Stall = prefab_Market_Stall,
	Rock_A = prefab_Rock_A,
	Rock_B = prefab_Rock_B,
	Barrel = prefab_Barrel,
	Crate = prefab_Crate,
	LampPost = prefab_LampPost,
	Bush = prefab_Bush,
}

-- ---------- normalizar prefabs: Folder -> Model ----------
local ServerStorage = game:GetService("ServerStorage")
local kit = ensureFolder(ServerStorage, "VillageKit")

local function getPrefabModel(name)
	local node = kit:FindFirstChild(name)
	if not node then
		-- no existe: creamos Model
		local mdl = factories[name] and factories[name]() or nil
		if mdl then mdl.Parent = kit; print("→ Prefab creado:", name); return mdl end
		warn("No hay factory para "..name); return nil
	end
	if node:IsA("Model") then return node end
	if node:IsA("Folder") then
		-- caso común: carpeta vacía creada antes; la reemplazamos por un Model
		local childModel = node:FindFirstChildWhichIsA("Model")
		if childModel then
			return childModel
		else
			local mdl = factories[name] and factories[name]() or nil
			if mdl then
				mdl.Parent = kit
				node:Destroy()
				print("↺ Reemplazado Folder por Model:", name)
				return mdl
			else
				warn("La Folder '"..name.."' no contiene Model y no hay factory.")
				return nil
			end
		end
	end
	-- si es otra cosa (Part/MeshPart, etc.), lo envolvemos en un Model
	if node:IsA("BasePart") then
		local mdl = Instance.new("Model"); mdl.Name = name; mdl.Parent = kit
		node.Parent = mdl
		mdl.PrimaryPart = node
		anchorAll(mdl)
		print("↺ Envolví '"..name.."' (Part) dentro de un Model")
		return mdl
	end
	warn("Prefab '"..name.."' no es Model/Folder/Part (tipo="..node.ClassName..")")
	return nil
end

-- Prepara todos los prefabs necesarios
for name,_ in pairs(factories) do
	getPrefabModel(name)
end

-- ---------- carpeta de trabajo ----------
local Village = ensureFolder(workspace, "Village")
for _,child in ipairs(Village:GetChildren()) do child:Destroy() end

-- ---------- colocar instancias ----------
local function place(name, cf)
	local src = getPrefabModel(name)
	if not src then warn("No se pudo obtener prefab: "..name); return end
	local m = src:Clone()
	m:PivotTo(cf)
	m.Parent = Village
	anchorAll(m)
	return m
end

-- ---------- layout ----------
local CENTER = Vector3.new(0, 5, 0) -- ajusta Y a tu terreno
local HOUSE_RADIUS = 70
local NUM_HOUSES = 8

-- Torre
place("Tower", CFrame.new(CENTER + Vector3.new(0, 12, -110)) * CFrame.Angles(0, math.rad(15), 0))

-- Mercado
place("Market_Stall", CFrame.new(CENTER + Vector3.new(0,0,6)))
place("Market_Stall", CFrame.new(CENTER + Vector3.new(6,0,-6)) * CFrame.Angles(0, math.rad(40), 0))
place("Market_Stall", CFrame.new(CENTER + Vector3.new(-6,0,-4)) * CFrame.Angles(0, math.rad(-25), 0))

-- Anillo de casas
for i=1, NUM_HOUSES do
	local angle = (i/NUM_HOUSES) * math.pi*2
	local pos = CENTER + Vector3.new(math.cos(angle)*HOUSE_RADIUS, 0, math.sin(angle)*HOUSE_RADIUS)
	local rot = CFrame.Angles(0, angle + math.pi, 0)
	local houseName = (i % 2 == 0) and "House_A" or "House_B"
	place(houseName, CFrame.new(pos) * rot)
end

print("✅ Pueblo creado en Workspace/Village (prefabs normalizados). ¡Ya puedes mover/rotar todo!")


```