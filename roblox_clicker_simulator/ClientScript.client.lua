-- Client Script for Roblox Clicker Simulator
-- Handles UI, user input, and client-side game logic

local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local UserInputService = game:GetService("UserInputService")
local TweenService = game:GetService("TweenService")
local SoundService = game:GetService("SoundService")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

-- Wait for RemoteEvents to be created
local remoteEvents = ReplicatedStorage:WaitForChild("RemoteEvents")
local clickEvent = remoteEvents:WaitForChild("ClickEvent")
local upgradeEvent = remoteEvents:WaitForChild("UpgradeEvent")
local petSpawnEvent = remoteEvents:WaitForChild("PetSpawnEvent")

-- Game data
local gameData = {
    coins = 0,
    clickPower = 1,
    totalClicks = 0,
    pets = {},
    upgrades = {},
    petTypes = {}
}

-- UI Creation
local function createMainGUI()
    local screenGui = Instance.new("ScreenGui")
    screenGui.Name = "ClickerSimulatorGUI"
    screenGui.Parent = playerGui
    
    -- Main frame
    local mainFrame = Instance.new("Frame")
    mainFrame.Name = "MainFrame"
    mainFrame.Size = UDim2.new(1, 0, 1, 0)
    mainFrame.Position = UDim2.new(0, 0, 0, 0)
    mainFrame.BackgroundColor3 = Color3.fromRGB(30, 30, 30)
    mainFrame.BorderSizePixel = 0
    mainFrame.Parent = screenGui
    
    -- Top bar with coins and click power
    local topBar = Instance.new("Frame")
    topBar.Name = "TopBar"
    topBar.Size = UDim2.new(1, 0, 0.1, 0)
    topBar.Position = UDim2.new(0, 0, 0, 0)
    topBar.BackgroundColor3 = Color3.fromRGB(50, 50, 50)
    topBar.BorderSizePixel = 0
    topBar.Parent = mainFrame
    
    -- Coins display
    local coinsLabel = Instance.new("TextLabel")
    coinsLabel.Name = "CoinsLabel"
    coinsLabel.Size = UDim2.new(0.3, 0, 1, 0)
    coinsLabel.Position = UDim2.new(0, 0, 0, 0)
    coinsLabel.BackgroundTransparency = 1
    coinsLabel.Text = "Coins: 0"
    coinsLabel.TextColor3 = Color3.fromRGB(255, 215, 0)
    coinsLabel.TextScaled = true
    coinsLabel.Font = Enum.Font.SourceSansBold
    coinsLabel.Parent = topBar
    
    -- Click power display
    local clickPowerLabel = Instance.new("TextLabel")
    clickPowerLabel.Name = "ClickPowerLabel"
    clickPowerLabel.Size = UDim2.new(0.3, 0, 1, 0)
    clickPowerLabel.Position = UDim2.new(0.35, 0, 0, 0)
    clickPowerLabel.BackgroundTransparency = 1
    clickPowerLabel.Text = "Click Power: 1"
    clickPowerLabel.TextColor3 = Color3.fromRGB(0, 255, 0)
    clickPowerLabel.TextScaled = true
    clickPowerLabel.Font = Enum.Font.SourceSansBold
    clickPowerLabel.Parent = topBar
    
    -- Total clicks display
    local totalClicksLabel = Instance.new("TextLabel")
    totalClicksLabel.Name = "TotalClicksLabel"
    totalClicksLabel.Size = UDim2.new(0.3, 0, 1, 0)
    totalClicksLabel.Position = UDim2.new(0.7, 0, 0, 0)
    totalClicksLabel.BackgroundTransparency = 1
    totalClicksLabel.Text = "Total Clicks: 0"
    totalClicksLabel.TextColor3 = Color3.fromRGB(255, 255, 255)
    totalClicksLabel.TextScaled = true
    totalClicksLabel.Font = Enum.Font.SourceSansBold
    totalClicksLabel.Parent = topBar
    
    -- Main click button
    local clickButton = Instance.new("TextButton")
    clickButton.Name = "ClickButton"
    clickButton.Size = UDim2.new(0.4, 0, 0.4, 0)
    clickButton.Position = UDim2.new(0.3, 0, 0.2, 0)
    clickButton.BackgroundColor3 = Color3.fromRGB(255, 100, 100)
    clickButton.BorderSizePixel = 0
    clickButton.Text = "CLICK ME!"
    clickButton.TextColor3 = Color3.fromRGB(255, 255, 255)
    clickButton.TextScaled = true
    clickButton.Font = Enum.Font.SourceSansBold
    clickButton.Parent = mainFrame
    
    -- Add corner radius to click button
    local corner = Instance.new("UICorner")
    corner.CornerRadius = UDim.new(0.1, 0)
    corner.Parent = clickButton
    
    -- Upgrades section
    local upgradesFrame = Instance.new("Frame")
    upgradesFrame.Name = "UpgradesFrame"
    upgradesFrame.Size = UDim2.new(0.25, 0, 0.6, 0)
    upgradesFrame.Position = UDim2.new(0.05, 0, 0.35, 0)
    upgradesFrame.BackgroundColor3 = Color3.fromRGB(40, 40, 40)
    upgradesFrame.BorderSizePixel = 0
    upgradesFrame.Parent = mainFrame
    
    local upgradesCorner = Instance.new("UICorner")
    upgradesCorner.CornerRadius = UDim.new(0.05, 0)
    upgradesCorner.Parent = upgradesFrame
    
    -- Upgrades title
    local upgradesTitle = Instance.new("TextLabel")
    upgradesTitle.Name = "UpgradesTitle"
    upgradesTitle.Size = UDim2.new(1, 0, 0.1, 0)
    upgradesTitle.Position = UDim2.new(0, 0, 0, 0)
    upgradesTitle.BackgroundTransparency = 1
    upgradesTitle.Text = "UPGRADES"
    upgradesTitle.TextColor3 = Color3.fromRGB(255, 255, 255)
    upgradesTitle.TextScaled = true
    upgradesTitle.Font = Enum.Font.SourceSansBold
    upgradesTitle.Parent = upgradesFrame
    
    -- Click power upgrade button
    local clickPowerUpgrade = Instance.new("TextButton")
    clickPowerUpgrade.Name = "ClickPowerUpgrade"
    clickPowerUpgrade.Size = UDim2.new(0.9, 0, 0.15, 0)
    clickPowerUpgrade.Position = UDim2.new(0.05, 0, 0.15, 0)
    clickPowerUpgrade.BackgroundColor3 = Color3.fromRGB(100, 200, 100)
    clickPowerUpgrade.BorderSizePixel = 0
    clickPowerUpgrade.Text = "Upgrade Click Power\nCost: 100"
    clickPowerUpgrade.TextColor3 = Color3.fromRGB(255, 255, 255)
    clickPowerUpgrade.TextScaled = true
    clickPowerUpgrade.Font = Enum.Font.SourceSans
    clickPowerUpgrade.Parent = upgradesFrame
    
    local clickPowerCorner = Instance.new("UICorner")
    clickPowerCorner.CornerRadius = UDim.new(0.1, 0)
    clickPowerCorner.Parent = clickPowerUpgrade
    
    -- Pet efficiency upgrade button
    local petEfficiencyUpgrade = Instance.new("TextButton")
    petEfficiencyUpgrade.Name = "PetEfficiencyUpgrade"
    petEfficiencyUpgrade.Size = UDim2.new(0.9, 0, 0.15, 0)
    petEfficiencyUpgrade.Position = UDim2.new(0.05, 0, 0.35, 0)
    petEfficiencyUpgrade.BackgroundColor3 = Color3.fromRGB(100, 100, 200)
    petEfficiencyUpgrade.BorderSizePixel = 0
    petEfficiencyUpgrade.Text = "Upgrade Pet Efficiency\nCost: 500"
    petEfficiencyUpgrade.TextColor3 = Color3.fromRGB(255, 255, 255)
    petEfficiencyUpgrade.TextScaled = true
    petEfficiencyUpgrade.Font = Enum.Font.SourceSans
    petEfficiencyUpgrade.Parent = upgradesFrame
    
    local petEfficiencyCorner = Instance.new("UICorner")
    petEfficiencyCorner.CornerRadius = UDim.new(0.1, 0)
    petEfficiencyCorner.Parent = petEfficiencyUpgrade
    
    -- Pets section
    local petsFrame = Instance.new("Frame")
    petsFrame.Name = "PetsFrame"
    petsFrame.Size = UDim2.new(0.25, 0, 0.6, 0)
    petsFrame.Position = UDim2.new(0.7, 0, 0.35, 0)
    petsFrame.BackgroundColor3 = Color3.fromRGB(40, 40, 40)
    petsFrame.BorderSizePixel = 0
    petsFrame.Parent = mainFrame
    
    local petsCorner = Instance.new("UICorner")
    petsCorner.CornerRadius = UDim.new(0.05, 0)
    petsCorner.Parent = petsFrame
    
    -- Pets title
    local petsTitle = Instance.new("TextLabel")
    petsTitle.Name = "PetsTitle"
    petsTitle.Size = UDim2.new(1, 0, 0.1, 0)
    petsTitle.Position = UDim2.new(0, 0, 0, 0)
    petsTitle.BackgroundTransparency = 1
    petsTitle.Text = "PETS"
    petsTitle.TextColor3 = Color3.fromRGB(255, 255, 255)
    petsTitle.TextScaled = true
    petsTitle.Font = Enum.Font.SourceSansBold
    petsTitle.Parent = petsFrame
    
    -- Pet buttons will be created dynamically
    local petsScrollFrame = Instance.new("ScrollingFrame")
    petsScrollFrame.Name = "PetsScrollFrame"
    petsScrollFrame.Size = UDim2.new(1, 0, 0.9, 0)
    petsScrollFrame.Position = UDim2.new(0, 0, 0.1, 0)
    petsScrollFrame.BackgroundTransparency = 1
    petsScrollFrame.BorderSizePixel = 0
    petsScrollFrame.ScrollBarThickness = 8
    petsScrollFrame.Parent = petsFrame
    
    return screenGui, {
        coinsLabel = coinsLabel,
        clickPowerLabel = clickPowerLabel,
        totalClicksLabel = totalClicksLabel,
        clickButton = clickButton,
        clickPowerUpgrade = clickPowerUpgrade,
        petEfficiencyUpgrade = petEfficiencyUpgrade,
        petsScrollFrame = petsScrollFrame
    }
