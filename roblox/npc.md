# 

Crear una carpeta: Workspace/Waypoints

En el Command Bar:
```sh


local npc = workspace:FindFirstChild("NPC_Noob") or error("Renombra tu modelo a NPC_Noob o cambia el nombre aquí")
local root = npc:WaitForChild("HumanoidRootPart")

local folder = workspace:FindFirstChild("Waypoints") or Instance.new("Folder", workspace)
folder.Name = "Waypoints"

local function mk(name, pos)
    local p = Instance.new("Part")
    p.Name = name
    p.Size = Vector3.new(1,1,1)
    p.Anchored = true
    p.CanCollide = false
    p.Transparency = 1
    p.CFrame = CFrame.new(pos)
    p.Parent = folder
end

local r = 30
mk("P1", root.Position + Vector3.new( r, 0,  0))
mk("P2", root.Position + Vector3.new( 0, 0,  r))
mk("P3", root.Position + Vector3.new(-r, 0,  0))
mk("P4", root.Position + Vector3.new( 0, 0, -r))


```