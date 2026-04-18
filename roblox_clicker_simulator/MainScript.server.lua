-- Main Server Script for Roblox Clicker Simulator
-- Handles game logic, data management, and pet spawning

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local RunService = game:GetService("RunService")
local DataStoreService = game:GetService("DataStoreService")

-- Create RemoteEvents for client-server communication
local remoteEvents = Instance.new("Folder")
remoteEvents.Name = "RemoteEvents"
remoteEvents.Parent = ReplicatedStorage

local clickEvent = Instance.new("RemoteEvent")
clickEvent.Name = "ClickEvent"
clickEvent.Parent = remoteEvents

local upgradeEvent = Instance.new("RemoteEvent")
upgradeEvent.Name = "UpgradeEvent"
upgradeEvent.Parent = remoteEvents

local petSpawnEvent = Instance.new("RemoteEvent")
petSpawnEvent.Name = "PetSpawnEvent"
petSpawnEvent.Parent = remoteEvents

-- DataStore for saving player data
local playerDataStore = DataStoreService:GetDataStore("PlayerData")

-- Game configuration
local GAME_CONFIG = {
    BASE_CLICK_POWER = 1,
    CLICK_POWER_MULTIPLIER = 1.5,
    BASE_PET_COST = 100,
    PET_COST_MULTIPLIER = 1.8,
    PET_AUTO_CLICK_INTERVAL = 1, -- seconds
    PET_AUTO_CLICK_POWER = 0.1
}

-- Pet types and their properties
local PET_TYPES = {
    {
        Name = "Basic Cat",
        Cost = 100,
        AutoClickPower = 0.1,
        Model = "rbxassetid://1234567890" -- Replace with actual pet model ID
    },
    {
        Name = "Golden Dog",
        Cost = 500,
        AutoClickPower = 0.5,
        Model = "rbxassetid://1234567891"
    },
    {
        Name = "Dragon",
        Cost = 2500,
        AutoClickPower = 2.5,
        Model = "rbxassetid://1234567892"
    },
    {
        Name = "Phoenix",
        Cost = 10000,
        AutoClickPower = 10,
        Model = "rbxassetid://1234567893"
    }
}

-- Player data structure
local function createDefaultPlayerData()
    return {
        coins = 0,
        clickPower = GAME_CONFIG.BASE_CLICK_POWER,
        totalClicks = 0,
        pets = {},
        upgrades = {
            clickPowerLevel = 1,
            petEfficiencyLevel = 1
        }
    }
end

-- Store player data in memory
local playerData = {}

-- Data management functions
local function savePlayerData(player)
    local success, errorMessage = pcall(function()
        playerDataStore:SetAsync(player.UserId, playerData[player.UserId])
    end)
    
    if not success then
        warn("Failed to save data for " .. player.Name .. ": " .. errorMessage)
    end
end

local function loadPlayerData(player)
    local success, data = pcall(function()
        return playerDataStore:GetAsync(player.UserId)
    end)
    
    if success and data then
        playerData[player.UserId] = data
    else
        playerData[player.UserId] = createDefaultPlayerData()
    end
    
    return playerData[player.UserId]
end

-- Game logic functions
local function calculateClickPower(player)
    local data = playerData[player.UserId]
    local basePower = GAME_CONFIG.BASE_CLICK_POWER
    local upgradeMultiplier = math.pow(GAME_CONFIG.CLICK_POWER_MULTIPLIER, data.upgrades.clickPowerLevel - 1)
    
    return basePower * upgradeMultiplier
end

local function calculatePetCost(petType, petCount)
    return math.floor(PET_TYPES[petType].Cost * math.pow(GAME_CONFIG.PET_COST_MULTIPLIER, petCount))
end

local function handleClick(player)
    local data = playerData[player.UserId]
    local clickPower = calculateClickPower(player)
    
    data.coins = data.coins + clickPower
    data.totalClicks = data.totalClicks + 1
    
    -- Update click power in case of upgrades
    data.clickPower = clickPower
    
    return data.coins, data.clickPower
end

