from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, StartInventoryPool, Toggle, Range, OptionSet
from .Data import Regions


class SmallKeyShuffle(Choice):
    """Select how the small keys will be handled."""
    display_name = "Shuffle small keys"
    option_vanilla = 0
    option_unlocked = 1
    option_original_dungeon = 2
    option_own_world = 3
    option_any_world = 4
    option_different_world = 5
    default = 2


class BigKeyShuffle(Choice):
    """Select how the big keys will be randomized."""
    display_name = "Include Big Keys"
    option_vanilla = 0
    option_unlocked = 1
    option_own_world = 3
    option_any_world = 4
    option_different_world = 5
    default = 0


class HealthCicadaShuffle(Choice):
    """Select how the health cicadas will be randomized."""
    display_name = "Include Health Cicadas"
    option_vanilla = 0
    option_own_world = 1
    option_any_world = 2
    option_different_world = 3
    default = 0


class RedCaveShuffle(Choice):
    """
    Select how progression through the Red Cave dungeon should be handled.
    [Progressive] Three Progressive Red Cave items will be added to the pool, and each will open the next section of the dungeon, in the following order: left, right, top.
    [Original Dungeon] Same as above, but the progression items will be restricted to the original dungeon.
    [Vanilla] The Red Cave will open up the same way it does in vanilla. The red tentacles will not be location checks.
    """
    display_name = "Red Cave Shuffle"
    option_progressive = 0
    option_original_dungeon = 1
    option_vanilla = 2
    default = 0


class SplitWindmill(Toggle):
    """
    Select how the Windmill behaves.
    [Off] The Windmill behaves as it does in vanilla. Turning it on moves the three statues blocking access to the lategame dungeons.
    [On] The Windmill doesn't do anything special, and instead becomes a location. Three items are added to the pool, one for each dungeon statue.
    """
    display_name = "Split Windmill"


class StartBroom(Choice):
    """Select which broom to start with."""
    display_name = "Starting Broom"
    option_none = 0
    option_normal = 1
    option_wide = 2
    option_long = 3
    option_swap = 4
    default = 0


class NexusGatesOpen(Choice):
    """Select which Nexus Gates are open from the start. Street is always open."""
    display_name = "Nexus Gates opened"
    option_street_only = 0
    option_street_and_fields = 1
    option_early = 2
    option_all = 3
    option_random_count = 4
    default = 1


class RandomNexusGateOpenCount(Range):
    """The amount of random Nexus Gates to be opened from the start. Only has an effect if Nexus Gates is set to
    random."""
    display_name = "Random Nexus Gates open count"
    range_start = 1
    range_end = len(Regions.regions_with_nexus_gate)
    default = 4


class CustomNexusGatesOpen(OptionSet):
    """
    Specify specific Nexus Gates to open from the start.
    If set, this will override the value of nexus_gates_open.
    Note that the Street Nexus Gate will always be open.
    """
    valid_keys = Regions.regions_with_nexus_gate


class VictoryCondition(Choice):
    """
    Select the end goal of your game.
    All Bosses: Defeat all bosses, ending with Briar.
    All Cards: Open the 49 card gate in the top section of the Nexus. Postgame must be enabled for this.
    """
    display_name = "Victory Condition"
    option_all_bosses = 0
    option_all_cards = 1
    default = 0


class EnablePostgame(Toggle):
    """
    If true, Swap will be usable outside of GO in specific areas near postgame content.
    If false, Swap is only used to access the top half of GO, and all postgame areas will be removed from logic.
    """
    display_name = "Enable Postgame"


class IncludeGreenCubeChest(Toggle):
    """Include the chest that forces you to wait almost 2 hours to access it."""
    display_name = "Include green cube chest"


@dataclass
class AnodyneGameOptions(PerGameCommonOptions):
    small_key_shuffle: SmallKeyShuffle
    health_cicada_shuffle: HealthCicadaShuffle
    big_key_shuffle: BigKeyShuffle
    red_cave_shuffle: RedCaveShuffle
    split_windmill: SplitWindmill
    start_broom: StartBroom
    nexus_gates_open: NexusGatesOpen
    random_nexus_gate_open_count: RandomNexusGateOpenCount
    custom_nexus_gates_open: CustomNexusGatesOpen
    victory_condition: VictoryCondition
    enable_postgame: EnablePostgame
    green_cube_chest: IncludeGreenCubeChest
    death_link: DeathLink
    start_inventory_from_pool: StartInventoryPool
