all_exits = [
    ["Menu", "Blank start", []],
    ["Apartment floor 1", "Suburb", []],
    ["Suburb", "Apartment floor 1", ["Jump Shoes"]],
    ["Apartment floor 1", "Apartment floor 2", []],
    ["Apartment floor 2", "Apartment floor 1", []],
    ["Apartment floor 1", "Apartment floor 2 top left", ["Keys:Apartment:4"]],
    ["Apartment floor 2 top left", "Apartment floor 1", ["Keys:Apartment:4"]],
    ["Apartment floor 2", "Apartment floor 3", ["Keys:Apartment:3"]],
    ["Apartment floor 3", "Apartment floor 2", ["Keys:Apartment:3"]],
    ["Apartment floor 2 top left", "Apartment floor 1 top left", ["Combat"]],
    ["Apartment floor 1 top left", "Apartment floor 2 top left", ["Combat"]],
    ["Beach", "Fields", []],
    ["Fields", "Beach", []],
    ["Beach", "Red Sea", ["Combat"]],
    ["Red Sea", "Beach", []],
    ["Bedroom", "Overworld", []],
    ["Overworld", "Bedroom", []],
    ["Bedroom", "Bedroom exit", ["Combat", "Keys:Temple of the Seeing One:2"]],
    # You can always use return to entrance to get to the start from the exit
    ["Bedroom exit", "Bedroom", []],
    ["Bedroom exit", "Overworld post windmill", ["Temple of the Seeing One Statue", "Keys:Temple of the Seeing One:3"]],
    ["Overworld post windmill", "Bedroom exit", ["Temple of the Seeing One Statue", "Keys:Temple of the Seeing One:3"]],
    ["Bedroom drawer", "Drawer", ["Swap:2"]],
    ["Drawer", "Bedroom drawer", ["Swap:2"]],
    ["Bedroom drawer", "Overworld", ["Swap:2"]],
    ["Overworld", "Bedroom drawer", ["Swap:2", "Cards:4", "Combat"]],
    ["Blank start", "Nexus bottom", []],
    # The secret windmill doesn't require any keys.
    ["Blank windmill", "Fields", ["Swap:2"]],
    ["Fields", "Blank windmill", ["Swap:2"]],
    ["Blank windmill", "Drawer dark", ["Cards:47"]],
    ["Drawer dark", "Blank windmill", ["Cards:47"]],
    ["Blue", "Go top", []],
    ["Go top", "Blue", []],
    ["Cell", "Circus", []],
    ["Circus", "Cell", []],
    ["Circus", "Circus 2", ["Keys:Circus:1", "Combat", "Jump Shoes"]],
    ["Circus 2", "Circus 3", ["Keys:Circus:2"]],
    ["Circus 3", "Circus 4", ["Keys:Circus:3"]],
    ["Cell", "Red Cave top", ["Red Cave Statue"]],
    ["Red Cave top", "Cell", ["Red Cave Statue"]],
    ["Cliff", "Forest", []],
    ["Forest", "Cliff", []],
    ["Cliff", "Crowd floor 2", []],
    ["Crowd floor 2", "Cliff", []],
    ["Cliff", "Crowd jump challenge", []],
    ["Crowd jump challenge", "Cliff", []],
    ["Cliff post windmill", "Space", []],
    ["Space", "Cliff post windmill", []],
    ["Crowd floor 1", "Cliff post windmill", ["Mountain Cavern Statue"]],
    ["Cliff post windmill", "Crowd floor 1", ["Mountain Cavern Statue"]],
    # Technically this entrance works from floor 2, but only if you've used *this* entrance before, which is
    # logically the same as only this entrance existing.
    ["Crowd floor 3", "Crowd floor 1", ["Combat", "Keys:Mountain Cavern:3"]],
    ["Crowd floor 2", "Crowd floor 3", []],
    ["Crowd floor 3", "Crowd floor 2", []],
    # Essentially one way, because the reverse direction is blocked by a gate the first time
    ["Crowd floor 1", "Crowd floor 2", ["Combat", "Jump Shoes"]],
    ["Debug", "Nexus top", []],
    ["Nexus top", "Debug", []],
    ["Drawer dark", "Nexus top", []],
    ["Nexus top", "Drawer dark", []],
    ["Fields", "Overworld", ["Green Key"]],
    ["Overworld", "Fields", ["Green Key"]],
    ["Fields", "Forest", []],
    ["Forest", "Fields", []],
    ["Fields", "Terminal", ["Red Key", "Jump Shoes"]],
    ["Terminal", "Fields", ["Red Key", "Jump Shoes"]],
    ["Fields", "Windmill entrance", ["Green Key"]],
    ["Windmill entrance", "Fields", ["Green Key"]],
    ["Windmill entrance", "Windmill", ["Red Key", "Blue Key"]],
    ["Windmill", "Windmill entrance", ["Red Key", "Blue Key"]],
    ["Go bottom", "Terminal", ["Endgame Access"]],
    ["Terminal", "Go bottom", ["Endgame Access"]],
    ["Go bottom", "Go top", ["Swap:1", "Defeat Servants", "Defeat Watcher", "Defeat Manager"]],
    ["Go top", "Go bottom", ["Swap:1"]],
    # Requires beating Blue, which requires Jump Shoes.
    # Treated as one-way because you can't unlock the door from the Happy side.
    # You CAN clip through it though... add the connection or patch it on the client side?
    ["Go top", "Happy", ["Jump Shoes"]],
    ["Hotel roof", "Space", []],
    ["Space", "Hotel roof", []],
    ["Hotel roof", "Hotel floor 4", []],
    ["Hotel floor 4", "Hotel roof", []],
    ["Hotel floor 4", "Hotel floor 3", ["Combat", "Jump Shoes"]],
    ["Hotel floor 3", "Hotel floor 4", ["Combat", "Jump Shoes"]],
    ["Hotel floor 3", "Hotel floor 2", ["Keys:Hotel:3"]],
    ["Hotel floor 2", "Hotel floor 3", []],
    # Door requires key and has key behind it
    ["Hotel floor 3", "Hotel floor 2 right", ["Keys:Hotel:6"]],
    ["Hotel floor 2 right", "Hotel floor 3", []],
    ["Hotel floor 2", "Hotel floor 1", []],
    ["Hotel floor 1", "Hotel floor 2", []],
    ["Nexus bottom", "Street", []],
    ["Street", "Nexus bottom", []],
    ["Nexus top", "Boss Rush", []],
    ["Boss Rush", "Nexus top", []],
    ["Nexus top", "Blank ending", ["Cards:49"]],
    ["Blank ending", "Nexus top", ["Cards:49"]],
    ["Overworld post windmill", "Suburb", []],
    ["Suburb", "Overworld post windmill", []],
    ["Overworld post windmill", "Overworld", []],
    ["Red Cave center", "Red Sea", []],
    ["Red Sea", "Red Cave center", []],
    ["Red Cave left", "Red Sea", []],
    ["Red Sea", "Red Cave left", ["RedCave:Left"]],
    ["Red Cave right", "Red Sea", []],
    ["Red Sea", "Red Cave right", ["RedCave:Right"]],
    ["Red Cave top", "Red Sea", []],
    ["Red Sea", "Red Cave top", ["RedCave:Top"]],
    ["Red Cave bottom", "Red Sea", []],
    ["Red Sea", "Red Cave bottom", []],
    # Hidden path
    ["Red Cave Isaac", "Red Sea", []],
    ["Red Sea", "Red Cave Isaac", []],
    ["Street", "Overworld", ["Combat", "Keys:Street:1"]],
    ["Suburb", "Suburb card house", ["Combat"]],
    ["Suburb card house", "Suburb", ["Combat"]],
]