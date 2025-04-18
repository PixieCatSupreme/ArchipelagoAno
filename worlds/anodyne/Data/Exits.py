from worlds.anodyne.Options import BeachGauntletGate, OverworldGauntletGate, PostgameBlank, OverworldFieldsGate, \
    WindmillEntranceGate, WindmillMiddleGate, WindmillTopGate, PostgameEnd, FieldsGate, EndgameRequirement

all_exits = [
    ["Menu", "Blank start", []],
    ["Apartment floor 1", "Suburb", []],
    ["Suburb", "Apartment floor 1", ["Jump Shoes"]],
    ["Apartment floor 1", "Apartment floor 2", []],
    ["Apartment floor 2", "Apartment floor 1", []],
    ["Apartment floor 1", "Apartment floor 2 top left", ["Small Key (Apartment):4"]],
    ["Apartment floor 2 top left", "Apartment floor 1", ["Small Key (Apartment):4"]],
    ["Apartment floor 2", "Apartment floor 3", ["Small Key (Apartment):3", "Jump Shoes"]],
    ["Apartment floor 3", "Apartment floor 2", ["Small Key (Apartment):3", "Jump Shoes"]],
    ["Apartment floor 2 top left", "Apartment floor 1 top left", ["Combat"]],
    ["Apartment floor 1 top left", "Apartment floor 2 top left", ["Combat"]],
    ["Beach", "Fields", []],
    ["Fields", "Beach", []],
    ["Beach", "Red Sea", ["Combat"]],
    ["Red Sea", "Beach", []],
    ["Beach", "Beach Gauntlet", ["Combat",BeachGauntletGate.typename()]],
    ["Bedroom", "Overworld", []],
    ["Overworld", "Bedroom", []],
    ["Bedroom", "Bedroom exit", ["Combat", "Temple Boss Access"]],
    # You can always use return to entrance to get to the start from the exit
    ["Bedroom exit", "Bedroom", []],
    ["Bedroom exit", "Overworld post windmill", ["Temple of the Seeing One Statue", "Small Key (Temple of the Seeing One):3",
                                                 "Combat"]],
    ["Overworld post windmill", "Bedroom exit", ["Temple of the Seeing One Statue", "Small Key (Temple of the Seeing One):3",
                                                 "Combat"]],
    ["Bedroom drawer", "Drawer", ["Progressive Swap:2"]],
    ["Drawer", "Bedroom drawer", ["Progressive Swap:2"]],
    ["Bedroom drawer", "Overworld", ["Progressive Swap:2"]],
    ["Overworld Gauntlet", "Bedroom drawer", ["Progressive Swap:2", "Combat"]],
    ["Overworld", "Overworld Gauntlet", [OverworldGauntletGate.typename(), "Combat"]],
    ["Blank start", "Nexus bottom", []],
    # The secret windmill doesn't require any keys.
    ["Blank windmill", "Fields", ["Progressive Swap:2"]],
    ["Fields", "Blank windmill", ["Progressive Swap:2"]],
    ["Blank windmill", "Drawer dark", [PostgameBlank.typename()]],
    ["Drawer dark", "Blank windmill", [PostgameBlank.typename()]],
    ["Blue", "Go top", []],
    ["Go top", "Blue", []],
    ["Cell", "Circus", []],
    ["Circus", "Cell", []],
    ["Circus", "Circus 2", ["Small Key (Circus):1", "Combat", "Jump Shoes"]],
    ["Circus 2", "Circus 3", ["Small Key (Circus):2"]],
    ["Circus 3", "Circus 4", ["Small Key (Circus):3"]],
    ["Cell", "Red Cave exit", ["Red Cave Statue"]],
    ["Red Cave exit", "Cell", ["Red Cave Statue"]],
    ["Cliff", "Forest", []],
    ["Forest", "Cliff", []],
    ["Cliff", "Crowd floor 2", []],
    ["Crowd floor 2", "Cliff", []],
    ["Cliff", "Crowd jump challenge", []],
    ["Crowd jump challenge", "Cliff", []],
    ["Cliff post windmill", "Space", []],
    ["Space", "Cliff post windmill", []],
    ["Crowd floor 1", "Crowd exit", ["Defeat The Wall"]],
    ["Crowd exit", "Crowd floor 1", ["Combat"]],
    ["Crowd exit", "Cliff post windmill", ["Mountain Cavern Statue"]],
    ["Cliff post windmill", "Crowd exit", ["Mountain Cavern Statue"]],
    # Technically this entrance works from floor 2, but only if you've used *this* entrance before, which is
    # logically the same as only this entrance existing.
    ["Crowd floor 3", "Crowd floor 1", ["Combat", "Small Key (Mountain Cavern):3"]],
    ["Crowd floor 2", "Crowd floor 3", []],
    ["Crowd floor 3", "Crowd floor 2", []],
    # Return to entrance
    ["Crowd floor 1", "Crowd floor 2", []],
    ["Crowd exit", "Crowd floor 2", []],
    ["Debug", "Nexus top", []],
    ["Nexus top", "Debug", []],
    ["Drawer dark", "Nexus top", []],
    ["Nexus top", "Drawer dark", []],
    ["Fields", "Overworld", [OverworldFieldsGate.typename()]],
    ["Overworld", "Fields", [OverworldFieldsGate.typename()]],
    ["Fields", "Forest", []],
    ["Forest", "Fields", []],
    ["Fields", "Fields Lake", ["Combat", "Jump Shoes"]],
    ["Fields Lake", "Fields", []],
    ["Fields", "Fields Past Gate", [FieldsGate.typename()]],
    ["Fields Past Gate", "Fields", [FieldsGate.typename()]],
    ["Terminal", "Fields Past Gate", ["Jump Shoes"]],
    ["Fields Past Gate", "Terminal", ["Jump Shoes"]],
    ["Fields", "Fields North Secret Area", ["Progressive Swap:2"]],
    ["Fields North Secret Area", "Fields", ["Progressive Swap:2"]],
    ["Fields", "Windmill entrance", [WindmillEntranceGate.typename()]],
    ["Windmill entrance", "Fields", [WindmillEntranceGate.typename()]],
    ["Windmill entrance", "Windmill", [WindmillMiddleGate.typename(),WindmillTopGate.typename()]],
    ["Windmill", "Windmill entrance", [WindmillMiddleGate.typename(),WindmillTopGate.typename()]],
    ["Terminal top", "Terminal", [EndgameRequirement.typename(), "Defeat Sage"]],
    ["Terminal", "Terminal top", [EndgameRequirement.typename()]],
    ["Terminal top", "Go bottom", ["Defeat Sage"]],
    ["Go bottom", "Terminal top", []],
    # Reverse isn't possible without cheats because of the blocks
    ["Go bottom", "Go top", ["Progressive Swap:1", "GO Color Puzzle"]],
    # Requires beating Blue, which requires Jump Shoes and Combat.
    ["Go top", "Happy", ["Jump Shoes", "Combat"]],
    # You can clip through the happy blocker.
    ["Happy", "Go top", []],
    ["Hotel roof", "Space", []],
    ["Space", "Hotel roof", []],
    ["Space", "Space Gauntlet", ["Progressive Swap:2", "Combat", "Jump Shoes"]],
    ["Space Gauntlet", "Space", ["Progressive Swap:2"]],
    ["Hotel roof", "Hotel floor 4", ["Jump Shoes"]],
    ["Hotel floor 4", "Hotel roof", ["Jump Shoes"]],
    ["Hotel floor 4", "Hotel floor 3", ["Combat", "Jump Shoes", "Small Key (Hotel):1"]],
    ["Hotel floor 3", "Hotel floor 4", ["Combat", "Jump Shoes"]],
    ["Hotel floor 3", "Hotel floor 2", ["Small Key (Hotel):4"]],
    ["Hotel floor 2", "Hotel floor 3", []],
    # Door requires key and has key behind it
    ["Hotel floor 3", "Hotel floor 2 right", ["Small Key (Hotel):6"]],
    ["Hotel floor 2 right", "Hotel floor 3", []],
    ["Hotel floor 2", "Hotel floor 1", []],
    ["Hotel floor 1", "Hotel floor 2", []],
    ["Nexus bottom", "Street", []],
    ["Street", "Nexus bottom", []],
    ["Nexus top", "Boss Rush", ["Combat","Jump Shoes"]],
    ["Boss Rush", "Nexus top", []],
    ["Nexus top", "Blank ending", [PostgameEnd.typename()]],
    ["Blank ending", "Nexus top", [PostgameEnd.typename()]],
    ["Overworld post windmill", "Suburb", []],
    ["Suburb", "Overworld post windmill", []],
    ["Overworld post windmill", "Overworld", []],
    ["Red Cave center", "Red Sea", []],
    ["Red Sea", "Red Cave center", []],
    ["Red Cave left", "Red Sea", []],
    ["Red Sea", "Red Cave left", ["RedCave-Left"]],
    ["Red Cave right", "Red Sea", []],
    ["Red Sea", "Red Cave right", ["RedCave-Right"]],
    ["Red Cave top", "Red Sea", []],
    ["Red Sea", "Red Cave top", ["RedCave-Top"]],
    ["Red Cave bottom", "Red Sea", []],
    ["Red Sea", "Red Cave bottom", []],
    ["Red Cave top", "Red Cave exit", ["Defeat Rogue"]],
    # Return to entrance
    ["Red Cave exit", "Red Cave top", []],
    # Hidden path
    ["Red Cave Isaac", "Red Sea", []],
    ["Red Sea", "Red Cave Isaac", []],
    ["Street", "Overworld", ["Combat", "Small Key (Street):1"]],
    ["Suburb", "Suburb card house", ["Combat"]],
    ["Suburb card house", "Suburb", ["Combat"]],
]

secret_path_connections = [
    ["Fields Past Gate", "Fields North Secret Area", []],
    ["Fields North Secret Area", "Fields Past Gate", []]
]