end

-- Update UI functions
local function updateUI()
    local gui = playerGui:FindFirstChild("ClickerSimulatorGUI")
    if not gui then return end
    
    local mainFrame = gui.MainFrame
    local topBar = mainFrame.TopBar
    local upgradesFrame = mainFrame.UpgradesFrame
    local petsFrame = mainFrame.PetsFrame
    
    -- Update top bar
    topBar.CoinsLabel.Text = "Coins: " .. string.format("%.0f", gameData.coins)
    topBar.ClickPowerLabel.Text = "Click Power: " .. string.format("%.1f", gameData.clickPower)
    topBar.TotalClicksLabel.Text = "Total Clicks: " .. gameData.totalClicks
    
    -- Update upgrade buttons
    local clickPowerCost = math.floor(100 * math.pow(2, gameData.upgrades.clickPowerLevel - 1))
    upgradesFrame.ClickPowerUpgrade.Text = "Upgrade Click Power\nCost: " .. clickPowerCost
    
    local petEfficiencyCost = math.floor(500 * math.pow(2, gameData.upgrades.petEfficiencyLevel - 1))
    upgradesFrame.PetEfficiencyUpgrade.Text = "Upgrade Pet Efficiency\nCost: " .. petEfficiencyCost
end

local function createPetButtons()
    local gui = playerGui:FindFirstChild("ClickerSimulatorGUI")
    if not gui then return end
    
    local petsScrollFrame = gui.MainFrame.PetsFrame.PetsScrollFrame
    petsScrollFrame:ClearAllChildren()
    
    local buttonHeight = 0.2
    local buttonSpacing = 0.05
    
    for i, petType in ipairs(gameData.petTypes) do
        local petCount = gameData.pets[i] or 0
        local cost = math.floor(petType.Cost * math.pow(1.8, petCount))
        
        local petButton = Instance.new("TextButton")
        petButton.Name = "PetButton" .. i
        petButton.Size = UDim2.new(0.9, 0, buttonHeight, 0)
        petButton.Position = UDim2.new(0.05, 0, (i - 1) * (buttonHeight + buttonSpacing), 0)
        petButton.BackgroundColor3 = Color3.fromRGB(200, 100, 200)
        petButton.BorderSizePixel = 0
        petButton.Text = petType.Name .. "\nOwned: " .. petCount .. "\nCost: " .. cost
        petButton.TextColor3 = Color3.fromRGB(255, 255, 255)
        petButton.TextScaled = true
        petButton.Font = Enum.Font.SourceSans
        petButton.Parent = petsScrollFrame
        
        local petCorner = Instance.new("UICorner")
        petCorner.CornerRadius = UDim.new(0.1, 0)
        petCorner.Parent = petButton
        
        -- Connect click event
        petButton.MouseButton1Click:Connect(function()
            petSpawnEvent:FireServer(i)
        end)
    end
    
    -- Update canvas size
    petsScrollFrame.CanvasSize = UDim2.new(0, 0, #gameData.petTypes * (buttonHeight + buttonSpacing), 0)
end

-- Event handlers
local function onInitializeData(data)
    gameData = data
    updateUI()
    createPetButtons()
end

local function onUpdateData(data)
    gameData.coins = data.coins
    gameData.clickPower = data.clickPower
    gameData.totalClicks = data.totalClicks
    updateUI()
end

local function onUpgradeResponse(response)
    if response.success then
        gameData.coins = response.coins
        if response.upgradeType == "clickPower" then
            gameData.clickPower = response.value
        elseif response.upgradeType == "petEfficiency" then
            gameData.upgrades.petEfficiencyLevel = response.value
        end
        updateUI()
    end
end

local function onPetResponse(response)
    if response.success then
        gameData.coins = response.coins
        gameData.pets[response.petType] = response.petCount
        createPetButtons()
    end
end

-- Connect RemoteEvents
local initEvent = remoteEvents:WaitForChild("InitializeData")
local updateEvent = remoteEvents:WaitForChild("UpdateData")
local upgradeResponseEvent = remoteEvents:WaitForChild("UpgradeResponse")
local petResponseEvent = remoteEvents:WaitForChild("PetResponse")

initEvent.OnClientEvent:Connect(onInitializeData)
updateEvent.OnClientEvent:Connect(onUpdateData)
upgradeResponseEvent.OnClientEvent:Connect(onUpgradeResponse)
petResponseEvent.OnClientEvent:Connect(onPetResponse)

-- Create GUI and connect events
local screenGui, uiElements = createMainGUI()

-- Click button event
uiElements.clickButton.MouseButton1Click:Connect(function()
    clickEvent:FireServer()
    
    -- Visual feedback
    local originalSize = uiElements.clickButton.Size
    local tween = TweenService:Create(uiElements.clickButton, TweenInfo.new(0.1), {Size = originalSize * 0.9})
    tween:Play()
    tween.Completed:Connect(function()
        local returnTween = TweenService:Create(uiElements.clickButton, TweenInfo.new(0.1), {Size = originalSize})
        returnTween:Play()
    end)
end)

-- Upgrade button events
uiElements.clickPowerUpgrade.MouseButton1Click:Connect(function()
    upgradeEvent:FireServer("clickPower")
end)

uiElements.petEfficiencyUpgrade.MouseButton1Click:Connect(function()
    upgradeEvent:FireServer("petEfficiency")
end)

-- Keyboard input for clicking (spacebar)
UserInputService.InputBegan:Connect(function(input, gameProcessed)
    if gameProcessed then return end
    
    if input.KeyCode == Enum.KeyCode.Space then
        clickEvent:FireServer()
    end
end)

print("Clicker Simulator Client Script loaded successfully!")
