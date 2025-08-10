from enum import Enum, auto
from typing import NamedTuple, List, Dict

from .Regions import Apartment, Beach, Bedroom, Blank, Cell, Circus, Debug, Boss_Rush, Street, Space, Red_Cave, Drawer, \
    Cliff, Crowd, Fields, Terminal, Forest, Happy, Red_Sea, Overworld, Blue, Go, Hotel, Nexus, Suburb, Windmill, \
    RegionEnum, postgame_regions, postgame_without_secret_paths


class LocationType(Enum):
    Chest = 0
    Cicada = auto()
    BigKey = auto()
    Tentacle = auto()
    Dust = auto()
    Nexus = auto()
    AreaEvent = auto()

class LocationData(NamedTuple):
    region: RegionEnum
    base_name: str
    reqs: List[str] = []
    type:LocationType = LocationType.Chest
    has_key:bool = False
    outside_of_dungeon:bool = False

    @property
    def name(self):
        return f"{self.region.area_name()} - {self.base_name}"

    @property
    def small_key(self):
        return self.has_key

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
    LocationData(Apartment.floor_1, "1F Ledge Chest", ["Combat"], has_key=True),
    # DE415E2A-06EE-83AC-F1A3-5DCA1FA44735
    LocationData(Apartment.floor_1, "1F Rat Maze Chest", ["Combat"], has_key=True),
    LocationData(Apartment.floor_1, "1F Exterior Chest", ["Combat", "Jump Shoes"]),
    LocationData(Apartment.floor_1_top_left, "1F Couches Chest", ["Combat", "Jump Shoes"]),
    # 5B55A264-3FCD-CF38-175C-141B2D093029
    LocationData(Apartment.floor_2, "2F Rat Maze Chest", ["Combat", "Jump Shoes"], has_key=True),
    # 2BBF01C8-8267-7E71-5BD4-325001DBC0BA
    LocationData(Apartment.floor_3, "3F Gauntlet Chest", ["Combat"], has_key=True),
    LocationData(Apartment.floor_3, "Boss Chest", ["Defeat Watcher"]),
    LocationData(Beach.DEFAULT, "Dock Chest"),
    LocationData(Beach.gauntlet, "Secret Chest", ["Progressive Swap:2"]),
    LocationData(Beach.DEFAULT, "Out-of-bounds Chest", ["Progressive Swap:2"]),
    # 40DE36CF-9238-F8B0-7A57-C6C8CA465CC2
    LocationData(Bedroom.entrance, "Entrance Chest", has_key=True),
    LocationData(Bedroom.shieldy_room, "Shieldy Room Chest", []),
    LocationData(Bedroom.core, "Rock-Surrounded Chest", []),
    LocationData(Bedroom.exit, "Boss Chest", []),
    # D41F2750-E3C7-BBB4-D650-FAFC190EBD32
    LocationData(Bedroom.after_statue, "After Statue Left Chest", [], has_key=True),
    LocationData(Bedroom.after_statue, "After Statue Right Chest", []),
    # 401939A4-41BA-E07E-3BA2-DC22513DCC5C
    LocationData(Bedroom.core, "Dark Room Chest", [], has_key=True),
    LocationData(Blank.windmill, "Card Chest"),
    LocationData(Cell.DEFAULT, "Top Left Chest", ["Jump Shoes"]),
    LocationData(Cell.DEFAULT, "Chaser Gauntlet Chest", ["Progressive Swap:2", "Combat", "Jump Shoes"]),
    # 75C2D434-4AE8-BCD0-DBEB-8E6CDA67BF45
    LocationData(Circus.entry_gauntlets, "Rat Maze Chest", [], has_key=True),
    LocationData(Circus.entry_gauntlets, "Clowns Chest", []),
    LocationData(Circus.circlejump_gauntlets, "Fire Pillar Chest", []),
    # 69E8FBD6-2DA3-D25E-446F-6A59AC3E9FC2
    LocationData(Circus.entry_gauntlets, "Arthur Chest", [], has_key=True),
    # 6A95EB2F-75FD-8649-5E07-3ED37C69A9FB
    LocationData(Circus.circlejump_gauntlets, "Javiera Chest", [], has_key=True),
    # A2479A02-9B0D-751F-71A4-DB15C4982DF5
    LocationData(Circus.third_key_gauntlet, "Lion Chest", [], has_key=True),
    LocationData(Circus.north_gauntlet, "Double Clowns Chest", []),
    LocationData(Circus.boss_gauntlet, "Boss Chest", ["Defeat Servants"]),
    LocationData(Cliff.post_windmill, "Upper Chest"),
    LocationData(Cliff.post_windmill, "Lower Chest"),
    LocationData(Crowd.floor_2_gauntlets, "2F Crowded Ledge Chest",
                 ["Small Key (Mountain Cavern):4"]),
    # BE2FB96B-1D5F-FCD1-3F58-D158DB982C21
    LocationData(Crowd.floor_2, "2F Four Enemies Chest", ["Combat"], has_key=True),
    # 5743A883-D209-2518-70D7-869D14925B77
    LocationData(Crowd.floor_2_gauntlets, "2F Entrance Chest", has_key=True),
    # 21EE2D01-54FB-F145-9464-4C2CC8725EB3
    LocationData(Crowd.floor_2_gauntlets, "2F Frogs and Dog Chest", has_key=True),
    LocationData(Crowd.floor_3_center, "3F Roller Chest", []),
    LocationData(Crowd.exit, "Boss Chest", []),
    LocationData(Crowd.jump_challenge, "Extend Upgrade Chest", ["Combat", "Jump Shoes"], outside_of_dungeon=True),
    # 868736EF-EC8B-74C9-ACAB-B7BC56A44394
    LocationData(Crowd.floor_2_gauntlets, "2F Frogs and Rotators Chest", has_key=True),
    LocationData(Debug.DEFAULT, "River Puzzles Chest", ["Combat", "Jump Shoes"]),
    LocationData(Debug.DEFAULT, "Upper Prison Chest"),
    LocationData(Debug.DEFAULT, "Lower Prison Chest"),
    LocationData(Debug.DEFAULT, "Jumping Chest"),
    LocationData(Debug.DEFAULT, "Maze Chest", ["Jump Shoes"]),
    LocationData(Drawer.DEFAULT, "Game Over Chest", ["Progressive Swap:2"]),
    LocationData(Drawer.DEFAULT, "Brown Area Chest"),
    LocationData(Fields.Lake, "Island Chest", ["Combat", "Jump Shoes"]),
    LocationData(Fields.Lake, "Gauntlet Chest", ["Combat", "Jump Shoes"]),
    # Cleaning up his cave
    LocationData(Fields.Goldman, "Goldman's Cave Chest", ["Combat"]),
    LocationData(Fields.DEFAULT, "Blocked River Chest", ["Progressive Swap:2", "Jump Shoes"]),
    LocationData(Fields.DEFAULT, "Cardboard Box", ["Miao"], type=LocationType.AreaEvent),
    LocationData(Fields.DEFAULT, "Shopkeeper Trade", ["Cardboard Box"], type=LocationType.AreaEvent),
    LocationData(Fields.DEFAULT, "Mitra Trade", ["Biking Shoes"], type=LocationType.AreaEvent),
    # Hidden path
    LocationData(Fields.North_Secret_Area, f"Near {Overworld.area_name()} Secret Chest"),
    # Hidden path
    LocationData(Fields.DEFAULT, "Secluded Glen Chest", ["SwapOrSecret"]),
    # Hidden path
    # Logically, this is in Terminal, because it is separated from the rest of Fields in the same way Terminal is.
    LocationData(Fields.Terminal_Entrance, f"Near {Terminal.area_name()} Secret Chest", ["SwapOrSecret"]),
    LocationData(Forest.DEFAULT, "Inlet Chest", ["Combat"]),
    # This is the one that takes 2 hours
    LocationData(Forest.DEFAULT, "Bunny Chest", ["Progressive Swap:2"]),
    LocationData(Go.bottom, "Swap Upgrade Chest"),
    LocationData(Go.bottom, "Secret Color Puzzle Chest", ["Progressive Swap:2"]),
    # 6C8870D4-7600-6FFD-B425-2D951E65E160
    LocationData(Hotel.floor_4, "4F Annoyers Chest", ["Combat", "Jump Shoes"], has_key=True),
    LocationData(Hotel.floor_4, "4F Dust Blower Maze Chest", ["Combat", "Jump Shoes", "Small Key (Hotel):1"]),
    LocationData(Hotel.floor_3, "3F Dashers Chest", ["Small Key (Hotel):6"]),
    # 64EE884F-EA96-FB09-8A9E-F75ABDB6DC0D
    LocationData(Hotel.floor_3, "3F Gasguy Chest", ["Combat"], has_key=True),
    # 075E6024-FE2D-9C4A-1D2B-D627655FD31A
    LocationData(Hotel.floor_3, "3F Rotators Chest", ["Combat"], has_key=True),
    LocationData(Hotel.floor_2_right, "2F Dog Chest", ["Combat"]),
    # 1990B3A2-DBF8-85DA-C372-ADAFAA75744C
    LocationData(Hotel.floor_2_right, "2F Crevice Right Chest", has_key=True),
    # D2392D8D-0633-2640-09FA-4B921720BFC4
    LocationData(Hotel.floor_2, "2F Backrooms Chest", ["Combat"], has_key=True),
    # 019CBC29-3614-9302-6848-DDAEDC7C49E5
    LocationData(Hotel.floor_1, "1F Burst Flowers Chest", has_key=True),
    # 9D6FDA36-0CC6-BACC-3844-AEFB6C5C6290
    LocationData(Hotel.floor_2, "2F Crevice Left Chest", ["Jump Shoes"], has_key=True),
    LocationData(Hotel.floor_1, "Boss Chest", ["Defeat Manager"]),
    LocationData(Hotel.roof, "Roof Chest", ["Combat", "Progressive Swap:2"], outside_of_dungeon=True),
    LocationData(Nexus.top, "Isolated Chest", ["Progressive Swap:2"]),
    LocationData(Overworld.DEFAULT, "Near Gate Chest"),
    LocationData(Overworld.post_windmill, "After Temple Chest", ["Combat"]),
    LocationData(Red_Cave.top, "Top Cave Slasher Chest", ["Combat"]),
    # 72BAD10E-598F-F238-0103-60E1B36F6240
    LocationData(Red_Cave.center, "Middle Cave Right Chest", has_key=True),
    # AE87F1D5-57E0-1749-7E1E-1D0BCC1BCAB4
    LocationData(Red_Cave.center, "Middle Cave Left Chest", ["Combat"], has_key=True),
    LocationData(Red_Cave.center, "Middle Cave Middle Chest", ["Small Key (Red Grotto):6"]),
    LocationData(Red_Cave.exit, "Boss Chest", []),
    # 4A9DC50D-8739-9AD8-2CB1-82ECE29D3B6F
    LocationData(Red_Cave.left, "Left Cave Rapids Chest", ["Combat"], has_key=True),
    # A7672339-F3FB-C49E-33CE-42A49D7E4533
    LocationData(Red_Cave.right, "Right Cave Slasher Chest", ["Combat"], has_key=True),
    # 83286BFB-FFDA-237E-BA57-CA2E532E1DC7
    LocationData(Red_Cave.right, "Right Cave Four Shooter Chest", ["Combat"], has_key=True),
    # CDA1FF45-0F88-4855-B0EC-A9B42376C33F
    LocationData(Red_Cave.left, "Left Cave Sticky Chest", ["Combat"], has_key=True),
    LocationData(Red_Cave.bottom, "Widen Upgrade Chest", outside_of_dungeon=True),
    LocationData(Red_Cave.Isaac, "Isaac Dungeon Chest", ["Combat"], outside_of_dungeon=True),
    LocationData(Red_Sea.DEFAULT, "Lonely Chest"),
    LocationData(Red_Sea.DEFAULT, "Out-of-bounds Chest", ["Progressive Swap:2"]),
    LocationData(Suburb.card_house, "Stab Reward Chest"),
    LocationData(Suburb.DEFAULT, "Killers Chest", ["Combat", "Progressive Swap:2"]),
    LocationData(Space.DEFAULT, "Left Chest"),
    LocationData(Space.DEFAULT, "Right Chest"),
    LocationData(Space.Gauntlet, "Challenge Area Chest"),
    # Wiggle glitch available
    LocationData(Space.DEFAULT, "Hidden Chest"),
    # 3307AA58-CCF1-FB0D-1450-5AF0A0C458F7
    LocationData(Street.DEFAULT, "Key Chest", ["Combat"], has_key=True),
    LocationData(Street.DEFAULT, "Broom Chest"),
    LocationData(Street.DEFAULT, "Secret Chest", ["Progressive Swap:2"]),
    LocationData(Terminal.DEFAULT, "Broken Bridge Chest"),
    LocationData(Windmill.DEFAULT, "Chest", []),
    LocationData(Windmill.DEFAULT, "Activation", [], type=LocationType.AreaEvent),
    LocationData(Boss_Rush.DEFAULT, "Reward Chest"),
    # Health Cicadas
    LocationData(Apartment.floor_3, "Health Cicada", ["Defeat Watcher"], type=LocationType.Cicada),
    LocationData(Beach.gauntlet, "Health Cicada", [], type=LocationType.Cicada),
    LocationData(Bedroom.exit, "Health Cicada", ["Defeat Seer"], type=LocationType.Cicada),
    # Has to be frame 4
    LocationData(Cell.past_gate, "Health Cicada", ["Jump Shoes"], type=LocationType.Cicada),
    LocationData(Circus.boss_gauntlet, "Health Cicada", ["Defeat Servants"], type=LocationType.Cicada),
    LocationData(Crowd.floor_1, "Health Cicada", ["Defeat The Wall"], type=LocationType.Cicada),
    LocationData(Hotel.floor_1, "Health Cicada", ["Defeat Manager"], type=LocationType.Cicada),
    LocationData(Overworld.Gauntlet, "Health Cicada", [], type=LocationType.Cicada),
    LocationData(Red_Cave.top, "Health Cicada", ["Defeat Rogue"], type=LocationType.Cicada),
    LocationData(Suburb.past_gate, "Health Cicada", [], type=LocationType.Cicada),
    LocationData(Bedroom.exit, "Green Key", [], type=LocationType.BigKey),
    LocationData(Red_Cave.exit, "Red Key", [], type=LocationType.BigKey),
    LocationData(Crowd.exit, "Blue Key", [], type=LocationType.BigKey),
    LocationData(Red_Cave.center, "Middle Cave Left Tentacle", ["Combat"], type=LocationType.Tentacle),
    LocationData(Red_Cave.center, "Middle Cave Right Tentacle", [], type=LocationType.Tentacle),
    LocationData(Red_Cave.left, "Left Cave Tentacle", ["Small Key (Red Grotto):6"], type=LocationType.Tentacle),
    LocationData(Red_Cave.right, "Right Cave Tentacle", ["Small Key (Red Grotto):6"], type=LocationType.Tentacle),
    LocationData(Go.top, "Defeat Briar", ["Combat", "Jump Shoes"], type=LocationType.AreaEvent),
    # Nexus portals
    LocationData(Apartment.floor_1, "Warp Pad", type=LocationType.Nexus),
    LocationData(Beach.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Bedroom.exit, "Warp Pad", type=LocationType.Nexus),
    LocationData(Blue.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Cell.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Cliff.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Circus.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Crowd.exit, "Warp Pad", type=LocationType.Nexus),
    LocationData(Fields.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Forest.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Go.bottom, "Warp Pad", type=LocationType.Nexus),
    LocationData(Happy.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Hotel.floor_4, "Warp Pad", type=LocationType.Nexus),
    LocationData(Overworld.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Red_Cave.exit, "Warp Pad", type=LocationType.Nexus),
    LocationData(Red_Sea.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Suburb.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Space.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Terminal.DEFAULT, "Warp Pad", type=LocationType.Nexus),
    LocationData(Windmill.entrance, "Warp Pad", type=LocationType.Nexus),
    LocationData(Blue.DEFAULT, "Completion Reward", type=LocationType.AreaEvent),
    LocationData(Happy.gauntlet, "Completion Reward", type=LocationType.AreaEvent),
    # Dust locations
    LocationData(Apartment.floor_1, "1F Shortcut Room Dust 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Apartment.floor_2, "2F Switch Pillar Rat Maze Dust", ["Jump Shoes", "Small Key (Apartment):3"], type=LocationType.Dust),
    LocationData(Apartment.floor_2, "2F Dash Trap Rat Maze Dust", ["Jump Shoes", "Small Key (Apartment):3"], type=LocationType.Dust),
    LocationData(Apartment.floor_2, "2F Flooded Room Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Apartment.floor_1_top_left, "1F Couches Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Shortcut Room Dust 2", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Rat Maze Chest Dust 1", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Rat Maze Chest Dust 2", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Rat Maze Chest Dust 3", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Entrance Dust", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Flooded Room Dust", type=LocationType.Dust),
    LocationData(Apartment.floor_1, "1F Flooded Library Dust", type=LocationType.Dust),
    LocationData(Bedroom.core, "Laser Room Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Laser Room Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Room With Holes Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Room With Holes Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Past Shieldy Puzzle Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Before Boss Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.core, "Past Shieldy Puzzle Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.shieldy_room, "Shieldy Room Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.shieldy_room, "Shieldy Room Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Laser Room Dust 3", type=LocationType.Dust),
    LocationData(Bedroom.entrance, "Entrance Dust 1", type=LocationType.Dust),
    LocationData(Bedroom.entrance, "Entrance Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Before Boss Dust 2", type=LocationType.Dust),
    LocationData(Bedroom.core, "Laser Room Dust 4", type=LocationType.Dust),
    LocationData(Blue.DEFAULT, "Laser Room Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Circus.entry_gauntlets, "Dash Trap Dust", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Fire Pillars in Water Dust 3", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Lion Dust 1", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Lion Dust 2", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Fire Pillars in Water Dust 2", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Fire Pillars in Water Dust 1", type=LocationType.Dust),
    # Overlaps with Fire Pillars in Water Dust 3
    LocationData(Circus.third_key_gauntlet, "Fire Pillars in Water Dust 4", type=LocationType.Dust),
    LocationData(Circus.boss_gauntlet, "Dog Room Dust", type=LocationType.Dust),
    LocationData(Circus.circlejump_gauntlets, "Javiera Dust 2", type=LocationType.Dust),
    LocationData(Circus.circlejump_gauntlets, "Javiera Dust 1", type=LocationType.Dust),
    LocationData(Circus.past_entrance_lake, "Slime and Fire Pillar Dust", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Small Contort Room Dust", type=LocationType.Dust),
    LocationData(Circus.third_key_gauntlet, "Save Point Dust", type=LocationType.Dust),
    LocationData(Circus.entry_gauntlets, "Clown Dust 1", type=LocationType.Dust),
    LocationData(Circus.entry_gauntlets, "Clown Dust 2", type=LocationType.Dust),
    LocationData(Circus.boss_gauntlet, "Spike Dust", type=LocationType.Dust),
    LocationData(Circus.entrance_lake, "Dash Pad over Hole Dust", type=LocationType.Dust),
    LocationData(Circus.past_entrance_lake, "Lion and Dash Pad Dust", type=LocationType.Dust),
    LocationData(Circus.entrance_lake, "Spike Roller in Water Dust", type=LocationType.Dust),
    LocationData(Circus.DEFAULT, "Entrance Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_3, "3F Top Center Moving Platform Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_3, "3F Top Right Moving Platform Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Crowd.floor_3_center, "3F Roller Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Frogs and Annoyers Dust", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Rotators and Annoyers Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Rotators and Annoyers Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Circular Hole Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Circular Hole Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Crossing Moving Platforms Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Crossing Moving Platforms Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Moving Platform Crossroad Dust 1", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Moving Platform Crossroad Dust 2", type=LocationType.Dust),
    LocationData(Crowd.floor_2_gauntlets, "2F Moving Platform Crossroad Dust 3", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Moving Platform Dust", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Whirlpool Room Dust 1", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Whirlpool Room Dust 2", type=LocationType.Dust),
    LocationData(Debug.DEFAULT, "Sound Test Console Dust", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 1", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 2", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 3", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 4", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 5", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 6", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 7", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 8", type=LocationType.Dust),
    LocationData(Fields.Goldman, "Goldman's Cave Dust 9", type=LocationType.Dust),
    LocationData(Fields.Lake, "Lake After Spikes Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "North River Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Lake After Holes Floating Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "South East of Lake Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Lake Near Windmill Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "North of Lake Rapids Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "North East of Lake Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Before Annoyer Maze Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Mitra House Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Near Red Gate Dust", type=LocationType.Dust),
    LocationData(Fields.Past_Gate, "After Red Gate Dust", type=LocationType.Dust),
    LocationData(Fields.Terminal_Entrance, "Near Terminal Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "North West of Lake Dust", type=LocationType.Dust),
    LocationData(Fields.DEFAULT, "Near Beach Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "South West Corner Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "South East of Gauntlet Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Before Gauntlet Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Island Chest Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Island Start Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Post Whirlpool Dust", type=LocationType.Dust),
    LocationData(Fields.Lake, "Olive Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Relaxation Pond Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Near Cliff Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Floating Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Thorax Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Carved Rock Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Tiny Island Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Inlet Dust", type=LocationType.Dust),
    LocationData(Forest.DEFAULT, "Before Inlet Chest Dust", type=LocationType.Dust),
    LocationData(Happy.gauntlet, "Final Room Dust", [], type=LocationType.Dust),
    LocationData(Happy.gauntlet, "Dustmaid Dust", [], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Floating Dustmaid Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "3F Hallway Dustmaid Dust 2", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "3F Hallway Dustmaid Dust 1", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Moving Platform Crossroad 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Boss Dust", ["Small Key (Hotel):6","Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Gasguy Dust", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Dustmaid and Steampipe Dust 3", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Dustmaid and Steampipe Dust 2", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Dustmaid and Steampipe Dust 1", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Dustmaid and Steampipe Dust 4", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "2F Steampipe Dust 2", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "2F Steampipe Dust 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_1, "1F Locked Dust", ["Small Key (Hotel):6", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "2F Dustmaid and Steampipe Dust 3", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "2F Dustmaid and Steampipe Dust 1", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "2F Dustmaid and Steampipe Dust 2", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_2, "2F Dustmaid Hallway Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "3F Stream Dustmaid Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_3, "3F Bedroom Dust", ["Small Key (Hotel):4", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Slime Dust 2", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Slime Dust 1", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Moving Platform Crossroad 2", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Dustmaid Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Near Elevator Dust", ["Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Spring Puzzle Dust", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Hotel.floor_4, "4F Moving Platform Puzzle Dust", ["Small Key (Hotel):1", "Jump Shoes"], type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Boss Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Boss Dust 2", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Before Boss Dust", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Slasher Dust", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Before Slasher Dust", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Boss Dust 3", type=LocationType.Dust),
    LocationData(Red_Cave.top, "Top Cave Boss Dust 4", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Left Cave Rapids Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Left Cave Rapids Dust 2", type=LocationType.Dust),
    LocationData(Red_Cave.right, "Right Cave Before Slasher Dust", type=LocationType.Dust),
    LocationData(Red_Cave.right, "Right Cave Whirlpool Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Left Cave Whirlpool Dust 1", type=LocationType.Dust),
    LocationData(Red_Cave.left, "Left Cave Whirlpool Dust 2", type=LocationType.Dust),
    LocationData(Red_Cave.right, "Right Cave Whirlpool Dust 2", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Challenge Area Dustmaid Dust 1", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Challenge Area Dustmaid Dust 2", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Challenge Area Lion Dust 1", type=LocationType.Dust),
    LocationData(Space.Gauntlet, "Challenge Area Lion Dust 2", type=LocationType.Dust),
    LocationData(Street.DEFAULT, "After Bridge Dust 1", ["Small Key (Street):1"], type=LocationType.Dust),
    LocationData(Street.DEFAULT, "After Bridge Dust 2", ["Small Key (Street):1"], type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Before Red Boss Dust", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Red Boss Dust 1", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Red Boss Dust 2", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Red Boss Dust 3", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Red Boss Dust 4", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Manager Phase 1 Dust", type=LocationType.Dust),
    LocationData(Boss_Rush.DEFAULT, "Manager Phase 2 Dust", type=LocationType.Dust)
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
