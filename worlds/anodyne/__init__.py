import logging

from BaseClasses import Region, Location, Item, ItemClassification, CollectionState
from Fill import fill_restrictive, FillError
from worlds.AutoWorld import WebWorld, World
from typing import List, Callable, Dict

from . import Constants

from .Data import Items, Locations, Regions, Exits, Events
from .Options import AnodyneGameOptions, IncludeGreenCubeChest, SmallKeyShuffle, StartBroom, \
    VictoryCondition, BigKeyShuffle, HealthCicadaShuffle, NexusGatesOpen, RedCaveShuffle


class AnodyneLocation(Location):
    game = "Anodyne"


class AnodyneItem(Item):
    game = "Anodyne"


class AnodyneWebWorld(WebWorld):
    theme = "dirt"


class AnodyneWorld(World):
    """
    Anodyne is a unique Zelda-like game, influenced by games such as Yume Nikki and Link's Awakening. 
    In Anodyne, you'll visit areas urban, natural, and bizarre, fighting your way through dungeons 
    and areas in Young's subconscious.
    """
    game = "Anodyne"  # name of the game/world
    options_dataclass = AnodyneGameOptions
    options: AnodyneGameOptions
    topology_present = False  # show path to required location checks in spoiler

    data_version = 1

    item_name_to_id = Constants.item_name_to_id
    location_name_to_id = Constants.location_name_to_id

    gates_unlocked: list[str] = []
    location_count: int = 0
    dungeon_items: Dict[str, List[Item]] = {}

    def generate_early(self):
        self.gates_unlocked.clear()
        self.location_count = 0
        self.dungeon_items.clear()

        nexus_gate_open = self.options.nexus_gates_open

        # Street is always unlocked
        if len(self.options.custom_nexus_gates_open.value) > 0:
            self.gates_unlocked.extend(self.options.custom_nexus_gates_open.value)
        elif nexus_gate_open == NexusGatesOpen.option_street_and_fields:
            self.gates_unlocked.append("Fields")
        elif nexus_gate_open == NexusGatesOpen.option_early:
            for region_name in Regions.early_nexus_gates:
                self.gates_unlocked.append(region_name)
        elif nexus_gate_open == NexusGatesOpen.option_all:
            for region_name in Regions.regions_with_nexus_gate:
                self.gates_unlocked.append(region_name)
        elif nexus_gate_open == NexusGatesOpen.option_random_count:
            random_nexus_gate_count = int(self.options.random_nexus_gate_open_count)

            if random_nexus_gate_count == Regions.regions_with_nexus_gate:
                for region_name in Regions.regions_with_nexus_gate:
                    self.gates_unlocked.append(region_name)
            else:
                unused_gates = Regions.regions_with_nexus_gate.copy()
                for _ in range(random_nexus_gate_count):
                    gate_index = self.random.randint(0, len(unused_gates) - 1)
                    gate_name = unused_gates[gate_index]

                    self.gates_unlocked.append(gate_name)
                    unused_gates.remove(gate_name)

    def create_item(self, name: str) -> Item:
        if name in Items.progression_items:
            item_class = ItemClassification.progression
        elif name in Items.useful_items:
            item_class = ItemClassification.useful
        elif name in Items.trap_items:
            item_class = ItemClassification.trap
        else:
            item_class = ItemClassification.filler

        return AnodyneItem(name, item_class, self.item_name_to_id.get(name, None), self.player)

    def create_regions(self) -> None:
        include_health_cicadas = self.options.health_cicada_shuffle
        include_big_keys = self.options.big_key_shuffle
        include_postgame = self.options.enable_postgame

        all_regions: Dict[str, Region] = {}

        for region_name in Regions.all_regions:
            if not include_postgame and region_name in Regions.postgame_regions:
                continue

            region = Region(region_name, self.player, self.multiworld)
            if region_name in Locations.locations_by_region:
                for location in Locations.locations_by_region[region_name]:
                    if include_health_cicadas == HealthCicadaShuffle.option_vanilla and location.health_cicada:
                        continue

                    if include_big_keys in [BigKeyShuffle.option_vanilla, BigKeyShuffle.option_unlocked]\
                            and location.big_key:
                        continue

                    if self.options.red_cave_shuffle == RedCaveShuffle.option_vanilla and location.tentacle:
                        continue

                    if not include_postgame and location.postgame():
                        continue

                    location_id = Constants.location_name_to_id[location.name]

                    new_location = AnodyneLocation(self.player, location.name, location_id, region)
                    new_location.access_rule = Constants.get_access_rule(location.reqs, region_name, self)
                    region.locations.append(new_location)

                    self.location_count += 1

            all_regions[region_name] = region

        for exit_vals in Exits.all_exits:
            exit1: str = exit_vals[0]
            exit2: str = exit_vals[1]

            if not include_postgame and (exit1 in Regions.postgame_regions or exit2 in Regions.postgame_regions):
                continue

            requirements: list[str] = exit_vals[2]

            r1 = all_regions[exit1]
            r2 = all_regions[exit2]

            e = r1.create_exit(f"{exit1} to {exit2} exit")
            e.connect(r2)
            e.access_rule = Constants.get_access_rule(requirements, exit1, self)

        for region_name in self.gates_unlocked:
            all_regions["Nexus bottom"].create_exit(f"{region_name} Nexus Gate").connect(all_regions[region_name])

        for region_name, events in Events.events_by_region.items():
            if not include_postgame and region_name in Regions.postgame_regions:
                continue

            for event_name in events:
                if include_big_keys != BigKeyShuffle.option_vanilla and event_name in Items.big_keys:
                    continue

                requirements: list[str] = Events.events_by_region[region_name][event_name]
                self.create_event(all_regions[region_name], event_name, Constants.get_access_rule(requirements,
                                                                                                  region_name, self))

        self.multiworld.regions += all_regions.values()

        # TODO: Debug-guard this.
        from Utils import visualize_regions

        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def set_rules(self) -> None:
        if self.options.enable_postgame and not self.options.green_cube_chest:
            # TODO: Probably just fully remove this location when the option is off.
            self.options.exclude_locations.value.add("Green cube chest")

        victory_condition: VictoryCondition = self.options.victory_condition
        requirements: list[str] = []

        if victory_condition == VictoryCondition.option_all_bosses:
            requirements.append("Defeat Seer")
            requirements.append("Defeat Rogue")
            requirements.append("Defeat The Wall")
            requirements.append("Defeat Manager")
            requirements.append("Defeat Servants")
            requirements.append("Defeat Watcher")
            requirements.append("Defeat Sage")
            requirements.append("Defeat Briar")
        elif victory_condition == VictoryCondition.option_all_cards:
            if not self.options.enable_postgame:
                raise Exception("Postgame must be enabled in order to use the All Cards victory condition.")

            requirements.append("Cards:49")
            requirements.append("Open 49 card gate")

        self.multiworld.completion_condition[self.player] = Constants.get_access_rule(requirements, "Event", self)

    def create_items(self) -> None:
        item_pool: List[Item] = []
        local_item_pool: set[str] = set()
        non_local_item_pool: set[str] = set()

        small_key_shuffle: SmallKeyShuffle = self.options.small_key_shuffle

        start_broom: StartBroom = self.options.start_broom
        start_broom_item: List[str] = []

        health_cicada_shuffle = self.options.health_cicada_shuffle
        big_key_shuffle = self.options.big_key_shuffle

        placed_items = 0

        excluded_items: set[str] = {
            *Items.small_key_item_count.keys(),
            *Items.big_keys,
            "Health Cicada",
            *Items.filler_items,
            *Items.trap_items,
            "Progressive Red Cave",
        }

        if small_key_shuffle == SmallKeyShuffle.option_vanilla:
            for location in Locations.all_locations:
                if location.small_key:
                    dungeon = Regions.dungeon_area_to_dungeon[location.region_name]
                    item_name = f"Small Key ({dungeon})"
                    self.multiworld.get_location(location.name, self.player).place_locked_item(
                        self.create_item(item_name))
                    placed_items += 1
        elif small_key_shuffle == SmallKeyShuffle.option_original_dungeon:
            for dungeon in Regions.dungeon_areas.keys():
                small_key_name = f"Small Key ({dungeon})"
                items = self.dungeon_items.setdefault(dungeon, [])

                for _ in range(Items.small_key_item_count[small_key_name]):
                    items.append(self.create_item(small_key_name))
                    placed_items += 1
        elif small_key_shuffle != SmallKeyShuffle.option_unlocked:
            for key_item, key_count in Items.small_key_item_count.items():
                placed_items += key_count

                for _ in range(key_count):
                    item_pool.append(self.create_item(key_item))

                if small_key_shuffle == SmallKeyShuffle.option_own_world:
                    local_item_pool.add(key_item)
                elif small_key_shuffle == SmallKeyShuffle.option_different_world:
                    non_local_item_pool.add(key_item)

        if start_broom == StartBroom.option_normal:
            start_broom_item = ["Broom"]
        elif start_broom == StartBroom.option_wide:
            start_broom_item = ["Broom", "Widen"]
        elif start_broom == StartBroom.option_long:
            start_broom_item = ["Broom", "Extend"]
        elif start_broom == StartBroom.option_swap:
            start_broom_item = ["Swap"]

        for broom_item in start_broom_item:
            self.multiworld.push_precollected(self.create_item(broom_item))
            excluded_items.add(broom_item)

        if health_cicada_shuffle != HealthCicadaShuffle.option_vanilla:
            health_cicada_amount = len([location for location in Locations.all_locations if location.health_cicada])
            placed_items += health_cicada_amount
            item_name = "Health Cicada"

            if health_cicada_shuffle == HealthCicadaShuffle.option_own_world:
                local_item_pool.add(item_name)
            elif health_cicada_shuffle == HealthCicadaShuffle.option_different_world:
                non_local_item_pool.add(item_name)

            for _ in range(health_cicada_amount):
                item_pool.append(self.create_item(item_name))

        if big_key_shuffle not in [BigKeyShuffle.option_vanilla, BigKeyShuffle.option_unlocked]:
            placed_items += len(Items.big_keys)

            for big_key in Items.big_keys:
                item_pool.append(self.create_item(big_key))

                if big_key_shuffle == BigKeyShuffle.option_own_world:
                    local_item_pool.add(big_key)
                elif big_key_shuffle == BigKeyShuffle.option_different_world:
                    non_local_item_pool.add(big_key)

        if self.options.red_cave_shuffle != RedCaveShuffle.option_vanilla:
            placed_items += 3

            pool: List[Item] = item_pool
            if self.options.red_cave_shuffle == RedCaveShuffle.option_original_dungeon:
                pool = self.dungeon_items.setdefault("Red Cave", [])

            for _ in range(3):
                pool.append(self.create_item("Progressive Red Cave"))

        if not self.options.enable_postgame:
            excluded_items.update(Items.postgame_cards)

        for name in Items.all_items:
            if name not in excluded_items:
                placed_items += 1
                item_pool.append(self.create_item(name))

        if placed_items < self.location_count:
            # TODO: Prioritize extending the item pool using available secret items (just the golden poop and heart when
            # postgame is disabled, and all of them if enabled). After that, if there's any space left, fill it with
            # some other generic filler item.
            item_pool.extend(self.create_filler() for _ in range(self.location_count - placed_items))

        self.multiworld.itempool += item_pool

        self.options.local_items.value |= local_item_pool
        self.options.non_local_items.value |= non_local_item_pool

    def get_filler_item_name(self) -> str:
        # TODO: See TODO in create_items.
        return self.random.choice(Items.filler_items)

    def create_event(self, region: Region, event_name: str, access_rule: Callable[[CollectionState], bool]) -> None:
        loc = AnodyneLocation(self.player, event_name, None, region)
        loc.place_locked_item(self.create_event_item(event_name))
        loc.access_rule = access_rule
        region.locations.append(loc)

    def create_event_item(self, name: str) -> Item:
        item = self.create_item(name)
        item.classification = ItemClassification.progression
        return item

    def pre_fill(self):
        for dungeon, confined_dungeon_items in self.dungeon_items.items():
            if len(confined_dungeon_items) == 0:
                continue

            collection_state = self.multiworld.get_all_state(False)
            for other_dungeon, other_dungeon_items in self.dungeon_items.items():
                if other_dungeon == dungeon:
                    continue

                for other_dungeon_item in other_dungeon_items:
                    collection_state.collect(other_dungeon_item)

            dungeon_location_names = [location.name
                                      for region_name in Regions.dungeon_areas[dungeon]
                                      for location in Locations.locations_by_region.get(region_name, [])]

            if dungeon == "Street" and self.options.small_key_shuffle == SmallKeyShuffle.option_original_dungeon and\
                    self.options.nexus_gates_open == NexusGatesOpen.option_street_only and\
                    self.options.start_broom == StartBroom.option_none:
                # This is a degenerate case; we need to prevent pre-fill from putting the Street small key in the Broom
                # chest because if it does, there are no reachable locations at the start of the game.
                dungeon_location_names.remove("Street - Broom Chest")

            dungeon_locations = [location for location in self.multiworld.get_locations(self.player)
                                 if location.name in dungeon_location_names]

            for attempts_remaining in range(2, -1, -1):
                self.random.shuffle(dungeon_locations)
                try:
                    fill_restrictive(self.multiworld, collection_state, dungeon_locations, confined_dungeon_items,
                                     single_player_placement=True, lock=True, allow_excluded=True)
                    break
                except FillError as exc:
                    if attempts_remaining == 0:
                        raise exc
                    logging.debug(f"Failed to shuffle dungeon items for player {self.player}. Retrying...")

    def fill_slot_data(self):
        return {
            "death_link": bool(self.options.death_link.value),
            "unlock_gates": self.options.small_key_shuffle == SmallKeyShuffle.option_unlocked,
            "unlock_big_gates": self.options.big_key_shuffle == BigKeyShuffle.option_unlocked,
            "nexus_gates_unlocked": self.gates_unlocked,
            "vanilla_red_cave": self.options.red_cave_shuffle == RedCaveShuffle.option_vanilla,
        }
