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

class RegionEnum(Enum):
    def __init_subclass__(cls, **kwargs):
        all_areas.append(cls)

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return "" if name == "DEFAULT" else name.replace('_',' ')

    @classmethod
    def area_name(cls):
        name = cls.__name__.replace('_', ' ')
        return area_name_trans.setdefault(name, name)

    def __str__(self):
        return self.area_name()+(' ' + self.value).rstrip()

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
    past_gate = auto()

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
    past_gate = auto()

class Terminal(RegionEnum):
    DEFAULT = auto()
    top = auto()

class Windmill(RegionEnum):
    DEFAULT = auto()
    entrance = auto()


early_nexus_gates = [
    Beach,
    Cliff,
    Fields,
    Forest,
    Overworld,
    Red_Sea
]

endgame_nexus_gates = [
    Blue,
    Go,
    Happy,
]

post_temple_boss_nexus_gates:list[type[RegionEnum]] = [
    Bedroom,
    Suburb,
    Apartment
]

wrong_big_key_early_locked_nexus_gates = [
    Apartment,
    Bedroom,
    Suburb
]

postgame_regions:list[RegionEnum] = [
    Bedroom.drawer,
    *Drawer,
    *Blank,
    *Debug,
    *Boss_Rush,
    Nexus.top,
    Space.Gauntlet
]

postgame_without_secret_paths:list[RegionEnum] = [
    Fields.North_Secret_Area
]

