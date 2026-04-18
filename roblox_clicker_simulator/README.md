# Roblox Clicker Simulator

A complete clicker simulator game for Roblox with pets, upgrades, and auto-clicking functionality.

## Features

- **Clicking System**: Click to earn coins with increasing click power
- **Pet System**: Purchase pets that automatically click for you
- **Upgrade System**: Upgrade your click power and pet efficiency
- **Data Persistence**: Player progress is saved automatically
- **Modern UI**: Clean, responsive interface with visual feedback

## Installation

1. Create a new Roblox place
2. In ServerScriptService, create a new Server Script and paste the contents of `MainScript.server.lua`
3. In StarterPlayer > StarterPlayerScripts, create a new Local Script and paste the contents of `ClientScript.client.lua`
4. The game will automatically create all necessary RemoteEvents and UI elements

## Game Mechanics

### Clicking
- Each click earns coins based on your current click power
- Click power can be upgraded using coins
- Spacebar can also be used to click

### Pets
- Pets automatically click for you every second
- Each pet type has different auto-click power and cost
- Pet costs increase exponentially with each purchase
- Pet efficiency can be upgraded to increase their auto-click power

### Upgrades
- **Click Power**: Increases coins earned per click
- **Pet Efficiency**: Increases all pets' auto-click power

### Pet Types
1. **Basic Cat** - Cost: 100, Auto-click: 0.1
2. **Golden Dog** - Cost: 500, Auto-click: 0.5
3. **Dragon** - Cost: 2,500, Auto-click: 2.5
4. **Phoenix** - Cost: 10,000, Auto-click: 10

## Configuration

You can modify the game configuration in `MainScript.server.lua`:

```lua
local GAME_CONFIG = {
    BASE_CLICK_POWER = 1,
    CLICK_POWER_MULTIPLIER = 1.5,
    BASE_PET_COST = 100,
    PET_COST_MULTIPLIER = 1.8,
    PET_AUTO_CLICK_INTERVAL = 1, -- seconds
    PET_AUTO_CLICK_POWER = 0.1
}
```

## Data Storage

Player data is automatically saved every 30 seconds and when players leave. The following data is persisted:
- Coins
- Click power level
- Total clicks
- Pet counts
- Upgrade levels

## Customization

### Adding New Pet Types
Add new entries to the `PET_TYPES` table in `MainScript.server.lua`:

```lua
{
    Name = "Your Pet Name",
    Cost = 1000,
    AutoClickPower = 1.0,
    Model = "rbxassetid://YOUR_MODEL_ID"
}
```

### Modifying UI
The UI is created in `ClientScript.client.lua` in the `createMainGUI()` function. You can customize colors, sizes, and layout as needed.

### Adding New Upgrades
1. Add the upgrade type to the server script's `handleUpgrade()` function
2. Add corresponding UI elements in the client script
3. Update the upgrade cost calculation logic

## Troubleshooting

- **Data not saving**: Check that DataStoreService is enabled in your game settings
- **UI not appearing**: Ensure the client script is in StarterPlayer > StarterPlayerScripts
- **RemoteEvents not working**: Make sure both scripts are running and the server script creates the RemoteEvents

## Performance Notes

- Pet auto-clicking runs on separate threads to avoid blocking
- UI updates are optimized to only refresh when necessary
- Data is saved asynchronously to prevent lag

## Future Enhancements

Potential features to add:
- Prestige system
- Achievements
- Sound effects
- Particle effects for clicking
- More pet types
- Pet evolution system
- Multiplayer competitions
- Daily rewards
