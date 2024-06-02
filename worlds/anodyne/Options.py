from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, StartInventoryPool, Toggle, Range, OptionSet
from .Data import Regions


class SmallKeyShuffle(Choice):
    """
    Select how the small keys will be handled.
    [Vanilla] The small keys will be placed in the vanilla locations.
    [Unlocked] The key-locked gates in each dungeon will open automatically.
    [Original Dungeon] The small keys will be shuffled within their own dungeons.
    [Own World] The small keys will be shuffled within your own world.
    [Any World] The small keys will be shuffled throughout the entire multiworld.
    [Different World] The small keys will specifically be shuffled into other players' worlds.
    """
    display_name = "Shuffle Small Keys"
    option_vanilla = 0
    option_unlocked = 1
    option_original_dungeon = 2
    option_own_world = 3
    option_any_world = 4
    option_different_world = 5
    default = 2


class BigKeyShuffle(Choice):
    """
    Select how the big keys will be randomized.
    [Vanilla] The big keys will be placed in the vanilla locations.
    [Unlocked] The big key gates will open automatically.
    [Own World] The big keys will be shuffled within your own world.
    [Any World] The big keys will be shuffled throughout the entire multiworld.
    [Different World] The big keys will specifically be shuffled into other players' worlds.
    """
    display_name = "Shuffle Big Keys"
    option_vanilla = 0
    option_unlocked = 1
    option_own_world = 3
    option_any_world = 4
    option_different_world = 5
    default = 4


class HealthCicadaShuffle(Choice):
    """
    Select how the health cicadas will be randomized.
    [Vanilla] The health cicadas will not be locations.
    [Own World] Health cicadas will be locations, and the items will be shuffled within your world.
    [Any World] The health cicadas will be shuffled throughout the entire multiworld.
    [Different World] The health cicadas will specifically be shuffled into other players' worlds.
    """
    display_name = "Shuffle Health Cicadas"
    option_vanilla = 0
    option_own_world = 1
    option_any_world = 2
    option_different_world = 3
    default = 2


class RedCaveAccess(Choice):
    """
    Select how progression through the Red Cave dungeon should be handled.
    [Progressive] Three Progressive Red Cave items will be added to the pool, and each will open the next section of the dungeon, in the following order: left, right, top.
    [Original Dungeon] Same as above, but the progression items will be restricted to the original dungeon.
    [Vanilla] The Red Cave will open up the same way it does in vanilla. The red tentacles will not be location checks.
    """
    display_name = "Red Cave Access"
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
    """
    Select which Nexus Gates are open from the start. Street is always open.
    [Street Only] Only the Street gate is open.
    [Street and Fields] The Street and Fields gates are open.
    [Early] The gates for pre-dungeon areas near Fields are also open.
    [Random Count] A number of random gates will be open. The number is specified in another option.
    [Random Pre-Endgame] Same as above, but the GO, Blue, and Happy gates are excluded.
    """
    display_name = "Open Nexus Gates"
    option_street_only = 0
    option_street_and_fields = 1
    option_early = 2
    option_all = 3
    option_random_count = 4
    option_random_pre_endgame = 5
    default = 1


class RandomNexusGateOpenCount(Range):
    """
    The amount of random Nexus Gates to be opened from the start. Only has an effect if Nexus Gates is set to random.
    """
    display_name = "Random Open Nexus Gates Count"
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
    [Defeat Briar] Reach the credits screen after defeating the Briar.
    [All Cards] Open the 49 card gate in the top section of the Nexus. Postgame must be enabled for this.
    """
    display_name = "Victory Condition"
    option_defeat_briar = 0
    option_all_cards = 1
    default = 0


class PostgameMode(Choice):
    """
    Determines how the Swap upgrade behaves.
    Note that even when "Expanded Swap" is available, Swap will not work in almost every room the way it does in the base game. It will be limited to rooms near postgame content, so that you can reach those checks/areas without breaking the rest of the game's logic.
    [Disabled] Swap is only used to access the top half of GO, and all postgame areas will be removed from logic.
    [Vanilla] Expanded Swap unlocks upon defeating Briar.
    [Unlocked] Expanded Swap is automatically available upon receiving the Swap item.
    [Progressive] The first Progressive Swap will behave like pre-Briar Swap, and the second is the Expanded Swap.
    """
    display_name = "Postgame Mode"
    option_disabled = 0
    option_vanilla = 1
    option_unlocked = 2
    option_progressive = 3
    default = 0


class IncludeForestBunnyChest(Toggle):
    """Include the chest that forces you to wait almost 2 hours to access it."""
    display_name = "Include Forest Bunny Chest"


@dataclass
class AnodyneGameOptions(PerGameCommonOptions):
    small_key_shuffle: SmallKeyShuffle
    health_cicada_shuffle: HealthCicadaShuffle
    big_key_shuffle: BigKeyShuffle
    red_cave_access: RedCaveAccess
    split_windmill: SplitWindmill
    start_broom: StartBroom
    nexus_gates_open: NexusGatesOpen
    random_nexus_gate_open_count: RandomNexusGateOpenCount
    custom_nexus_gates_open: CustomNexusGatesOpen
    victory_condition: VictoryCondition
    postgame_mode: PostgameMode
    forest_bunny_chest: IncludeForestBunnyChest
    death_link: DeathLink
    start_inventory_from_pool: StartInventoryPool
