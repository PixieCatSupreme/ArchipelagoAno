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
    region: RegionEnum
    _name: str
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
    LocationData(Apartment.floor_1, "Apartment - 1F Ledge Chest", ["Combat"], type=LocationType.Key),
    # DE415E2A-06EE-83AC-F1A3-5DCA1FA44735
    LocationData(Apartment.floor_1, "Apartment - 1F Rat Maze Chest", ["Combat"], type=LocationType.Key),
    LocationData(Apartment.floor_1, "Apartment - 1F Exterior Chest", ["Combat", "Jump Shoes"]),
    LocationData(Apartment.floor_1_top_left, "Apartment - 1F Couches Chest", ["Combat", "Jump Shoes"]),
    # 5B55A264-3FCD-CF38-175C-141B2D093029
    LocationData(Apartment.floor_2, "Apartment - 2F Rat Maze Chest", ["Combat", "Jump Shoes"], type=LocationType.Key),
    # 2BBF01C8-8267-7E71-5BD4-325001DBC0BA
    LocationData(Apartment.floor_3, "Apartment - 3F Gauntlet Chest", ["Combat"], type=LocationType.Key),
    LocationData(Apartment.floor_3, "Apartment - Boss Chest", ["Defeat Watcher"]),
    LocationData(Beach.DEFAULT, "Beach - Dock Chest"),
    LocationData(Beach.gauntlet, "Beach - Secret Chest", ["Progressive Swap:2"]),
    LocationData(Beach.DEFAULT, "Beach - Out-of-bounds Chest", ["Progressive Swap:2"]),
    # 40DE36CF-9238-F8B0-7A57-C6C8CA465CC2
    LocationData(Bedroom.entrance, "Temple of the Seeing One - Entrance Chest", type=LocationType.Key),
    LocationData(Bedroom.shieldy_room, "Temple of the Seeing One - Shieldy Room Chest", []),
    LocationData(Bedroom.core, "Temple of the Seeing One - Rock-Surrounded Chest", []),
    LocationData(Bedroom.exit, "Temple of the Seeing One - Boss Chest", []),
    # D41F2750-E3C7-BBB4-D650-FAFC190EBD32
    LocationData(Bedroom.after_statue, "Temple of the Seeing One - After Statue Left Chest", [], type=LocationType.Key),
    LocationData(Bedroom.after_statue, "Temple of the Seeing One - After Statue Right Chest", []),
    # 401939A4-41BA-E07E-3BA2-DC22513DCC5C
    LocationData(Bedroom.core, "Temple of the Seeing One - Dark Room Chest", [], type=LocationType.Key),
    LocationData(Blank.windmill, "Blank - Card Chest"),
    LocationData(Cell.DEFAULT, "Cell - Top Left Chest", ["Jump Shoes"]),
    LocationData(Cell.DEFAULT, "Cell - Chaser Gauntlet Chest", ["Progressive Swap:2", "Combat", "Jump Shoes"]),
    # 75C2D434-4AE8-BCD0-DBEB-8E6CDA67BF45
    LocationData(Circus.entry_gauntlets, "Circus - Rat Maze Chest", [], type=LocationType.Key),
    LocationData(Circus.entry_gauntlets, "Circus - Clowns Chest", []),
    LocationData(Circus.circlejump_gauntlets, "Circus - Fire Pillar Chest", []),
    # 69E8FBD6-2DA3-D25E-446F-6A59AC3E9FC2
    LocationData(Circus.entry_gauntlets, "Circus - Arthur Chest", [], type=LocationType.Key),
    # 6A95EB2F-75FD-8649-5E07-3ED37C69A9FB
    LocationData(Circus.circlejump_gauntlets, "Circus - Javiera Chest", [], type=LocationType.Key),
    # A2479A02-9B0D-751F-71A4-DB15C4982DF5
    LocationData(Circus.third_key_gauntlet, "Circus - Lion Chest", [], type=LocationType.Key),
    LocationData(Circus.north_gauntlet, "Circus - Double Clowns Chest", []),
    LocationData(Circus.boss_gauntlet, "Circus - Boss Chest", ["Defeat Servants"]),
    LocationData(Cliff.post_windmill, "Cliffs - Upper Chest"),
    LocationData(Cliff.post_windmill, "Cliffs - Lower Chest"),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Crowded Ledge Chest",
                 ["Small Key (Mountain Cavern):4"]),
    # BE2FB96B-1D5F-FCD1-3F58-D158DB982C21
    LocationData(Crowd.floor_2, "Mountain Cavern - 2F Four Enemies Chest", ["Combat"], type=LocationType.Key),
    # 5743A883-D209-2518-70D7-869D14925B77
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Entrance Chest", type=LocationType.Key),
    # 21EE2D01-54FB-F145-9464-4C2CC8725EB3
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Frogs and Dog Chest", type=LocationType.Key),
    LocationData(Crowd.floor_3_center, "Mountain Cavern - 3F Roller Chest", []),
    LocationData(Crowd.exit, "Mountain Cavern - Boss Chest", []),
    LocationData(Crowd.jump_challenge, "Mountain Cavern - Extend Upgrade Chest", ["Combat", "Jump Shoes"]),
    # 868736EF-EC8B-74C9-ACAB-B7BC56A44394
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Frogs and Rotators Chest", type=LocationType.Key),
    LocationData(Debug.DEFAULT, "Debug - River Puzzles Chest", ["Combat", "Jump Shoes"]),
    LocationData(Debug.DEFAULT, "Debug - Upper Prison Chest"),
    LocationData(Debug.DEFAULT, "Debug - Lower Prison Chest"),
    LocationData(Debug.DEFAULT, "Debug - Jumping Chest"),
    LocationData(Debug.DEFAULT, "Debug - Maze Chest", ["Jump Shoes"]),
    LocationData(Drawer.DEFAULT, "Drawer - Game Over Chest", ["Progressive Swap:2"]),
    LocationData(Drawer.DEFAULT, "Drawer - Brown Area Chest"),
    LocationData(Fields.Lake, "Fields - Island Chest", ["Combat", "Jump Shoes"]),
    LocationData(Fields.Lake, "Fields - Gauntlet Chest", ["Combat", "Jump Shoes"]),
    # Cleaning up his cave
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Chest", ["Combat"]),
    LocationData(Fields.DEFAULT, "Fields - Blocked River Chest", ["Progressive Swap:2", "Jump Shoes"]),
    LocationData(Fields.DEFAULT, "Fields - Cardboard Box", ["Miao"]),
    LocationData(Fields.DEFAULT, "Fields - Shopkeeper Trade", ["Cardboard Box"]),
    LocationData(Fields.DEFAULT, "Fields - Mitra Trade", ["Biking Shoes"]),
    # Hidden path
    LocationData(Fields.North_Secret_Area, "Fields - Near Overworld Secret Chest"),
    # Hidden path
    LocationData(Fields.DEFAULT, "Fields - Secluded Glen Chest", ["SwapOrSecret"]),
    # Hidden path
    # Logically, this is in Terminal, because it is separated from the rest of Fields in the same way Terminal is.
    LocationData(Terminal.DEFAULT, "Fields - Near Terminal Secret Chest", ["SwapOrSecret"]),
    LocationData(Forest.DEFAULT, "Deep Forest - Inlet Chest", ["Combat"]),
    # This is the one that takes 2 hours
    LocationData(Forest.DEFAULT, "Deep Forest - Bunny Chest", ["Progressive Swap:2"]),
    LocationData(Go.bottom, "GO - Swap Upgrade Chest"),
    LocationData(Go.bottom, "GO - Secret Color Puzzle Chest", ["Progressive Swap:2"]),
    # 6C8870D4-7600-6FFD-B425-2D951E65E160
    LocationData(Hotel.floor_4, "Hotel - 4F Annoyers Chest", ["Combat", "Jump Shoes"], type=LocationType.Key),
    LocationData(Hotel.floor_4, "Hotel - 4F Dust Blower Maze Chest", ["Combat", "Jump Shoes", "Small Key (Hotel):1"]),
    LocationData(Hotel.floor_3, "Hotel - 3F Dashers Chest", ["Small Key (Hotel):6"]),
    # 64EE884F-EA96-FB09-8A9E-F75ABDB6DC0D
    LocationData(Hotel.floor_3, "Hotel - 3F Gasguy Chest", ["Combat"], type=LocationType.Key),
    # 075E6024-FE2D-9C4A-1D2B-D627655FD31A
    LocationData(Hotel.floor_3, "Hotel - 3F Rotators Chest", ["Combat"], type=LocationType.Key),
    LocationData(Hotel.floor_2_right, "Hotel - 2F Dog Chest", ["Combat"]),
    # 1990B3A2-DBF8-85DA-C372-ADAFAA75744C
    LocationData(Hotel.floor_2_right, "Hotel - 2F Crevice Right Chest", type=LocationType.Key),
    # D2392D8D-0633-2640-09FA-4B921720BFC4
    LocationData(Hotel.floor_2, "Hotel - 2F Backrooms Chest", ["Combat"], type=LocationType.Key),
    # 019CBC29-3614-9302-6848-DDAEDC7C49E5
    LocationData(Hotel.floor_1, "Hotel - 1F Burst Flowers Chest", type=LocationType.Key),
    # 9D6FDA36-0CC6-BACC-3844-AEFB6C5C6290
    LocationData(Hotel.floor_2, "Hotel - 2F Crevice Left Chest", ["Jump Shoes"], type=LocationType.Key),
    LocationData(Hotel.floor_1, "Hotel - Boss Chest", ["Defeat Manager"]),
    LocationData(Hotel.roof, "Hotel - Roof Chest", ["Combat", "Progressive Swap:2"]),
    LocationData(Nexus.top, "Nexus - Isolated Chest", ["Progressive Swap:2"]),
    LocationData(Overworld.DEFAULT, "Overworld - Near Gate Chest"),
    LocationData(Overworld.post_windmill, "Overworld - After Temple Chest", ["Combat"]),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Slasher Chest", ["Combat"]),
    # 72BAD10E-598F-F238-0103-60E1B36F6240
    LocationData(Red_Cave.center, "Red Cave - Middle Cave Right Chest", type=LocationType.Key),
    # AE87F1D5-57E0-1749-7E1E-1D0BCC1BCAB4
    LocationData(Red_Cave.center, "Red Cave - Middle Cave Left Chest", ["Combat"], type=LocationType.Key),
    LocationData(Red_Cave.center, "Red Cave - Middle Cave Middle Chest", ["Small Key (Red Cave):6"]),
    LocationData(Red_Cave.exit, "Red Cave - Boss Chest", []),
    # 4A9DC50D-8739-9AD8-2CB1-82ECE29D3B6F
    LocationData(Red_Cave.left, "Red Cave - Left Cave Rapids Chest", ["Combat"], type=LocationType.Key),
    # A7672339-F3FB-C49E-33CE-42A49D7E4533
    LocationData(Red_Cave.right, "Red Cave - Right Cave Slasher Chest", ["Combat"], type=LocationType.Key),
    # 83286BFB-FFDA-237E-BA57-CA2E532E1DC7
    LocationData(Red_Cave.right, "Red Cave - Right Cave Four Shooter Chest", ["Combat"], type=LocationType.Key),
    # CDA1FF45-0F88-4855-B0EC-A9B42376C33F
    LocationData(Red_Cave.left, "Red Cave - Left Cave Sticky Chest", ["Combat"], type=LocationType.Key),
    LocationData(Red_Cave.bottom, "Red Cave - Widen Upgrade Chest"),
    LocationData(Red_Cave.Isaac, "Red Cave - Isaac Dungeon Chest", ["Combat"]),
    LocationData(Red_Sea.DEFAULT, "Red Sea - Lonely Chest"),
    LocationData(Red_Sea.DEFAULT, "Red Sea - Out-of-bounds Chest", ["Progressive Swap:2"]),
    LocationData(Suburb.card_house, "Young Town - Stab Reward Chest"),
    LocationData(Suburb.DEFAULT, "Young Town - Killers Chest", ["Combat", "Progressive Swap:2"]),
    LocationData(Space.DEFAULT, "Space - Left Chest"),
    LocationData(Space.DEFAULT, "Space - Right Chest"),
    LocationData(Space.Gauntlet, "Space - Challenge Area Chest"),
    # Wiggle glitch available
    LocationData(Space.DEFAULT, "Space - Hidden Chest"),
    # 3307AA58-CCF1-FB0D-1450-5AF0A0C458F7
    LocationData(Street.DEFAULT, "Street - Key Chest", ["Combat"], type=LocationType.Key),
    LocationData(Street.DEFAULT, "Street - Broom Chest"),
    LocationData(Street.DEFAULT, "Street - Secret Chest", ["Progressive Swap:2"]),
    LocationData(Terminal.DEFAULT, "Terminal - Broken Bridge Chest"),
    LocationData(Windmill.DEFAULT, "Windmill - Chest", []),
    LocationData(Windmill.DEFAULT, "Windmill - Activation", []),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Reward Chest"),
    # Health Cicadas
    LocationData(Apartment.floor_3, "Apartment - Health Cicada", ["Defeat Watcher"], type=LocationType.Cicada),
    LocationData(Beach.gauntlet, "Beach - Health Cicada", [], type=LocationType.Cicada),
    LocationData(Bedroom.exit, "Temple of the Seeing One - Health Cicada", ["Defeat Seer"], type=LocationType.Cicada),
    # Has to be frame 4
    LocationData(Cell.DEFAULT, "Cell - Health Cicada", [CellGate.typename(), "Jump Shoes"], type=LocationType.Cicada),
    LocationData(Circus.boss_gauntlet, "Circus - Health Cicada", ["Defeat Servants"], type=LocationType.Cicada),
    LocationData(Crowd.floor_1, "Mountain Cavern - Health Cicada", ["Defeat The Wall"], type=LocationType.Cicada),
    LocationData(Hotel.floor_1, "Hotel - Health Cicada", ["Defeat Manager"], type=LocationType.Cicada),
    LocationData(Overworld.Gauntlet, "Overworld - Health Cicada", [], type=LocationType.Cicada),
    LocationData(Red_Cave.top, "Red Cave - Health Cicada", ["Defeat Rogue"], type=LocationType.Cicada),
    LocationData(Suburb.DEFAULT, "Young Town - Health Cicada", [SuburbGate.typename()], type=LocationType.Cicada),
    LocationData(Bedroom.exit, "Temple of the Seeing One - Green Key", [], type=LocationType.BigKey),
    LocationData(Red_Cave.exit, "Red Cave - Red Key", [], type=LocationType.BigKey),
    LocationData(Crowd.exit, "Mountain Cavern - Blue Key", [], type=LocationType.BigKey),
    LocationData(Red_Cave.center, "Red Cave - Middle Cave Left Tentacle", ["Combat"], type=LocationType.Tentacle),
    LocationData(Red_Cave.center, "Red Cave - Middle Cave Right Tentacle", [], type=LocationType.Tentacle),
    LocationData(Red_Cave.left, "Red Cave - Left Cave Tentacle", ["Small Key (Red Cave):6"], type=LocationType.Tentacle),
    LocationData(Red_Cave.right, "Red Cave - Right Cave Tentacle", ["Small Key (Red Cave):6"], type=LocationType.Tentacle),
    LocationData(Go.top, "GO - Defeat Briar", ["Combat", "Jump Shoes"]),
    # Nexus portals
    LocationData(Apartment.floor_1, "Apartment - Warp Pad", type=LocationType.Nexus),
    LocationData(Beach.DEFAULT, "Beach - Warp Pad", type=LocationType.Nexus),
    LocationData(Bedroom.exit, "Temple of the Seeing One - Warp Pad", type=LocationType.Nexus),
    LocationData(Blue.DEFAULT, "Blue - Warp Pad", type=LocationType.Nexus),
    LocationData(Cell.DEFAULT, "Cell - Warp Pad", type=LocationType.Nexus),
    LocationData(Cliff.DEFAULT, "Cliffs - Warp Pad", type=LocationType.Nexus),
    LocationData(Circus.DEFAULT, "Circus - Warp Pad", type=LocationType.Nexus),
    LocationData(Crowd.exit, "Mountain Cavern - Warp Pad", type=LocationType.Nexus),
    LocationData(Fields.DEFAULT, "Fields - Warp Pad", type=LocationType.Nexus),
    LocationData(Forest.DEFAULT, "Deep Forest - Warp Pad", type=LocationType.Nexus),
    LocationData(Go.bottom, "GO - Warp Pad", type=LocationType.Nexus),
    LocationData(Happy.DEFAULT, "Happy - Warp Pad", type=LocationType.Nexus),
    LocationData(Hotel.floor_4, "Hotel - Warp Pad", type=LocationType.Nexus),
    LocationData(Overworld.DEFAULT, "Overworld - Warp Pad", type=LocationType.Nexus),
    LocationData(Red_Cave.exit, "Red Cave - Warp Pad", type=LocationType.Nexus),
    LocationData(Red_Sea.DEFAULT, "Red Sea - Warp Pad", type=LocationType.Nexus),
    LocationData(Suburb.DEFAULT, "Young Town - Warp Pad", type=LocationType.Nexus),
    LocationData(Space.DEFAULT, "Space - Warp Pad", type=LocationType.Nexus),
    LocationData(Terminal.DEFAULT, "Terminal - Warp Pad", type=LocationType.Nexus),
    LocationData(Windmill.entrance, "Windmill - Warp Pad", type=LocationType.Nexus),
    LocationData(Blue.DEFAULT, "Blue - Completion Reward"),
    LocationData(Happy.gauntlet, "Happy - Completion Reward"),
    # Dust locations
    LocationData(Apartment.floor_1, "Apartment - 1F Shortcut Room Dust 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Apartment.floor_2, "Apartment - 2F Switch Pillar Rat Maze Dust", ["Jump Shoes", "Small Key (Apartment):3"], type=LocationType.Dust),
    LocationData(Apartment.floor_2, "Apartment - 2F Dash Trap Rat Maze Dust", ["Jump Shoes", "Small Key (Apartment):3"], type=LocationType.Dust),
    LocationData(Apartment.floor_2, "Apartment - 2F Flooded Room Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Apartment.floor_1_top_left, "Apartment - 1F Couches Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Shortcut Room Dust 2", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Rat Maze Chest Dust 1", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Rat Maze Chest Dust 2", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Rat Maze Chest Dust 3", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Entrance Dust", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Flooded Room Dust", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "Apartment - 1F Flooded Library Dust", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Laser Room Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Laser Room Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Room With Holes Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Room With Holes Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Past Shieldy Puzzle Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Before Boss Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Past Shieldy Puzzle Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.shieldy_room, "Temple of the Seeing One - Shieldy Room Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.shieldy_room, "Temple of the Seeing One - Shieldy Room Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Laser Room Dust 3", type=LocationType.Dust),
    LocationData(Bedroom.entrance, "Temple of the Seeing One - Entrance Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.entrance, "Temple of the Seeing One - Entrance Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Before Boss Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Temple of the Seeing One - Laser Room Dust 4", type=LocationType.Dust),
    LocationData(Blue.DEFAULT, "Blue - Laser Room Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Circus.entry_gauntlets, "Circus - Dash Trap Dust", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Fire Pillars in Water Dust 3", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Lion Dust 1", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Lion Dust 2", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Fire Pillars in Water Dust 2", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Fire Pillars in Water Dust 1", type=LocationType.Dust),
    # Overlaps with Fire Pillars in Water Dust 3
    LocationData(Circus.third_key_gauntlet, "Circus - Fire Pillars in Water Dust 4", type=LocationType.Dust),
    LocationData(Circus.boss_gauntlet, "Circus - Dog Room Dust", type=LocationType.Dust),
    LocationData(Circus.circlejump_gauntlets, "Circus - Javiera Dust 2", type=LocationType.Dust),
    LocationData(Circus.circlejump_gauntlets, "Circus - Javiera Dust 1", type=LocationType.Dust),
    LocationData(Circus.past_entrance_lake, "Circus - Slime and Fire Pillar Dust", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Small Contort Room Dust", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Circus - Save Point Dust", type=LocationType.Dust),
    LocationData(Circus.entry_gauntlets, "Circus - Clown Dust 1", type=LocationType.Dust),
    LocationData(Circus.entry_gauntlets, "Circus - Clown Dust 2", type=LocationType.Dust),
    LocationData(Circus.boss_gauntlet, "Circus - Spike Dust", type=LocationType.Dust),
    LocationData(Circus.entrance_lake, "Circus - Dash Pad over Hole Dust", type=LocationType.Dust),
    LocationData(Circus.past_entrance_lake, "Circus - Lion and Dash Pad Dust", type=LocationType.Dust),
    LocationData(Circus.entrance_lake, "Circus - Spike Roller in Water Dust", type=LocationType.Dust),
    LocationData(Circus.DEFAULT, "Circus - Entrance Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_3, "Mountain Cavern - 3F Top Center Moving Platform Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_3, "Mountain Cavern - 3F Top Right Moving Platform Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Crowd.floor_3_center, "Mountain Cavern - 3F Roller Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Frogs and Annoyers Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Rotators and Annoyers Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Rotators and Annoyers Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Circular Hole Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Circular Hole Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Crossing Moving Platforms Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Crossing Moving Platforms Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Moving Platform Crossroad Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Moving Platform Crossroad Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "Mountain Cavern - 2F Moving Platform Crossroad Dust 3", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Debug - Moving Platform Dust", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Debug - Whirlpool Room Dust 1", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Debug - Whirlpool Room Dust 2", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Debug - Sound Test Console Dust", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 1", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 2", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 3", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 4", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 5", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 6", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 7", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 8", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Fields - Goldman's Cave Dust 9", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Lake After Spikes Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - North River Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Lake After Holes Floating Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - South East of Lake Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Lake Near Windmill Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - North of Lake Rapids Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - North East of Lake Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - Before Annoyer Maze Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - Mitra House Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - Near Red Gate Dust", type=LocationType.Dust),
    LocationData(Fields.Past_Gate, "Fields - After Red Gate Dust", type=LocationType.Dust),
    LocationData(Terminal.DEFAULT, "Fields - Near Terminal Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - North West of Lake Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Fields - Near Beach Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - South West Corner Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - South East of Gauntlet Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Before Gauntlet Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Island Chest Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Island Start Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Post Whirlpool Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Fields - Olive Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Relaxation Pond Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Near Cliff Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Floating Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Thorax Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Carved Rock Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Tiny Island Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Inlet Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Deep Forest - Before Inlet Chest Dust", type=LocationType.Dust),
    LocationData(Happy.gauntlet, "Happy - Final Room Dust", [], type=LocationType.Dust),
    LocationData(Happy.gauntlet, "Happy - Dustmaid Dust", [], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Floating Dustmaid Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "Hotel - 3F Hallway Dustmaid Dust 2", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "Hotel - 3F Hallway Dustmaid Dust 1", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Moving Platform Crossroad 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Boss Dust", ["Small Key (Hotel):6","Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Gasguy Dust", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Dustmaid and Steampipe Dust 3", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Dustmaid and Steampipe Dust 2", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Dustmaid and Steampipe Dust 1", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Dustmaid and Steampipe Dust 4", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "Hotel - 2F Steampipe Dust 2", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "Hotel - 2F Steampipe Dust 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "Hotel - 1F Locked Dust", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "Hotel - 2F Dustmaid and Steampipe Dust 3", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "Hotel - 2F Dustmaid and Steampipe Dust 1", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "Hotel - 2F Dustmaid and Steampipe Dust 2", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "Hotel - 2F Dustmaid Hallway Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "Hotel - 3F Stream Dustmaid Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "Hotel - 3F Bedroom Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Slime Dust 2", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Slime Dust 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Moving Platform Crossroad 2", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Dustmaid Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Near Elevator Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Spring Puzzle Dust", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "Hotel - 4F Moving Platform Puzzle Dust", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Boss Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Boss Dust 2", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Before Boss Dust", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Slasher Dust", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Before Slasher Dust", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Boss Dust 3", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Red Cave - Top Cave Boss Dust 4", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Red Cave - Left Cave Rapids Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Red Cave - Left Cave Rapids Dust 2", type=LocationType.Dust),
    LocationData(Red_Cave.right, "Red Cave - Right Cave Before Slasher Dust", type=LocationType.Dust),
    LocationData(Red_Cave.right, "Red Cave - Right Cave Whirlpool Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Red Cave - Left Cave Whirlpool Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Red Cave - Left Cave Whirlpool Dust 2", type=LocationType.Dust),
    LocationData(Red_Cave.right, "Red Cave - Right Cave Whirlpool Dust 2", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Space - Challenge Area Dustmaid Dust 1", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Space - Challenge Area Dustmaid Dust 2", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Space - Challenge Area Lion Dust 1", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Space - Challenge Area Lion Dust 2", type=LocationType.Dust),
    LocationData(Street.DEFAULT, "Street - After Bridge Dust 1", ["Small Key (Street):1"], type=LocationType.Dust),
    LocationData(Street.DEFAULT, "Street - After Bridge Dust 2", ["Small Key (Street):1"], type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Before Red Boss Dust", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Red Boss Dust 1", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Red Boss Dust 2", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Red Boss Dust 3", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Red Boss Dust 4", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Manager Phase 1 Dust", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Boss Rush - Manager Phase 2 Dust", type=LocationType.Dust)
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
