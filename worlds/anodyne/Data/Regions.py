all_regions = [
    "Menu",
    "Apartment floor 1",
    "Apartment floor 1 top left",
    "Apartment floor 2",
    "Apartment floor 2 top left",
    "Apartment floor 3",
    "Beach",
    "Bedroom",
    "Bedroom drawer",
    "Bedroom exit",
    "Blank start",
    "Blank windmill",
    "Blank ending",
    "Blue",
    "Cell",
    "Circus",
    "Circus 2",
    "Circus 3",
    "Circus 4",
    "Cliff",
    "Cliff post windmill",
    "Crowd floor 1",
    "Crowd floor 2",
    "Crowd floor 3",
    "Crowd jump challenge",
    "Debug",
    "Drawer",
    "Drawer dark",
    "Fields",
    "Forest",
    "Go bottom",
    "Go top",
    "Happy",
    "Hotel roof",
    "Hotel floor 4",
    "Hotel floor 3",
    "Hotel floor 2",
    "Hotel floor 2 right",
    "Hotel floor 1",
    "Nexus bottom",
    "Nexus top",
    "Overworld",
    "Overworld post windmill",
    "Red Cave top",
    "Red Cave left",
    "Red Cave center",
    "Red Cave right",
    "Red Cave bottom",
    "Red Cave Isaac",
    "Red Sea",
    "Suburb",
    "Suburb card house",
    "Space",
    "Street",
    "Terminal",
    "Windmill entrance",
    "Windmill",
    "Boss Rush"
]

dungeon_areas = {
    "Temple of the Seeing One": ["Bedroom", "Bedroom exit"],
    "Red Cave": ["Red Cave top",
                 "Red Cave left",
                 "Red Cave center",
                 "Red Cave right",
                 "Red Cave bottom",
                 "Red Cave Isaac"],
    "Mountain Cavern": ["Crowd floor 1",
                        "Crowd floor 2",
                        "Crowd floor 3",
                        "Crowd jump challenge"],
    "Hotel": ["Hotel roof",
              "Hotel floor 4",
              "Hotel floor 3",
              "Hotel floor 2",
              "Hotel floor 2 right",
              "Hotel floor 1"],
    "Apartment": ["Apartment floor 1",
                  "Apartment floor 1 top left",
                  "Apartment floor 2",
                  "Apartment floor 2 top left",
                  "Apartment floor 3"],
    "Circus": ["Circus", "Circus 2", "Circus 3", "Circus 4"],
    "Street": ["Street"],
}

dungeon_area_to_dungeon = {name: dungeon for dungeon, names in dungeon_areas.items() for name in names}

# The Street nexus gate is open from the start
regions_with_nexus_gate = [
    "Apartment floor 1",
    "Beach",
    "Bedroom exit",
    "Blue",
    "Cell",
    "Circus",
    "Cliff",
    "Crowd floor 1",
    "Fields",
    "Forest",
    "Go bottom",
    "Happy",
    "Hotel floor 4",
    "Overworld",
    "Red Cave top",
    "Red Sea",
    "Suburb",
    "Space",
    "Terminal",
    "Windmill entrance",
]

early_nexus_gates = [
    "Beach",
    "Cliff",
    "Fields",
    "Forest",
    "Overworld",
    "Red Sea"
]

endgame_nexus_gates = [
    "Blue",
    "Go bottom",
    "Happy",
]

postgame_regions = [
    "Blank windmill",
    "Blank ending",
    "Debug",
    "Drawer",
    "Drawer dark",
    "Boss Rush",
    "Nexus top",
]
