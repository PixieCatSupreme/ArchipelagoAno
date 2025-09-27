from typing import NamedTuple, Callable

from ..Options import AnodyneGameOptions, BigKeyShuffle, VictoryCondition, RedCaveAccess
from .Regions import Bedroom, Crowd, Windmill, Hotel, Circus, Apartment, Terminal, Go, Blue, \
    Happy, Red_Cave, RegionEnum, Nexus

def big_keys_vanilla(options:AnodyneGameOptions):
    return options.big_key_shuffle == BigKeyShuffle.option_vanilla

def windmill_vanilla(options:AnodyneGameOptions):
    return options.split_windmill.value == False

def blue_happy_vanilla(options:AnodyneGameOptions):
    return options.include_blue_happy.value == False

def final_gate_ending(options:AnodyneGameOptions):
    return options.victory_condition == VictoryCondition.option_final_gate

def tentacles_vanilla(options:AnodyneGameOptions):
    return options.red_grotto_access == RedCaveAccess.option_vanilla

class EventData(NamedTuple):
    region: RegionEnum
    name: str
    reqs: list[str]
    tracker_loc: tuple[int,int]
    is_active: Callable[[AnodyneGameOptions],bool] = lambda _: True

all_events: list[EventData] = [
    EventData(Bedroom.exit, "Defeat Seer",["Combat"],(392,59)),
    EventData(Bedroom.exit, "Grab Green Key",[],(600,104),big_keys_vanilla),
    EventData(Crowd.floor_1, "Defeat The Wall", ["Combat", "Jump Shoes"], (1519, 984)),
    EventData(Crowd.exit, "Grab Blue Key",[],(1544, 872),big_keys_vanilla),
    EventData(Windmill.DEFAULT, "Windmill activated",[],(216, 376), windmill_vanilla),
    EventData(Hotel.floor_1, "Defeat Manager", ["Small Key (Hotel):6", "Combat"], (1356, 1661)),
    EventData(Circus.boss_gauntlet, "Defeat Servants", ["Combat", "Jump Shoes"],(734, 184)),
    EventData(Apartment.floor_3, "Defeat Watcher", ["Combat", "Small Key (Apartment):4"], (1196, 993)),
    EventData(Terminal.top, "Defeat Sage", ["Combat", "Jump Shoes"], (400, 522)),
    EventData(Go.top, "Defeat Briar", ["Combat", "Complete Blue", "Complete Happy"],(400,240)),
    EventData(Blue.DEFAULT, "Blue Completion", ["Combat","Jump Shoes"],(5*16,2*16),blue_happy_vanilla),
    EventData(Happy.gauntlet, "Happy Completion", [],(41*16,11*16),blue_happy_vanilla),
    EventData(Nexus.ending, "Open final gate", [], (400,32), final_gate_ending),
    EventData(Red_Cave.center,"Center left tentacle hit",["Combat"],(232, 216), tentacles_vanilla),
    EventData(Red_Cave.center,"Center right tentacle hit",["Combat"],(840, 200), tentacles_vanilla),
    EventData(Red_Cave.left,"Left tentacle hit",["Combat", "Small Key (Red Grotto):6"],(200, 664), tentacles_vanilla),
    EventData(Red_Cave.right,"Right tentacle hit",["Combat", "Small Key (Red Grotto):6"],(872, 680), tentacles_vanilla),
    EventData(Red_Cave.top, "Defeat Rogue", ["Combat"],(1056, 80)),
    EventData(Red_Cave.exit, "Grab Red Key", [], (1096, 296),big_keys_vanilla)
]

all_event_names = {event.name for event in all_events}