local function handleUpgrade(player, upgradeType)
    local data = playerData[player.UserId]
    local cost = 0
    
    if upgradeType == "clickPower" then
        cost = math.floor(100 * math.pow(2, data.upgrades.clickPowerLevel - 1))
        if data.coins >= cost then
            data.coins = data.coins - cost
            data.upgrades.clickPowerLevel = data.upgrades.clickPowerLevel + 1
            data.clickPower = calculateClickPower(player)
            return true, data.coins, data.clickPower
        end
    elseif upgradeType == "petEfficiency" then
        cost = math.floor(500 * math.pow(2, data.upgrades.petEfficiencyLevel - 1))
        if data.coins >= cost then
            data.coins = data.coins - cost
            data.upgrades.petEfficiencyLevel = data.upgrades.petEfficiencyLevel + 1
            return true, data.coins, data.upgrades.petEfficiencyLevel
        end
    end
    
    return false, data.coins, 0
end

local function handlePetPurchase(player, petType)
    local data = playerData[player.UserId]
    local petCount = data.pets[petType] or 0
    local cost = calculatePetCost(petType, petCount)
    
    if data.coins >= cost then
        data.coins = data.coins - cost
        data.pets[petType] = petCount + 1
        return true, data.coins, data.pets[petType]
    end
    
    return false, data.coins, petCount
end

-- Pet auto-clicking system
local function startPetAutoClick(player)
    local data = playerData[player.UserId]
    
    spawn(function()
        while player.Parent and playerData[player.UserId] do
            wait(GAME_CONFIG.PET_AUTO_CLICK_INTERVAL)
            
            local totalAutoClickPower = 0
            for petType, count in pairs(data.pets) do
                if count > 0 then
                    local petData = PET_TYPES[petType]
                    local efficiencyMultiplier = math.pow(1.2, data.upgrades.petEfficiencyLevel - 1)
                    totalAutoClickPower = totalAutoClickPower + (petData.AutoClickPower * count * efficiencyMultiplier)
                end
            end
            
            if totalAutoClickPower > 0 then
                data.coins = data.coins + totalAutoClickPower
            end
        end
    end)
end

-- RemoteEvent handlers
clickEvent.OnServerEvent:Connect(function(player)
    local coins, clickPower = handleClick(player)
    
    -- Send updated data back to client
    local updateEvent = Instance.new("RemoteEvent")
    updateEvent.Name = "UpdateData"
    updateEvent.Parent = ReplicatedStorage.RemoteEvents
    updateEvent:FireClient(player, {
        coins = coins,
        clickPower = clickPower,
        totalClicks = playerData[player.UserId].totalClicks
    })
end)

upgradeEvent.OnServerEvent:Connect(function(player, upgradeType)
    local success, coins, value = handleUpgrade(player, upgradeType)
    
    local responseEvent = Instance.new("RemoteEvent")
    responseEvent.Name = "UpgradeResponse"
    responseEvent.Parent = ReplicatedStorage.RemoteEvents
    responseEvent:FireClient(player, {
        success = success,
        coins = coins,
        upgradeType = upgradeType,
        value = value
    })
end)

petSpawnEvent.OnServerEvent:Connect(function(player, petType)
    local success, coins, petCount = handlePetPurchase(player, petType)
    
    local responseEvent = Instance.new("RemoteEvent")
    responseEvent.Name = "PetResponse"
    responseEvent.Parent = ReplicatedStorage.RemoteEvents
    responseEvent:FireClient(player, {
        success = success,
        coins = coins,
        petType = petType,
        petCount = petCount
    })
end)

-- Player connection handling
Players.PlayerAdded:Connect(function(player)
    -- Load player data
    loadPlayerData(player)
    
    -- Start pet auto-clicking
    startPetAutoClick(player)
    
    -- Send initial data to client
    wait(1) -- Wait for client to load
    local initEvent = Instance.new("RemoteEvent")
    initEvent.Name = "InitializeData"
    initEvent.Parent = ReplicatedStorage.RemoteEvents
    initEvent:FireClient(player, {
        coins = playerData[player.UserId].coins,
        clickPower = playerData[player.UserId].clickPower,
        totalClicks = playerData[player.UserId].totalClicks,
        pets = playerData[player.UserId].pets,
        upgrades = playerData[player.UserId].upgrades,
        petTypes = PET_TYPES
    })
end)

Players.PlayerRemoving:Connect(function(player)
    -- Save player data when they leave
    savePlayerData(player)
    playerData[player.UserId] = nil
end)

-- Auto-save data every 30 seconds
spawn(function()
    while true do
        wait(30)
        for _, player in pairs(Players:GetPlayers()) do
            savePlayerData(player)
        end
    end
end)

print("Clicker Simulator Server Script loaded successfully!")
