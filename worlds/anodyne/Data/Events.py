events_by_region = {
    "Bedroom exit": {
        "Defeat Seer": ["Broom"],
        "Green Key": []
    },
    "Crowd floor 1": {
        "Defeat The Wall": ["Broom", "Jump Shoes"],
        "Blue Key": ["Defeat The Wall"]
    },
    "Windmill": {
        "Windmill activated": [],
    },
    "Hotel floor 1": {
        "Defeat Manager": ["Keys:Hotel:6", "Broom"],
    },
    "Circus": {
        "Defeat Servants": ["Keys:Circus:3", "Broom", "Jump Shoes"],
    },
    "Apartment floor 3": {
        "Defeat Watcher": ["Broom", "Keys:Apartment:4"],
    },
    "Terminal": {
        "Defeat Sage": ["Broom", "Cards:36"],
    },
    "Go top": {
        "Defeat Briar": ["Happy completed", "Briar access"],
    },
    "Nexus top": {
        "Open 49 card gate": ["Cards:49"],
    },
    "Red Cave center": {
        "Center left tentacle hit": ["Broom"],
        "Center right tentacle hit": ["Broom"],
    },
    "Red Cave left": {
        "Left tentacle hit": ["Broom", "Keys:Red Cave:6"],
    },
    "Red Cave right": {
        "Right tentacle hit": ["Broom", "Keys:Red Cave:6"],
    },
    "Red Cave top": {
        "Defeat Rogue": ["Broom"],
        "Red Key": ["Defeat Rogue"]
    },
    "Blue": {
        "Blue completed": ["Jump Shoes"],
    },
    "Happy": {
        "Happy completed": ["Blue completed"],
    },
}

all_events = [event_name for events in events_by_region.values() for event_name in events.keys()]
