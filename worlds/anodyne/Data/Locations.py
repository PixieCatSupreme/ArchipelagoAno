from enum import Enum, auto
from typing import NamedTuple, List, Dict

from ..Options import CellGate, SuburbGate
from .Regions import Apartment, Beach, Bedroom, Blank, Cell, Circus, Debug, Boss_Rush, Street, Space, Red_Cave, Drawer, \
    Cliff, Crowd, Fields, Terminal, Forest, Happy, Red_Sea, Overworld, Blue, Go, Hotel, Nexus, Suburb, Windmill, \
    RegionEnum, postgame_regions, postgame_without_secret_paths


class LocationType(Enum):
    Regular = auto()
    Cicada = auto()
    Key = auto()
    BigKey = auto()
    Tentacle = auto()
    Dust = auto()
    Nexus = auto()

class LocationData(NamedTuple):
    _name: str
    region: RegionEnum
    reqs: List[str] = []
    type:LocationType = LocationType.Regular

    @property
    def name(self):
        if ' - ' in self._name:
            return self._name
        return f"{self.region.area_name()} - {self._name}"

    @property
    def small_key(self):
        return self.type == LocationType.Key

    @property
    def big_key(self):
        return self.type == LocationType.BigKey

    @property
    def health_cicada(self):
        return self.type == LocationType.Cicada

    @property
    def dust(self):
        return self.type == LocationType.Dust

    @property
    def tentacle(self):
        return self.type == LocationType.Tentacle

    @property
    def nexus_gate(self):
        return self.type == LocationType.Nexus

    def postgame(self,secret_paths:bool):
        return ("SwapOrSecret" in self.reqs and not secret_paths) or "Progressive Swap:2" in self.reqs or self.region in postgame_regions or (not secret_paths and self.region in postgame_without_secret_paths)


