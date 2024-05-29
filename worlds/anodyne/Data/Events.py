events_by_region = {
    "Bedroom": {
        "Defeat Seer": ["Broom", "Keys:2"],
        "Green Key": ["Defeat Seer"]
    },
    "Crowd floor 1": {
        "Defeat The Wall": ["Broom", "Jump Shoes", "Break the Film"],
        "Blue Key": ["Defeat The Wall"]
    },
    "Crowd floor 3": {
        "Break the Film": ["Broom", "Keys:3"],
    },
    "Fields": {
        "Goldman moved": [],
    },
    "Windmill": {
        "Windmill activated": ["Green Key", "Red Key", "Blue Key"],
    },
    "Hotel floor 1": {
        "Defeat Manager": ["Keys:6", "Broom"],
    },
    "Circus": {
        "Defeat Servants": ["Keys:3", "Broom", "Jump Shoes"],
    },
    "Apartment floor 3": {
        "Defeat Watcher": ["Broom", "Keys:4"],
    },
    "Terminal": {
        "Defeat Sage": ["Broom", "Cards:36"],
    },
    "Go top": {
        "Defeat Briar": ["Happy completed"],
    },
    "Nexus top": {
        "Open 49 card gate": ["Cards:49"],
    },
    "Red Cave center": {
        "Center left tentacle hit": ["Broom"],
        "Center right tentacle hit": ["Broom"],
    },
    "Red Cave left": {
        "Left tentacle hit": ["Broom", "Keys:6"],
    },
    "Red Cave right": {
        "Right tentacle hit": ["Broom", "Keys:6"],
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
