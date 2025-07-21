from enum import Enum, auto

area_name_trans = {
    "Overworld": "Woods",
    "Bedroom": "Temple of the Seeing One",
    "Red Cave": "Red Grotto",
    "Crowd": "Mountain Cavern",
    "Forest": "Deep Forest",
    "Suburb": "Young Town",
    "Terminal": "Crossing",
    "Happy": "Red",
    "Go": "Garden"
}

all_areas:list[type['RegionEnum']] = []

class RegionEnum(str,Enum):
    def __init_subclass__(cls, **kwargs):
        all_areas.append(cls)

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return "" if name == "DEFAULT" else name.replace('_',' ')

    def __str__(self):
        name = self.__class__.__name__.replace('_',' ')
        return area_name_trans.setdefault(name,name)+(' ' + self.value).rstrip()

class Apartment(RegionEnum):
    floor_1 = auto()
    floor_1_top_left = auto()
    floor_2 = auto()
    floor_2_top_left = auto()
    floor_3 = auto()

class Beach(RegionEnum):
    DEFAULT = auto()
    gauntlet = auto()

class Bedroom(RegionEnum):
    entrance = auto()
    core = auto()
    shieldy_room = auto()
    after_statue = auto()
    exit = auto()
    drawer = auto()

class Blank(RegionEnum):
    windmill = auto()
    ending = auto()

class Blue(RegionEnum):
    DEFAULT = auto()

class Circus(RegionEnum):
    DEFAULT = auto()
    entrance_lake = auto()
    entry_gauntlets = auto()
    past_entrance_lake = auto()
    circlejump_gauntlets = auto()
    third_key_gauntlet = auto()
    boss_gauntlet = auto()
    north_gauntlet = auto()

class Crowd(RegionEnum):
    floor_1 = auto()
    floor_2 = auto()
    floor_2_gauntlets = auto()
    floor_3 = auto()
    floor_3_center = auto()
    jump_challenge = auto()
    exit = auto()

class Boss_Rush(RegionEnum):
    DEFAULT = auto()

class Cell(RegionEnum):
    DEFAULT = auto()

class Cliff(RegionEnum):
    DEFAULT = auto()
    post_windmill = auto()

class Debug(RegionEnum):
    DEFAULT = auto()

class Drawer(RegionEnum):
    DEFAULT = auto()
    dark = auto()

class Fields(RegionEnum):
    DEFAULT = auto()
    Lake = auto()
    Past_Gate = auto()
    North_Secret_Area = auto()
    Goldman = "Goldman's Cave"
    East = auto()

class Forest(RegionEnum):
    DEFAULT = auto()

class Go(RegionEnum):
    bottom = auto()
    top = auto()

class Happy(RegionEnum):
    DEFAULT = auto()
    gauntlet = auto()

class Hotel(RegionEnum):
    roof = auto()
    floor_4 = auto()
    floor_3 = auto()
    floor_2 = auto()
    floor_2_right = auto()
    floor_1 = auto()

class Nexus(RegionEnum):
    bottom = auto()
    top = auto()

class Overworld(RegionEnum):
    DEFAULT = auto()
    west = auto()
    Gauntlet = auto()
    post_windmill = auto()

class Red_Cave(RegionEnum):
    top = auto()
    left = auto()
    center = auto()
    right = auto()
    bottom = auto()
    exit = auto()
    Isaac = auto()

class Red_Sea(RegionEnum):
    DEFAULT = auto()

class Space(RegionEnum):
    DEFAULT = auto()
    Gauntlet = auto()

class Street(RegionEnum):
    DEFAULT = auto()

class Suburb(RegionEnum):
    DEFAULT = auto()
    card_house = auto()

class Terminal(RegionEnum):
    DEFAULT = auto()
    top = auto()

class Windmill(RegionEnum):
    DEFAULT = auto()
    entrance = auto()

dungeon_areas = {
    "Temple of the Seeing One": ["Bedroom entrance",
                                 "Bedroom core",
                                 "Bedroom shieldy room",
                                 "Bedroom after statue",
                                 "Bedroom exit"],
    "Red Cave": ["Red Cave top",
                 "Red Cave left",
                 "Red Cave center",
                 "Red Cave right",
                 "Red Cave bottom",
                 "Red Cave exit",
                 "Red Cave Isaac"],
    "Mountain Cavern": ["Crowd floor 1",
                        "Crowd floor 2",
                        "Crowd floor 2 gauntlets",
                        "Crowd floor 3",
                        "Crowd floor 3 center",
                        "Crowd jump challenge",
                        "Crowd exit"],
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
    "Circus":  ["Circus",
                "Circus entrance lake",
                "Circus entry gauntlets",
                "Circus past entrance lake",
                "Circus circlejump gauntlets",
                "Circus third key gauntlet",
                "Circus boss gauntlet",
                "Circus north gauntlet"],
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
    "Crowd exit",
    "Fields",
    "Forest",
    "Go bottom",
    "Happy",
    "Hotel floor 4",
    "Overworld",
    "Red Cave exit",
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

wrong_big_key_early_locked_nexus_gates = [
    "Apartment floor 1",
    "Bedroom exit",
    "Suburb"
]

postgame_regions:list[RegionEnum] = [
    Bedroom.drawer,
    *Blank,
    *Debug,
    *Boss_Rush,
    Nexus.top,
    Space.Gauntlet
]

postgame_without_secret_paths:list[RegionEnum] = [
    Fields.North_Secret_Area
]

post_temple_boss_nexus_gates:list[type[RegionEnum]] = [
    Bedroom,
    Suburb,
    Apartment
]