# This array must maintain a consistent order because the IDs are generated from it.
all_locations: List[LocationData] = [
    # 0AC41F72-EE1D-0D32-8F5D-8F25796B6396
    LocationData("Apartment - 1F Ledge Chest", Apartment.floor_1, ["Combat"], type=LocationType.Key),
    # DE415E2A-06EE-83AC-F1A3-5DCA1FA44735
    LocationData("Apartment - 1F Rat Maze Chest", Apartment.floor_1, ["Combat"], type=LocationType.Key),
    LocationData("Apartment - 1F Exterior Chest", Apartment.floor_1, ["Combat", "Jump Shoes"]),
    LocationData("Apartment - 1F Couches Chest", Apartment.floor_1_top_left, ["Combat", "Jump Shoes"]),
    # 5B55A264-3FCD-CF38-175C-141B2D093029
    LocationData("Apartment - 2F Rat Maze Chest", Apartment.floor_2, ["Combat", "Jump Shoes"], type=LocationType.Key),
    # 2BBF01C8-8267-7E71-5BD4-325001DBC0BA
    LocationData("Apartment - 3F Gauntlet Chest", Apartment.floor_3, ["Combat"], type=LocationType.Key),
    LocationData("Apartment - Boss Chest", Apartment.floor_3, ["Defeat Watcher"]),
    LocationData("Beach - Dock Chest", Beach.DEFAULT),
    LocationData("Beach - Secret Chest", Beach.gauntlet, ["Progressive Swap:2"]),
    LocationData("Beach - Out-of-bounds Chest", Beach.DEFAULT, ["Progressive Swap:2"]),
    # 40DE36CF-9238-F8B0-7A57-C6C8CA465CC2
    LocationData("Temple of the Seeing One - Entrance Chest", Bedroom.entrance, type=LocationType.Key),
    LocationData("Temple of the Seeing One - Shieldy Room Chest", Bedroom.shieldy_room, []),
    LocationData("Temple of the Seeing One - Rock-Surrounded Chest", Bedroom.core, []),
    LocationData("Temple of the Seeing One - Boss Chest", Bedroom.exit, []),
    # D41F2750-E3C7-BBB4-D650-FAFC190EBD32
    LocationData("Temple of the Seeing One - After Statue Left Chest", Bedroom.after_statue, [], type=LocationType.Key),
    LocationData("Temple of the Seeing One - After Statue Right Chest", Bedroom.after_statue, []),
    # 401939A4-41BA-E07E-3BA2-DC22513DCC5C
    LocationData("Temple of the Seeing One - Dark Room Chest", Bedroom.core, [], type=LocationType.Key),
    LocationData("Blank - Card Chest", Blank.windmill),
    LocationData("Cell - Top Left Chest", Cell.DEFAULT, ["Jump Shoes"]),
    LocationData("Cell - Chaser Gauntlet Chest", Cell.DEFAULT, ["Progressive Swap:2", "Combat", "Jump Shoes"]),
    # 75C2D434-4AE8-BCD0-DBEB-8E6CDA67BF45
    LocationData("Circus - Rat Maze Chest", Circus.entry_gauntlets, [], type=LocationType.Key),
    LocationData("Circus - Clowns Chest", Circus.entry_gauntlets, []),
    LocationData("Circus - Fire Pillar Chest", Circus.circlejump_gauntlets, []),
    # 69E8FBD6-2DA3-D25E-446F-6A59AC3E9FC2
    LocationData("Circus - Arthur Chest", Circus.entry_gauntlets, [], type=LocationType.Key),
    # 6A95EB2F-75FD-8649-5E07-3ED37C69A9FB
    LocationData("Circus - Javiera Chest", Circus.circlejump_gauntlets, [], type=LocationType.Key),
    # A2479A02-9B0D-751F-71A4-DB15C4982DF5
    LocationData("Circus - Lion Chest", Circus.third_key_gauntlet, [], type=LocationType.Key),
    LocationData("Circus - Double Clowns Chest", Circus.north_gauntlet, []),
    LocationData("Circus - Boss Chest", Circus.boss_gauntlet, ["Defeat Servants"]),
    LocationData("Cliffs - Upper Chest", Cliff.post_windmill),
    LocationData("Cliffs - Lower Chest", Cliff.post_windmill),
    LocationData("Mountain Cavern - 2F Crowded Ledge Chest", Crowd.floor_2_gauntlets,
                 ["Small Key (Mountain Cavern):4"]),
    # BE2FB96B-1D5F-FCD1-3F58-D158DB982C21
    LocationData("Mountain Cavern - 2F Four Enemies Chest", Crowd.floor_2, ["Combat"], type=LocationType.Key),
    # 5743A883-D209-2518-70D7-869D14925B77
    LocationData("Mountain Cavern - 2F Entrance Chest", Crowd.floor_2_gauntlets, type=LocationType.Key),
    # 21EE2D01-54FB-F145-9464-4C2CC8725EB3
    LocationData("Mountain Cavern - 2F Frogs and Dog Chest", Crowd.floor_2_gauntlets, type=LocationType.Key),
    LocationData("Mountain Cavern - 3F Roller Chest", Crowd.floor_3_center, []),
    LocationData("Mountain Cavern - Boss Chest", Crowd.exit, []),
    LocationData("Mountain Cavern - Extend Upgrade Chest", Crowd.jump_challenge, ["Combat", "Jump Shoes"]),
    # 868736EF-EC8B-74C9-ACAB-B7BC56A44394
    LocationData("Mountain Cavern - 2F Frogs and Rotators Chest", Crowd.floor_2_gauntlets, type=LocationType.Key),
    LocationData("Debug - River Puzzles Chest", Debug.DEFAULT, ["Combat", "Jump Shoes"]),
    LocationData("Debug - Upper Prison Chest", Debug.DEFAULT),
    LocationData("Debug - Lower Prison Chest", Debug.DEFAULT),
    LocationData("Debug - Jumping Chest", Debug.DEFAULT),
    LocationData("Debug - Maze Chest", Debug.DEFAULT, ["Jump Shoes"]),
    LocationData("Drawer - Game Over Chest", Drawer.DEFAULT, ["Progressive Swap:2"]),
    LocationData("Drawer - Brown Area Chest", Drawer.DEFAULT),
    LocationData("Fields - Island Chest", Fields.Lake, ["Combat", "Jump Shoes"]),
    LocationData("Fields - Gauntlet Chest", Fields.Lake, ["Combat", "Jump Shoes"]),
    # Cleaning up his cave
    LocationData("Fields - Goldman's Cave Chest", Fields.Goldman, ["Combat"]),
    LocationData("Fields - Blocked River Chest", Fields.DEFAULT, ["Progressive Swap:2", "Jump Shoes"]),
    LocationData("Fields - Cardboard Box", Fields.DEFAULT, ["Miao"]),
    LocationData("Fields - Shopkeeper Trade", Fields.DEFAULT, ["Cardboard Box"]),
    LocationData("Fields - Mitra Trade", Fields.DEFAULT, ["Biking Shoes"]),
    # Hidden path
    LocationData("Fields - Near Overworld Secret Chest", Fields.North_Secret_Area),
    # Hidden path
    LocationData("Fields - Secluded Glen Chest", Fields.DEFAULT, ["SwapOrSecret"]),
    # Hidden path
    # Logically, this is in Terminal, because it is separated from the rest of Fields in the same way Terminal is.
    LocationData("Fields - Near Terminal Secret Chest", Terminal.DEFAULT, ["SwapOrSecret"]),
    LocationData("Deep Forest - Inlet Chest", Forest.DEFAULT, ["Combat"]),
    # This is the one that takes 2 hours
    LocationData("Deep Forest - Bunny Chest", Forest.DEFAULT, ["Progressive Swap:2"]),
    LocationData("GO - Swap Upgrade Chest", Go.bottom),
    LocationData("GO - Secret Color Puzzle Chest", Go.bottom, ["Progressive Swap:2"]),
    # 6C8870D4-7600-6FFD-B425-2D951E65E160
    LocationData("Hotel - 4F Annoyers Chest", Hotel.floor_4, ["Combat", "Jump Shoes"], type=LocationType.Key),
    LocationData("Hotel - 4F Dust Blower Maze Chest", Hotel.floor_4, ["Combat", "Jump Shoes", "Small Key (Hotel):1"]),
    LocationData("Hotel - 3F Dashers Chest", Hotel.floor_3, ["Small Key (Hotel):6"]),
    # 64EE884F-EA96-FB09-8A9E-F75ABDB6DC0D
    LocationData("Hotel - 3F Gasguy Chest", Hotel.floor_3, ["Combat"], type=LocationType.Key),
    # 075E6024-FE2D-9C4A-1D2B-D627655FD31A
    LocationData("Hotel - 3F Rotators Chest", Hotel.floor_3, ["Combat"], type=LocationType.Key),
    LocationData("Hotel - 2F Dog Chest", Hotel.floor_2_right, ["Combat"]),
    # 1990B3A2-DBF8-85DA-C372-ADAFAA75744C
    LocationData("Hotel - 2F Crevice Right Chest", Hotel.floor_2_right, type=LocationType.Key),
    # D2392D8D-0633-2640-09FA-4B921720BFC4
    LocationData("Hotel - 2F Backrooms Chest", Hotel.floor_2, ["Combat"], type=LocationType.Key),
    # 019CBC29-3614-9302-6848-DDAEDC7C49E5
    LocationData("Hotel - 1F Burst Flowers Chest", Hotel.floor_1, type=LocationType.Key),
    # 9D6FDA36-0CC6-BACC-3844-AEFB6C5C6290
    LocationData("Hotel - 2F Crevice Left Chest", Hotel.floor_2, ["Jump Shoes"], type=LocationType.Key),
    LocationData("Hotel - Boss Chest", Hotel.floor_1, ["Defeat Manager"]),
    LocationData("Hotel - Roof Chest", Hotel.roof, ["Combat", "Progressive Swap:2"]),
    LocationData("Nexus - Isolated Chest", Nexus.top, ["Progressive Swap:2"]),
    LocationData("Overworld - Near Gate Chest", Overworld.DEFAULT),
    LocationData("Overworld - After Temple Chest", Overworld.post_windmill, ["Combat"]),
    LocationData("Red Cave - Top Cave Slasher Chest", Red_Cave.top, ["Combat"]),
    # 72BAD10E-598F-F238-0103-60E1B36F6240
    LocationData("Red Cave - Middle Cave Right Chest", Red_Cave.center, type=LocationType.Key),
    # AE87F1D5-57E0-1749-7E1E-1D0BCC1BCAB4
    LocationData("Red Cave - Middle Cave Left Chest", Red_Cave.center, ["Combat"], type=LocationType.Key),
    LocationData("Red Cave - Middle Cave Middle Chest", Red_Cave.center, ["Small Key (Red Cave):6"]),
    LocationData("Red Cave - Boss Chest", Red_Cave.exit, []),
    # 4A9DC50D-8739-9AD8-2CB1-82ECE29D3B6F
    LocationData("Red Cave - Left Cave Rapids Chest", Red_Cave.left, ["Combat"], type=LocationType.Key),
    # A7672339-F3FB-C49E-33CE-42A49D7E4533
    LocationData("Red Cave - Right Cave Slasher Chest", Red_Cave.right, ["Combat"], type=LocationType.Key),
    # 83286BFB-FFDA-237E-BA57-CA2E532E1DC7
    LocationData("Red Cave - Right Cave Four Shooter Chest", Red_Cave.right, ["Combat"], type=LocationType.Key),
    # CDA1FF45-0F88-4855-B0EC-A9B42376C33F
    LocationData("Red Cave - Left Cave Sticky Chest", Red_Cave.left, ["Combat"], type=LocationType.Key),
    LocationData("Red Cave - Widen Upgrade Chest", Red_Cave.bottom),
    LocationData("Red Cave - Isaac Dungeon Chest", Red_Cave.Isaac, ["Combat"]),
    LocationData("Red Sea - Lonely Chest", Red_Sea.DEFAULT),
    LocationData("Red Sea - Out-of-bounds Chest", Red_Sea.DEFAULT, ["Progressive Swap:2"]),
    LocationData("Young Town - Stab Reward Chest", Suburb.card_house),
    LocationData("Young Town - Killers Chest", Suburb.DEFAULT, ["Combat", "Progressive Swap:2"]),
    LocationData("Space - Left Chest", Space.DEFAULT),
    LocationData("Space - Right Chest", Space.DEFAULT),
    LocationData("Space - Challenge Area Chest", Space.Gauntlet),
    # Wiggle glitch available
    LocationData("Space - Hidden Chest", Space.DEFAULT),
    # 3307AA58-CCF1-FB0D-1450-5AF0A0C458F7
    LocationData("Street - Key Chest", Street.DEFAULT, ["Combat"], type=LocationType.Key),
    LocationData("Street - Broom Chest", Street.DEFAULT),
    LocationData("Street - Secret Chest", Street.DEFAULT, ["Progressive Swap:2"]),
    LocationData("Terminal - Broken Bridge Chest", Terminal.DEFAULT),
    LocationData("Windmill - Chest", Windmill.DEFAULT, []),
    LocationData("Windmill - Activation", Windmill.DEFAULT, []),
    LocationData("Boss Rush - Reward Chest", Boss_Rush.DEFAULT),
    # Health Cicadas
    LocationData("Apartment - Health Cicada", Apartment.floor_3, ["Defeat Watcher"], type=LocationType.Cicada),
    LocationData("Beach - Health Cicada", Beach.gauntlet, [], type=LocationType.Cicada),
    LocationData("Temple of the Seeing One - Health Cicada", Bedroom.exit, ["Defeat Seer"], type=LocationType.Cicada),
    # Has to be frame 4
    LocationData("Cell - Health Cicada", Cell.DEFAULT, [CellGate.typename(), "Jump Shoes"], type=LocationType.Cicada),
    LocationData("Circus - Health Cicada", Circus.boss_gauntlet, ["Defeat Servants"], type=LocationType.Cicada),
    LocationData("Mountain Cavern - Health Cicada", Crowd.floor_1, ["Defeat The Wall"], type=LocationType.Cicada),
    LocationData("Hotel - Health Cicada", Hotel.floor_1, ["Defeat Manager"], type=LocationType.Cicada),
    LocationData("Overworld - Health Cicada", Overworld.Gauntlet, [], type=LocationType.Cicada),
    LocationData("Red Cave - Health Cicada", Red_Cave.top, ["Defeat Rogue"], type=LocationType.Cicada),
    LocationData("Young Town - Health Cicada", Suburb.DEFAULT, [SuburbGate.typename()], type=LocationType.Cicada),
    LocationData("Temple of the Seeing One - Green Key", Bedroom.exit, [], type=LocationType.BigKey),
    LocationData("Red Cave - Red Key", Red_Cave.exit, [], type=LocationType.BigKey),
    LocationData("Mountain Cavern - Blue Key", Crowd.exit, [], type=LocationType.BigKey),
    LocationData("Red Cave - Middle Cave Left Tentacle", Red_Cave.center, ["Combat"], type=LocationType.Tentacle),
    LocationData("Red Cave - Middle Cave Right Tentacle", Red_Cave.center, [], type=LocationType.Tentacle),
    LocationData("Red Cave - Left Cave Tentacle", Red_Cave.left, ["Small Key (Red Cave):6"], type=LocationType.Tentacle),
    LocationData("Red Cave - Right Cave Tentacle", Red_Cave.right, ["Small Key (Red Cave):6"], type=LocationType.Tentacle),
    LocationData("GO - Defeat Briar", Go.top, ["Combat", "Jump Shoes"]),
    # Nexus portals
    LocationData("Apartment - Warp Pad", Apartment.floor_1, type=LocationType.Nexus),
    LocationData("Beach - Warp Pad", Beach.DEFAULT, type=LocationType.Nexus),
    LocationData("Temple of the Seeing One - Warp Pad", Bedroom.exit, type=LocationType.Nexus),
    LocationData("Blue - Warp Pad", Blue.DEFAULT, type=LocationType.Nexus),
    LocationData("Cell - Warp Pad", Cell.DEFAULT, type=LocationType.Nexus),
    LocationData("Cliffs - Warp Pad", Cliff.DEFAULT, type=LocationType.Nexus),
    LocationData("Circus - Warp Pad", Circus.DEFAULT, type=LocationType.Nexus),
    LocationData("Mountain Cavern - Warp Pad", Crowd.exit, type=LocationType.Nexus),
    LocationData("Fields - Warp Pad", Fields.DEFAULT, type=LocationType.Nexus),
    LocationData("Deep Forest - Warp Pad", Forest.DEFAULT, type=LocationType.Nexus),
    LocationData("GO - Warp Pad", Go.bottom, type=LocationType.Nexus),
    LocationData("Happy - Warp Pad", Happy.DEFAULT, type=LocationType.Nexus),
    LocationData("Hotel - Warp Pad", Hotel.floor_4, type=LocationType.Nexus),
    LocationData("Overworld - Warp Pad", Overworld.DEFAULT, type=LocationType.Nexus),
    LocationData("Red Cave - Warp Pad", Red_Cave.exit, type=LocationType.Nexus),
    LocationData("Red Sea - Warp Pad", Red_Sea.DEFAULT, type=LocationType.Nexus),
    LocationData("Young Town - Warp Pad", Suburb.DEFAULT, type=LocationType.Nexus),
    LocationData("Space - Warp Pad", Space.DEFAULT, type=LocationType.Nexus),
    LocationData("Terminal - Warp Pad", Terminal.DEFAULT, type=LocationType.Nexus),
    LocationData("Windmill - Warp Pad", Windmill.entrance, type=LocationType.Nexus),
    LocationData("Blue - Completion Reward", Blue.DEFAULT),
    LocationData("Happy - Completion Reward", Happy.gauntlet),
    # Dust locations
    LocationData("Apartment - 1F Shortcut Room Dust 1", Apartment.floor_1, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Apartment - 2F Switch Pillar Rat Maze Dust", Apartment.floor_2, ["Jump Shoes", "Small Key (Apartment):3"], type=LocationType.Dust),
    LocationData("Apartment - 2F Dash Trap Rat Maze Dust", Apartment.floor_2, ["Jump Shoes", "Small Key (Apartment):3"], type=LocationType.Dust),
    LocationData("Apartment - 2F Flooded Room Dust", Apartment.floor_2, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Apartment - 1F Couches Dust", Apartment.floor_1_top_left, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Apartment - 1F Shortcut Room Dust 2", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Apartment - 1F Rat Maze Chest Dust 1", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Apartment - 1F Rat Maze Chest Dust 2", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Apartment - 1F Rat Maze Chest Dust 3", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Apartment - 1F Entrance Dust", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Apartment - 1F Flooded Room Dust", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Apartment - 1F Flooded Library Dust", Apartment.floor_1, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Laser Room Dust 1", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Laser Room Dust 2", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Room With Holes Dust 1", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Room With Holes Dust 2", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Past Shieldy Puzzle Dust 1", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Before Boss Dust 1", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Past Shieldy Puzzle Dust 2", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Shieldy Room Dust 1", Bedroom.shieldy_room, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Shieldy Room Dust 2", Bedroom.shieldy_room, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Laser Room Dust 3", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Entrance Dust 1", Bedroom.entrance, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Entrance Dust 2", Bedroom.entrance, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Before Boss Dust 2", Bedroom.core, type=LocationType.Dust),
    LocationData("Temple of the Seeing One - Laser Room Dust 4", Bedroom.core, type=LocationType.Dust),
    LocationData("Blue - Laser Room Dust", Blue.DEFAULT, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Circus - Dash Trap Dust", Circus.entry_gauntlets, type=LocationType.Dust),
    LocationData("Circus - Fire Pillars in Water Dust 3", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Lion Dust 1", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Lion Dust 2", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Fire Pillars in Water Dust 2", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Fire Pillars in Water Dust 1", Circus.third_key_gauntlet, type=LocationType.Dust),
    # Overlaps with Fire Pillars in Water Dust 3
    LocationData("Circus - Fire Pillars in Water Dust 4", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Dog Room Dust", Circus.boss_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Javiera Dust 2", Circus.circlejump_gauntlets, type=LocationType.Dust),
    LocationData("Circus - Javiera Dust 1", Circus.circlejump_gauntlets, type=LocationType.Dust),
    LocationData("Circus - Slime and Fire Pillar Dust", Circus.past_entrance_lake, type=LocationType.Dust),
    LocationData("Circus - Small Contort Room Dust", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Save Point Dust", Circus.third_key_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Clown Dust 1", Circus.entry_gauntlets, type=LocationType.Dust),
    LocationData("Circus - Clown Dust 2", Circus.entry_gauntlets, type=LocationType.Dust),
    LocationData("Circus - Spike Dust", Circus.boss_gauntlet, type=LocationType.Dust),
    LocationData("Circus - Dash Pad over Hole Dust", Circus.entrance_lake, type=LocationType.Dust),
    LocationData("Circus - Lion and Dash Pad Dust", Circus.past_entrance_lake, type=LocationType.Dust),
    LocationData("Circus - Spike Roller in Water Dust", Circus.entrance_lake, type=LocationType.Dust),
    LocationData("Circus - Entrance Dust", Circus.DEFAULT, type=LocationType.Dust),
    LocationData("Mountain Cavern - 3F Top Center Moving Platform Dust", Crowd.floor_3, type=LocationType.Dust),
    LocationData("Mountain Cavern - 3F Top Right Moving Platform Dust", Crowd.floor_3, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Mountain Cavern - 3F Roller Dust", Crowd.floor_3_center, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Frogs and Annoyers Dust", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Rotators and Annoyers Dust 1", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Rotators and Annoyers Dust 2", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Circular Hole Dust 1", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Circular Hole Dust 2", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Crossing Moving Platforms Dust 1", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Crossing Moving Platforms Dust 2", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Moving Platform Crossroad Dust 1", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Moving Platform Crossroad Dust 2", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Mountain Cavern - 2F Moving Platform Crossroad Dust 3", Crowd.floor_2_gauntlets, type=LocationType.Dust),
    LocationData("Debug - Moving Platform Dust", Debug.DEFAULT, type=LocationType.Dust),
    LocationData("Debug - Whirlpool Room Dust 1", Debug.DEFAULT, type=LocationType.Dust),
    LocationData("Debug - Whirlpool Room Dust 2", Debug.DEFAULT, type=LocationType.Dust),
    LocationData("Debug - Sound Test Console Dust", Debug.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 1", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 2", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 3", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 4", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 5", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 6", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 7", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 8", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Goldman's Cave Dust 9", Fields.Goldman, type=LocationType.Dust),
    LocationData("Fields - Lake After Spikes Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - North River Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - Lake After Holes Floating Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - South East of Lake Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - Lake Near Windmill Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - North of Lake Rapids Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - North East of Lake Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - Before Annoyer Maze Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - Mitra House Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - Near Red Gate Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - After Red Gate Dust", Fields.Past_Gate, type=LocationType.Dust),
    LocationData("Fields - Near Terminal Dust", Terminal.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - North West of Lake Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - Near Beach Dust", Fields.DEFAULT, type=LocationType.Dust),
    LocationData("Fields - South West Corner Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - South East of Gauntlet Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - Before Gauntlet Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - Island Chest Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - Island Start Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - Post Whirlpool Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Fields - Olive Dust", Fields.Lake, type=LocationType.Dust),
    LocationData("Deep Forest - Relaxation Pond Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Near Cliff Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Floating Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Thorax Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Carved Rock Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Tiny Island Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Inlet Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Deep Forest - Before Inlet Chest Dust", Forest.DEFAULT, type=LocationType.Dust),
    LocationData("Happy - Final Room Dust", Happy.gauntlet, [], type=LocationType.Dust),
    LocationData("Happy - Dustmaid Dust", Happy.gauntlet, [], type=LocationType.Dust),
    LocationData("Hotel - 1F Floating Dustmaid Dust", Hotel.floor_1, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 3F Hallway Dustmaid Dust 2", Hotel.floor_3, ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 3F Hallway Dustmaid Dust 1", Hotel.floor_3, ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Moving Platform Crossroad 1", Hotel.floor_4, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Boss Dust", Hotel.floor_1, ["Small Key (Hotel):6","Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Gasguy Dust", Hotel.floor_1, ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Dustmaid and Steampipe Dust 3", Hotel.floor_1, ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Dustmaid and Steampipe Dust 2", Hotel.floor_1, ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Dustmaid and Steampipe Dust 1", Hotel.floor_1, ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Dustmaid and Steampipe Dust 4", Hotel.floor_1, ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 2F Steampipe Dust 2", Hotel.floor_2, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 2F Steampipe Dust 1", Hotel.floor_2, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 1F Locked Dust", Hotel.floor_1, ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 2F Dustmaid and Steampipe Dust 3", Hotel.floor_2, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 2F Dustmaid and Steampipe Dust 1", Hotel.floor_2, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 2F Dustmaid and Steampipe Dust 2", Hotel.floor_2, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 2F Dustmaid Hallway Dust", Hotel.floor_2, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 3F Stream Dustmaid Dust", Hotel.floor_3, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 3F Bedroom Dust", Hotel.floor_3, ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Slime Dust 2", Hotel.floor_4, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Slime Dust 1", Hotel.floor_4, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Moving Platform Crossroad 2", Hotel.floor_4, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Dustmaid Dust", Hotel.floor_4, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Near Elevator Dust", Hotel.floor_4, ["Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Spring Puzzle Dust", Hotel.floor_4, ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Hotel - 4F Moving Platform Puzzle Dust", Hotel.floor_4, ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Boss Dust 1", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Boss Dust 2", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Before Boss Dust", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Slasher Dust", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Before Slasher Dust", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Boss Dust 3", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Top Cave Boss Dust 4", Red_Cave.top, type=LocationType.Dust),
    LocationData("Red Cave - Left Cave Rapids Dust 1", Red_Cave.left, type=LocationType.Dust),
    LocationData("Red Cave - Left Cave Rapids Dust 2", Red_Cave.left, type=LocationType.Dust),
    LocationData("Red Cave - Right Cave Before Slasher Dust", Red_Cave.right, type=LocationType.Dust),
    LocationData("Red Cave - Right Cave Whirlpool Dust 1", Red_Cave.right, type=LocationType.Dust),
    LocationData("Red Cave - Left Cave Whirlpool Dust 1", Red_Cave.left, type=LocationType.Dust),
    LocationData("Red Cave - Left Cave Whirlpool Dust 2", Red_Cave.left, type=LocationType.Dust),
    LocationData("Red Cave - Right Cave Whirlpool Dust 2", Red_Cave.right, type=LocationType.Dust),
    LocationData("Space - Challenge Area Dustmaid Dust 1", Space.Gauntlet, type=LocationType.Dust),
    LocationData("Space - Challenge Area Dustmaid Dust 2", Space.Gauntlet, type=LocationType.Dust),
    LocationData("Space - Challenge Area Lion Dust 1", Space.Gauntlet, type=LocationType.Dust),
    LocationData("Space - Challenge Area Lion Dust 2", Space.Gauntlet, type=LocationType.Dust),
    LocationData("Street - After Bridge Dust 1", Street.DEFAULT, ["Small Key (Street):1"], type=LocationType.Dust),
    LocationData("Street - After Bridge Dust 2", Street.DEFAULT, ["Small Key (Street):1"], type=LocationType.Dust),
    LocationData("Boss Rush - Before Red Boss Dust", Boss_Rush.DEFAULT, type=LocationType.Dust),
    LocationData("Boss Rush - Red Boss Dust 1", Boss_Rush.DEFAULT, type=LocationType.Dust),
    LocationData("Boss Rush - Red Boss Dust 2", Boss_Rush.DEFAULT, type=LocationType.Dust),
    LocationData("Boss Rush - Red Boss Dust 3", Boss_Rush.DEFAULT, type=LocationType.Dust),
    LocationData("Boss Rush - Red Boss Dust 4", Boss_Rush.DEFAULT, type=LocationType.Dust),
    LocationData("Boss Rush - Manager Phase 1 Dust", Boss_Rush.DEFAULT, type=LocationType.Dust),
    LocationData("Boss Rush - Manager Phase 2 Dust", Boss_Rush.DEFAULT, type=LocationType.Dust)
]

locations_by_name: Dict[str, LocationData] = {location.name: location for location in all_locations}

def build_locations_by_region_dict():
    result: Dict[RegionEnum, List[LocationData]] = {}
    for location in all_locations:
        result.setdefault(location.region, []).append(location)
    return result


locations_by_region: Dict[RegionEnum, List[LocationData]] = build_locations_by_region_dict()

nexus_pad_locations = [location for location in all_locations if location.type == LocationType.Nexus]

location_groups = {
    "Warp Pads": [location.name for location in nexus_pad_locations],
}
