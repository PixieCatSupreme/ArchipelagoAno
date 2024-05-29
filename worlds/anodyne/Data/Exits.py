exits_by_region = {
    "Menu": {
        "New Game": [
            ["Menu", "Blank start", []]
        ]
    },
    "Apartment floor 1": {
        "Apartment floor 1 to Suburb exit": [
            ["Apartment floor 1", "Suburb", []],
            ["Suburb", "Apartment floor 1", []]
        ],
        "Apartment floor 1 to Apartment floor 2": [
            ["Apartment floor 1", "Apartment floor 2", []],
            ["Apartment floor 2", "Apartment floor 1", []]
        ],
        "Apartment floor 1 to Apartment floor 2 top left": [
            ["Apartment floor 1", "Apartment floor 2 top left", ["Keys:4"]],
            ["Apartment floor 2 top left", "Apartment floor 1", ["Keys:4"]]
        ]
    },
    "Apartment floor 2": {
        "Apartment floor 2 to Apartment floor 3": [
            ["Apartment floor 2", "Apartment floor 3", ["Keys:3"]],
            ["Apartment floor 3", "Apartment floor 2", ["Keys:3"]]
        ]
    },
    "Apartment floor 2 top left": {
        "Apartment floor 2 top left to Apartment floor 1 top left": [
            ["Apartment floor 2 top left", "Apartment floor 1 top left", ["Broom"]],
            ["Apartment floor 1 top left", "Apartment floor 2 top left", ["Broom"]]
        ]
    },
    "Beach": {
        "Beach to Fields exit": [
            ["Beach", "Fields", []],
            ["Fields", "Beach", []]
        ],
        "Beach to Red Sea exit": [
            ["Beach", "Red Sea", ["Broom"]],
            ["Red Sea", "Beach", []]
        ]
    },
    "Bedroom": {
        "Bedroom to Overworld exit": [
            ["Bedroom", "Overworld", []],
            ["Overworld", "Bedroom", []]
        ],
        "Bedroom to Overworld post windmill exit": [
            ["Bedroom", "Overworld post windmill", ["Windmill activated", "Broom", "Keys:3"]],
            ["Overworld post windmill", "Bedroom", ["Windmill activated", "Broom", "Keys:3"]]
        ]
    },
    "Bedroom drawer": {
        "Bedroom drawer to Drawer exit": [
            ["Bedroom drawer", "Drawer", ["Swap"]],
            ["Drawer", "Bedroom drawer", ["Swap"]]
        ],
        "Bedroom drawer to Overworld exit": [
             ["Bedroom drawer", "Overworld", ["Swap"]],
             ["Overworld", "Bedroom drawer", ["Swap"]]
         ]
    },
    "Blank start": {
        "Blank start to Nexus exit": [
            ["Blank start", "Nexus bottom", []],
        ]
    },
    "Blank windmill": {
        "Blank windmill to Windmill exit": [
            ["Blank windmill", "Windmill", ["Swap"]],
            ["Windmill", "Blank windmill", ["Swap"]]
        ],
        "Blank windmill to Drawer dark exit": [
            ["Blank windmill", "Drawer dark", ["Cards:47"]],
            ["Drawer dark", "Blank windmill", ["Cards:47"]]
        ]
    },
    "Blue": {
        "Blue to Go top exit": [
            ["Blue", "Go top", []],
            ["Go top", "Blue", []]
        ]
    },
    "Cell": {
        "Cell to Circus exit": [
            ["Cell", "Circus", []],
            ["Circus", "Cell", []]
        ],
        "Cell to Red Cave top exit": [
            ["Cell", "Red Cave top", ["Windmill activated"]],
            ["Red Cave top", "Cell", ["Windmill activated"]]
        ],
    },
    "Cliff": {
        "Cliff to Forest exit": [
            ["Cliff", "Forest", []],
            ["Forest", "Cliff", []]
        ],
        "Cliff to Crowd floor 2 exit": [
            ["Cliff", "Crowd floor 2", []],
            ["Crowd floor 2", "Cliff", []]
        ],
        "Cliff to Crowd jump challenge exit": [
            ["Cliff", "Crowd jump challenge", []],
            ["Crowd jump challenge", "Cliff", []]
        ]
    },
    "Cliff post windmill": {
        "Cliff post windmill to Space exit": [
            ["Cliff post windmill", "Space", []],
            ["Space", "Cliff post windmill", []]
        ],
        "Cliff post windmill to Crowd exit": [
            ["Crowd floor 1", "Cliff post windmill", ["Windmill activated"]],
            ["Cliff post windmill", "Crowd floor 1", ["Windmill activated"]]
        ]
    },
    "Crowd floor 2": {
        "Crowd floor 2 to Crowd floor 1 exit": [
            ["Crowd floor 2", "Crowd floor 1", []],
            ["Crowd floor 1", "Crowd floor 2", []]
        ],
        "Crowd floor 2 to Crowd floor 3 exit": [
            ["Crowd floor 2", "Crowd floor 3", []],
            ["Crowd floor 3", "Crowd floor 2", []]
        ]
    },
    "Debug": {
        "Debug to Nexus top exit": [
            ["Debug", "Nexus top", []],
            ["Nexus top", "Debug", []]
        ]
    },
    "Drawer dark": {
        "Drawer dark to Nexus top exit": [
             ["Drawer dark", "Nexus top", []],
             ["Nexus top", "Drawer dark", []]
         ]
    },
    "Fields": {
        "Fields to Overworld exit": [
            ["Fields", "Overworld", ["Green Key"]],
            ["Overworld", "Fields", ["Green Key"]]
        ],
        "Fields to Forest exit": [
            ["Fields", "Forest", ["Goldman moved"]],
            ["Forest", "Fields", []]
         ],
        "Fields to Terminal exit": [
             ["Fields", "Terminal", ["Red Key", "Jump Shoes"]],
             ["Terminal", "Fields", ["Red Key", "Jump Shoes"]]
         ],
        "Fields to Windmill exit": [
             ["Fields", "Windmill", ["Green Key", "Red Key", "Blue Key"]],
             ["Windmill", "Fields", ["Green Key", "Red Key", "Blue Key"]]
         ]
    },
    "Go bottom": {
        "Go bottom to Terminal exit": [
             ["Go bottom", "Terminal", ["Cards:36"]],
             ["Terminal", "Go bottom", ["Cards:36"]]
         ],
        "Go bottom to Go top exit": [
             ["Go bottom", "Go top", ["Swap"]],
             ["Go top", "Go bottom", ["Swap"]]
         ]
    },
    "Go top": {
        "Go top to Happy exit": [
             ["Go top", "Happy", ["Blue completed"]],
             ["Happy", "Go top", ["Blue completed"]]
         ]
    },
    "Hotel roof": {
        "Hotel roof to Space exit": [
             ["Hotel roof", "Space", []],
             ["Space", "Hotel roof", []]
         ],
        "Hotel roof to Hotel floor 4": [
            ["Hotel roof", "Hotel floor 4", []],
            ["Hotel floor 4", "Hotel roof", []]
        ]
    },
    "Hotel floor 4": {
        "Hotel floor 4 to Hotel floor 3": [
            ["Hotel floor 4", "Hotel floor 3", ["Broom", "Jump Shoes"]],
            ["Hotel floor 3", "Hotel floor 4", ["Broom", "Jump Shoes"]]
        ]
    },
    "Hotel floor 3": {
        "Hotel floor 3 to Hotel floor 2": [
            ["Hotel floor 3", "Hotel floor 2", ["Keys:3"]],
            ["Hotel floor 2", "Hotel floor 3", []]
        ],
        "Hotel floor 3 to Hotel floor 2 right": [
            # Door requires key and has key behind it
            ["Hotel floor 3", "Hotel floor 2 right", ["Keys:6"]],
            ["Hotel floor 2 right", "Hotel floor 3", []]
        ]
    },
    "Hotel floor 2": {
        "Hotel floor 2 to Hotel floor 1": [
            ["Hotel floor 2", "Hotel floor 1", []],
            ["Hotel floor 1", "Hotel floor 2", []]
        ]
    },
    "Nexus bottom": {
        "Nexus bottom to Street exit": [
            ["Nexus bottom", "Street", []],
            ["Street", "Nexus bottom", []]
        ],
    },
    "Nexus top": {
        "Nexus top to Boss Rush exit": [
             ["Nexus top", "Boss Rush", []],
             ["Boss Rush", "Nexus top", []]
         ],
        "Nexus top to Blank ending exit": [
             ["Nexus top", "Blank ending", ["Cards:49"]],
             ["Blank ending", "Nexus top", ["Cards:49"]]
         ]
    },
    "Overworld post windmill": {
        "Overworld post windmill to Suburb ending exit": [
             ["Overworld post windmill", "Suburb", []],
             ["Suburb", "Overworld post windmill", []]
         ],
        "Overworld post windmill to Overworld exit": [
             ["Overworld post windmill", "Overworld", []]
         ]
    },
    "Red Cave center": {
        "Red Cave center to Red Sea exit": [
             ["Red Cave center", "Red Sea", []],
             ["Red Sea", "Red Cave center", []]
         ]
    },
    "Red Cave left": {
        "Red Cave left to Red Sea exit": [
             ["Red Cave left", "Red Sea", []],
             ["Red Sea", "Red Cave left", ["Center left tentacle hit"]]
         ]
    },
    "Red Cave right": {
        "Red Cave right to Red Sea exit": [
             ["Red Cave right", "Red Sea", []],
             ["Red Sea", "Red Cave right", ["Center right tentacle hit"]]
         ]
    },
    "Red Cave top": {
        "Red Cave top to Red Sea exit": [
             ["Red Cave top", "Red Sea", []],
             ["Red Sea", "Red Cave top", ["Left tentacle hit", "Right tentacle hit"]]
         ]
    },
    "Red Cave bottom": {
        "Red Cave bottom to Red Sea exit": [
             ["Red Cave bottom", "Red Sea", []],
             ["Red Sea", "Red Cave bottom", []]
         ]
    },
    # Hidden path
    "Red Cave Isaac": {
        "Red Cave Isaac to Red Sea exit": [
             ["Red Cave Isaac", "Red Sea", []],
             ["Red Sea", "Red Cave Isaac", []]
         ]
    },
    "Street": {
        "Street to Overworld exit": [
             ["Street", "Overworld", ["Broom", "Keys:1"]],
         ]
    },
    "Suburb": {
        "Suburb to Suburb card house": [
            ["Suburb", "Suburb card house", ["Broom"]],
            ["Suburb card house", "Suburb", ["Broom"]]
        ]
    }
}
