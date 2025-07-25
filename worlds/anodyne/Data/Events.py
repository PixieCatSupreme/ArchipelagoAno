from worlds.anodyne.Data.Regions import Blank, Bedroom, Crowd, Windmill, Hotel, Circus, Apartment, Terminal, Go, Blue, \
    Happy, Red_Cave, RegionEnum

events_by_region:dict[RegionEnum,dict[str,list[str]]] = {
    Bedroom.exit: {
        "Defeat Seer": ["Combat"],
        "Grab Green Key": []
    },
    Crowd.floor_1: {
        "Defeat The Wall": ["Combat", "Jump Shoes"],
        "Grab Blue Key": ["Defeat The Wall"]
    },
    Windmill.DEFAULT: {
        "Windmill activated": [],
    },
    Hotel.floor_1: {
        "Defeat Manager": ["Small Key (Hotel):6", "Combat"],
    },
    Circus.boss_gauntlet: {
        "Defeat Servants": ["Combat", "Jump Shoes"],
    },
    Apartment.floor_3: {
        "Defeat Watcher": ["Combat", "Small Key (Apartment):4"],
    },
    Terminal.top: {
        "Defeat Sage": ["Combat", "Jump Shoes"],
    },
    Go.top: {
        "Defeat Briar": ["Combat", "Complete Blue", "Complete Happy"],
    },
    Blue.DEFAULT: {
        "Blue Completion": ["Combat", "Jump Shoes"],
    },
    Happy.gauntlet: {
        "Happy Completion": [],
    },
    Blank.ending: {
        "Open final gate": [],
    },
    Red_Cave.center: {
        "Center left tentacle hit": ["Combat"],
        "Center right tentacle hit": ["Combat"],
    },
    Red_Cave.left: {
        "Left tentacle hit": ["Combat", "Small Key (Red Cave):6"],
    },
    Red_Cave.right: {
        "Right tentacle hit": ["Combat", "Small Key (Red Cave):6"],
    },
    Red_Cave.top: {
        "Defeat Rogue": ["Combat"],
        "Grab Red Key": ["Defeat Rogue"]
    },
}

all_events = [event_name for events in events_by_region.values() for event_name in events.keys()]
