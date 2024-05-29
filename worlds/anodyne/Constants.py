import logging

from typing import Callable, NamedTuple
from BaseClasses import MultiWorld, CollectionState

from .Data import Items, Locations, Regions, Events
from .Options import KeyShuffle

id_offset: int = 20130204


class AnodyneExitConnection(NamedTuple):
    region1: str
    region2: str
    access_rule: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


class AnodyneExitInfo(NamedTuple):
    connections: list[AnodyneExitConnection]
    access_rule: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_name_to_id = {name: id for id, name in enumerate(Items.all_items, id_offset)}
location_name_to_id = {name: id for id, name in enumerate(Locations.all_locations, id_offset)}


def count_cards(state: CollectionState, player: int) -> int:
    card_count = 0
    for card in Items.cards:
        if state.has(card, player):
            card_count += 1

    return card_count


def count_keys(state: CollectionState, player: int, map_name: str) -> int:
    key_name: str = f"Small Key ({map_name})"

    if key_name not in Items.all_items:
        logging.warning(f"Item {key_name} does not exist")
        return 0
    else:
        return state.count(key_name, player)


def check_access(state: CollectionState, player: int, rule: str, map_name: str) -> bool:
    if rule.startswith("Cards:"):
        count = int(rule[6:])
        logging.debug(f"Card {count} check in {map_name} ({player})")
        return count >= count_cards(state, player)
    elif rule.startswith("Keys:"):
        if state.multiworld.worlds[player].options.key_shuffle == KeyShuffle.option_unlocked:
            logging.debug(f"Gates are unlocked ({player})")
            return True

        count = int(rule[5:])
        map_name = Regions.dungeon_area_to_dungeon.get(map_name, map_name)
        logging.debug(f"Key {count} check in {map_name} having {count_keys(state,player,map_name)} ({player})")
        return count_keys(state, player, map_name) >= count
    else:
        logging.debug(f"Item {rule} check in {map_name} ({player})")
        if rule not in Items.all_items and rule not in Events.all_events:
            logging.warning(f"Rule {rule} does not exist")
        return state.has(item=rule, player=player)
