from typing import NamedTuple, List, Dict

from . import Regions


class LocationData(NamedTuple):
    name: str
    region_name: str
    reqs: List[str] = []
    health_cicada: bool = False
    small_key: bool = False
    big_key: bool = False
    tentacle: bool = False
    nexus_gate: bool = False
    dust: bool = False

    def postgame(self):
        return "Swap:2" in self.reqs or self.region_name in Regions.postgame_regions


# This array must maintain a consistent order because the IDs are generated from it.
all_locations: List[LocationData] = [
    # 0AC41F72-EE1D-0D32-8F5D-8F25796B6396
    LocationData("Apartment - 1F Ledge Chest", "Apartment floor 1", ["Combat", "Jump Shoes"], small_key=True),
    # DE415E2A-06EE-83AC-F1A3-5DCA1FA44735
    LocationData("Apartment - 1F Rat Maze Chest", "Apartment floor 1", ["Combat", "Jump Shoes"], small_key=True),
    LocationData("Apartment - 1F Exterior Chest", "Apartment floor 1", ["Combat", "Jump Shoes"]),
    LocationData("Apartment - 1F Couches Chest", "Apartment floor 1 top left", ["Combat", "Jump Shoes"]),
    # 5B55A264-3FCD-CF38-175C-141B2D093029
    LocationData("Apartment - 2F Rat Maze Chest", "Apartment floor 2", ["Combat", "Jump Shoes"], small_key=True),
    # 2BBF01C8-8267-7E71-5BD4-325001DBC0BA
    LocationData("Apartment - 3F Gauntlet Chest", "Apartment floor 3", ["Combat"], small_key=True),
    LocationData("Apartment - Boss Chest", "Apartment floor 3", ["Defeat Watcher"]),
    LocationData("Beach - Dock Chest", "Beach"),
    LocationData("Beach - Secret Chest", "Beach", ["Swap:2", "Cards:8", "Combat"]),
    LocationData("Beach - Out-of-bounds Chest", "Beach", ["Swap:2"]),
    # 40DE36CF-9238-F8B0-7A57-C6C8CA465CC2
    LocationData("Temple of the Seeing One - Entrance Chest", "Bedroom", small_key=True),
    LocationData("Temple of the Seeing One - Shieldy Room Chest", "Bedroom",
                 ["Combat", "Keys:Temple of the Seeing One:3"]),
    LocationData("Temple of the Seeing One - Rock-Surrounded Chest", "Bedroom", ["Combat"]),
    LocationData("Temple of the Seeing One - Boss Chest", "Bedroom exit", []),
    # D41F2750-E3C7-BBB4-D650-FAFC190EBD32
    LocationData("Temple of the Seeing One - After Statue Left Chest", "Bedroom exit",
                 ["Combat", "Temple of the Seeing One Statue"], small_key=True),
    LocationData("Temple of the Seeing One - After Statue Right Chest", "Bedroom exit",
                 ["Combat", "Temple of the Seeing One Statue"]),
    # 401939A4-41BA-E07E-3BA2-DC22513DCC5C
    LocationData("Temple of the Seeing One - Dark Room Chest", "Bedroom", ["Combat"], small_key=True),
    LocationData("Blank - Card Chest", "Blank windmill"),
    LocationData("Cell - Top Left Chest", "Cell", ["Jump Shoes"]),
    LocationData("Cell - Chaser Gauntlet Chest", "Cell", ["Swap:2", "Combat", "Jump Shoes"]),
    # 75C2D434-4AE8-BCD0-DBEB-8E6CDA67BF45
    LocationData("Circus - Rat Maze Chest", "Circus", ["Combat", "Jump Shoes"], small_key=True),
    LocationData("Circus - Clowns Chest", "Circus", ["Combat", "Jump Shoes"]),
    LocationData("Circus - Fire Pillar Chest", "Circus 2", ["Combat", "Jump Shoes"]),
    # 69E8FBD6-2DA3-D25E-446F-6A59AC3E9FC2
    LocationData("Circus - Arthur Chest", "Circus", ["Combat", "Jump Shoes"], small_key=True),
    # 6A95EB2F-75FD-8649-5E07-3ED37C69A9FB
    LocationData("Circus - Javiera Chest", "Circus 2", ["Combat", "Jump Shoes"], small_key=True),
    # A2479A02-9B0D-751F-71A4-DB15C4982DF5
    LocationData("Circus - Lion Chest", "Circus 3", ["Combat", "Jump Shoes"], small_key=True),
    LocationData("Circus - Double Clowns Chest", "Circus 4", ["Combat", "Jump Shoes", "Keys:Circus:4"]),
    LocationData("Circus - Boss Chest", "Circus 4", ["Defeat Servants", "Combat", "Jump Shoes"]),
    LocationData("Cliffs - Upper Chest", "Cliff post windmill"),
    LocationData("Cliffs - Lower Chest", "Cliff post windmill"),
    LocationData("Mountain Cavern - 2F Crowded Ledge Chest", "Crowd floor 2",
                 ["Combat", "Jump Shoes", "Keys:Mountain Cavern:4"]),
    # BE2FB96B-1D5F-FCD1-3F58-D158DB982C21
    LocationData("Mountain Cavern - 2F Four Enemies Chest", "Crowd floor 2", ["Combat"], small_key=True),
    # 5743A883-D209-2518-70D7-869D14925B77
    LocationData("Mountain Cavern - 2F Entrance Chest", "Crowd floor 2", ["Combat", "Jump Shoes"], small_key=True),
    # 21EE2D01-54FB-F145-9464-4C2CC8725EB3
    LocationData("Mountain Cavern - 2F Frogs and Dog Chest", "Crowd floor 2", ["Combat", "Jump Shoes"], small_key=True),
    LocationData("Mountain Cavern - 3F Roller Chest", "Crowd floor 3",
                 ["Combat", "Jump Shoes", "Keys:Mountain Cavern:4"]),
    LocationData("Mountain Cavern - Boss Chest", "Crowd exit", []),
    LocationData("Mountain Cavern - Extend Upgrade Chest", "Crowd jump challenge", ["Combat", "Jump Shoes"]),
    # 868736EF-EC8B-74C9-ACAB-B7BC56A44394
    LocationData("Mountain Cavern - 2F Frogs and Rotators Chest", "Crowd floor 2", ["Combat", "Jump Shoes"],
                 small_key=True),
    LocationData("Debug - River Puzzles Chest", "Debug", ["Combat", "Jump Shoes"]),
    LocationData("Debug - Upper Prison Chest", "Debug"),
    LocationData("Debug - Lower Prison Chest", "Debug"),
    LocationData("Debug - Jumping Chest", "Debug"),
    LocationData("Debug - Maze Chest", "Debug", ["Jump Shoes"]),
    LocationData("Drawer - Game Over Chest", "Drawer", ["Swap:2"]),
    LocationData("Drawer - Brown Area Chest", "Drawer"),
    LocationData("Fields - Island Chest", "Fields", ["Combat", "Jump Shoes"]),
    LocationData("Fields - Gauntlet Chest", "Fields", ["Combat", "Jump Shoes"]),
    LocationData("Fields - Goldman's Cave Chest", "Fields", ["Combat"]),
    LocationData("Fields - Blocked River Chest", "Fields", ["Swap:2", "Jump Shoes"]),
    LocationData("Fields - Cardboard Box", "Fields"),
    LocationData("Fields - Shopkeeper Trade", "Fields", ["Cardboard Box"]),
    LocationData("Fields - Mitra Trade", "Fields", ["Biking Shoes"]),
    # Hidden path
    LocationData("Fields - Near Overworld Secret Chest", "Fields", ["Swap:2"]),
    # Hidden path
    LocationData("Fields - Secluded Glen Chest", "Fields", ["Swap:2"]),
    # Hidden path
    # Logically, this is in Terminal, because it is separated from the rest of Fields in the same way Terminal is.
    LocationData("Fields - Near Terminal Secret Chest", "Terminal", ["Swap:2"]),
    LocationData("Deep Forest - Inlet Chest", "Forest", ["Combat"]),
    # This is the one that takes 2 hours
    LocationData("Deep Forest - Bunny Chest", "Forest", ["Swap:2"]),
    LocationData("GO - Swap Upgrade Chest", "Go bottom"),
    LocationData("GO - Secret Color Puzzle Chest", "Go bottom", ["Swap:2"]),
    # 6C8870D4-7600-6FFD-B425-2D951E65E160
    LocationData("Hotel - 4F Annoyers Chest", "Hotel floor 4", ["Combat", "Jump Shoes"], small_key=True),
    LocationData("Hotel - 4F Dust Blower Maze Chest", "Hotel floor 4", ["Combat", "Jump Shoes", "Keys:Hotel:1"]),
    LocationData("Hotel - 3F Dashers Chest", "Hotel floor 3", ["Keys:Hotel:6"]),
    # 64EE884F-EA96-FB09-8A9E-F75ABDB6DC0D
    LocationData("Hotel - 3F Gasguy Chest", "Hotel floor 3", ["Combat"], small_key=True),
    # 075E6024-FE2D-9C4A-1D2B-D627655FD31A
    LocationData("Hotel - 3F Rotators Chest", "Hotel floor 3", ["Combat"], small_key=True),
    LocationData("Hotel - 2F Dog Chest", "Hotel floor 2 right", ["Combat"]),
    # 1990B3A2-DBF8-85DA-C372-ADAFAA75744C
    LocationData("Hotel - 2F Crevice Right Chest", "Hotel floor 2 right", small_key=True),
    # D2392D8D-0633-2640-09FA-4B921720BFC4
    LocationData("Hotel - 2F Backrooms Chest", "Hotel floor 2", ["Combat"], small_key=True),
    # 019CBC29-3614-9302-6848-DDAEDC7C49E5
    LocationData("Hotel - 1F Burst Flowers Chest", "Hotel floor 1", small_key=True),
    # 9D6FDA36-0CC6-BACC-3844-AEFB6C5C6290
    LocationData("Hotel - 2F Crevice Left Chest", "Hotel floor 2", ["Jump Shoes"], small_key=True),
    LocationData("Hotel - Boss Chest", "Hotel floor 1", ["Defeat Manager"]),
    LocationData("Hotel - Roof Chest", "Hotel roof", ["Swap:2"]),
    LocationData("Nexus - Isolated Chest", "Nexus top", ["Swap:2"]),
    LocationData("Overworld - Near Gate Chest", "Overworld"),
    LocationData("Overworld - After Temple Chest", "Overworld post windmill", ["Combat"]),
    LocationData("Red Cave - Top Cave Slasher Chest", "Red Cave top", ["Combat"]),
    # 72BAD10E-598F-F238-0103-60E1B36F6240
    LocationData("Red Cave - Middle Cave Right Chest", "Red Cave center", small_key=True),
    # AE87F1D5-57E0-1749-7E1E-1D0BCC1BCAB4
    LocationData("Red Cave - Middle Cave Left Chest", "Red Cave center", ["Combat"], small_key=True),
    LocationData("Red Cave - Middle Cave Middle Chest", "Red Cave center", ["Keys:Red Cave:6"]),
    LocationData("Red Cave - Boss Chest", "Red Cave exit", []),
    # 4A9DC50D-8739-9AD8-2CB1-82ECE29D3B6F
    LocationData("Red Cave - Left Cave Rapids Chest", "Red Cave left", ["Combat"], small_key=True),
    # A7672339-F3FB-C49E-33CE-42A49D7E4533
    LocationData("Red Cave - Right Cave Slasher Chest", "Red Cave right", small_key=True),
    # 83286BFB-FFDA-237E-BA57-CA2E532E1DC7
    LocationData("Red Cave - Right Cave Four Shooter Chest", "Red Cave right", small_key=True),
    # CDA1FF45-0F88-4855-B0EC-A9B42376C33F
    LocationData("Red Cave - Left Cave Sticky Chest", "Red Cave left", ["Combat"], small_key=True),
    LocationData("Red Cave - Widen Upgrade Chest", "Red Cave bottom"),
    LocationData("Red Cave - Isaac Dungeon Chest", "Red Cave Isaac", ["Combat"]),
    LocationData("Red Sea - Lonely Chest", "Red Sea"),
    LocationData("Red Sea - Out-of-bounds Chest", "Red Sea", ["Swap:2"]),
    LocationData("Young Town - Stab Reward Chest", "Suburb card house"),
    LocationData("Young Town - Killers Chest", "Suburb", ["Combat", "Swap:2"]),
    LocationData("Space - Left Chest", "Space"),
    LocationData("Space - Right Chest", "Space"),
    LocationData("Space - Challenge Area Chest", "Space", ["Combat", "Jump Shoes", "Swap:2"]),
    # Wiggle glitch available
    LocationData("Space - Hidden Chest", "Space"),
    # 3307AA58-CCF1-FB0D-1450-5AF0A0C458F7
    LocationData("Street - Key Chest", "Street", ["Combat"], small_key=True),
    LocationData("Street - Broom Chest", "Street"),
    LocationData("Street - Secret Chest", "Street", ["Swap:2"]),
    LocationData("Terminal - Broken Bridge Chest", "Terminal"),
    LocationData("Windmill - Chest", "Windmill", []),
    LocationData("Windmill - Activation", "Windmill", []),
    LocationData("Boss Rush - Reward Chest", "Boss Rush", ["Combat"]),
    # Health Cicadas
    LocationData("Apartment - Health Cicada", "Apartment floor 3", ["Defeat Watcher"], health_cicada=True),
    LocationData("Beach - Health Cicada", "Beach", ["Cards:8", "Combat"], health_cicada=True),
    LocationData("Temple of the Seeing One - Health Cicada", "Bedroom exit", ["Combat"], health_cicada=True),
    # Has to be frame 4
    LocationData("Cell - Health Cicada", "Cell", ["Cards:24"], health_cicada=True),
    LocationData("Circus - Health Cicada", "Circus 4", ["Defeat Servants"], health_cicada=True),
    LocationData("Mountain Cavern - Health Cicada", "Crowd floor 1", ["Defeat The Wall"], health_cicada=True),
    LocationData("Hotel - Health Cicada", "Hotel floor 1", ["Defeat Manager"], health_cicada=True),
    LocationData("Overworld - Health Cicada", "Overworld", ["Combat", "Cards:4"], health_cicada=True),
    LocationData("Red Cave - Health Cicada", "Red Cave top", ["Defeat Rogue"], health_cicada=True),
    LocationData("Young Town - Health Cicada", "Suburb", ["Combat", "Cards:16"], health_cicada=True),
    LocationData("Temple of the Seeing One - Green Key", "Bedroom exit", [], big_key=True),
    LocationData("Red Cave - Red Key", "Red Cave exit", [], big_key=True),
    LocationData("Mountain Cavern - Blue Key", "Crowd exit", [], big_key=True),
    LocationData("Red Cave - Middle Cave Left Tentacle", "Red Cave center", ["Combat"], tentacle=True),
    LocationData("Red Cave - Middle Cave Right Tentacle", "Red Cave center", ["Combat"], tentacle=True),
    LocationData("Red Cave - Left Cave Tentacle", "Red Cave left", ["Combat", "Keys:Red Cave:6"], tentacle=True),
    LocationData("Red Cave - Right Cave Tentacle", "Red Cave right", ["Combat", "Keys:Red Cave:6"], tentacle=True),
    LocationData("GO - Defeat Briar", "Go top", ["Combat", "Jump Shoes"]),
    # Nexus portals
    LocationData("Apartment - Warp Pad", "Apartment floor 1", nexus_gate=True),
    LocationData("Beach - Warp Pad", "Beach", nexus_gate=True),
    LocationData("Temple of the Seeing One - Warp Pad", "Bedroom exit", nexus_gate=True),
    LocationData("Blue - Warp Pad", "Blue", nexus_gate=True),
    LocationData("Cell - Warp Pad", "Cell", nexus_gate=True),
    LocationData("Cliffs - Warp Pad", "Cliff", nexus_gate=True),
    LocationData("Circus - Warp Pad", "Circus", nexus_gate=True),
    LocationData("Mountain Cavern - Warp Pad", "Crowd exit", nexus_gate=True),
    LocationData("Fields - Warp Pad", "Fields", nexus_gate=True),
    LocationData("Deep Forest - Warp Pad", "Forest", nexus_gate=True),
    LocationData("GO - Warp Pad", "Go bottom", nexus_gate=True),
    LocationData("Happy - Warp Pad", "Happy", nexus_gate=True),
    LocationData("Hotel - Warp Pad", "Hotel floor 4", nexus_gate=True),
    LocationData("Overworld - Warp Pad", "Overworld", nexus_gate=True),
    LocationData("Red Cave - Warp Pad", "Red Cave exit", nexus_gate=True),
    LocationData("Red Sea - Warp Pad", "Red Sea", nexus_gate=True),
    LocationData("Young Town - Warp Pad", "Suburb", nexus_gate=True),
    LocationData("Space - Warp Pad", "Space", nexus_gate=True),
    LocationData("Terminal - Warp Pad", "Terminal", nexus_gate=True),
    LocationData("Windmill - Warp Pad", "Windmill entrance", nexus_gate=True),
    # Dust locations
    LocationData("FA17F386-6A05-753A-1D7B-48B86645E69A - Apartment - x2 y2 0", "Apartment", dust=True),
    LocationData("D5383B50-30D9-AE32-AED2-24FE60368343 - Apartment - x5 y2 0", "Apartment", dust=True),
    LocationData("24F65D09-1CD3-1473-394D-FA61E6DAEAA7 - Apartment - x6 y2 0", "Apartment", dust=True),
    LocationData("E256B8DC-B00C-ACD8-423B-C67BC89A94EC - Apartment - x7 y3 0", "Apartment", dust=True),
    LocationData("9E5A4474-CE96-4F90-8B84-064C87C8541E - Apartment - x0 y0 0", "Apartment", dust=True),
    LocationData("DF3B2868-82EF-E2FD-9E61-B12867924540 - Apartment - x2 y2 1", "Apartment", dust=True),
    LocationData("A3D71CCC-B916-CA23-2A49-FF391CBCBB2F - Apartment - x0 y2 0", "Apartment", dust=True),
    LocationData("05A70FFA-5D0F-12E4-70E0-1B786535273B - Apartment - x0 y2 1", "Apartment", dust=True),
    LocationData("393332EB-E825-5FEB-043E-D406A28B6054 - Apartment - x0 y2 2", "Apartment", dust=True),
    LocationData("D2B44430-5B0C-3D8A-079B-F06DAB1CBDB9 - Apartment - x2 y5 0", "Apartment", dust=True),
    LocationData("9D700111-9B21-1989-B91F-AE383AC7BF8E - Apartment - x1 y3 0", "Apartment", dust=True),
    LocationData("F38982B7-5605-D1A8-A83F-D16E1CE2A519 - Apartment - x2 y1 0", "Apartment", dust=True),
    LocationData("44BDEF07-0647-E8B1-7342-A67617A8228B - Bedroom - x2 y3 0", "Bedroom", dust=True),
    LocationData("993C6C71-7140-4DC1-7C2A-13B0ED4357AA - Bedroom - x2 y3 1", "Bedroom", dust=True),
    LocationData("BC6A6606-05CE-C0ED-A6A2-43317C193D98 - Bedroom - x1 y2 0", "Bedroom", dust=True),
    LocationData("ECD716CE-2A94-7AE1-EB5A-7D88833AB4DD - Bedroom - x1 y2 1", "Bedroom", dust=True),
    LocationData("62324F0F-58EB-11A8-1BFE-8637643E0E3B - Bedroom - x1 y1 0", "Bedroom", dust=True),
    LocationData("0CAE2D8D-7C18-240F-E1BA-CFF1ECBD244E - Bedroom - x2 y1 0", "Bedroom", dust=True),
    LocationData("219440C1-CC31-C6A5-E304-242979F548DC - Bedroom - x1 y1 1", "Bedroom", dust=True),
    LocationData("66A6C7E7-2874-FE6B-AA81-3B1E1CABB687 - Bedroom - x1 y0 0", "Bedroom", dust=True),
    LocationData("8655FDD7-4D82-B727-CF9F-EBB72DD1759A - Bedroom - x1 y0 1", "Bedroom", dust=True),
    LocationData("61B1812F-ACC7-6B51-7123-BA711F9FFEC0 - Bedroom - x2 y3 2", "Bedroom", dust=True),
    LocationData("B2572A3F-1C5C-7A67-E09E-9A990FC19723 - Bedroom - x2 y4 0", "Bedroom", dust=True),
    LocationData("92A5DD40-8013-4679-F45D-2CBA02AF13CB - Bedroom - x2 y4 1", "Bedroom", dust=True),
    LocationData("8E069325-4584-D2FD-B474-2F33969DF446 - Bedroom - x2 y1 1", "Bedroom", dust=True),
    LocationData("75DC2B48-F865-89C1-1431-02696938D51F - Bedroom - x2 y3 3", "Bedroom", dust=True),
    LocationData("2AB83B94-9C29-EC42-EAD7-9136E2B3C4C0 - Blue - x2 y0 0", "Blue", dust=True),
    LocationData("414E5354-369F-DA51-1802-23F5BDD26A81 - Circus - x6 y7 0", "Circus", dust=True),
    LocationData("FABFC3D7-E83E-B806-1183-B98B6A6DF4F5 - Circus - x2 y3 0", "Circus", dust=True),
    LocationData("6232C7FC-18D0-89E7-32C0-A9CB554779F3 - Circus - x1 y2 0", "Circus", dust=True),
    LocationData("A3D94AC2-2906-372A-6761-C9BCE3FA880D - Circus - x1 y2 1", "Circus", dust=True),
    LocationData("31B1FBCC-7FDD-3121-A2E2-E3A57524E309 - Circus - x2 y3 1", "Circus", dust=True),
    LocationData("120618BF-7FBA-F71F-9E45-D00881B4E862 - Circus - x2 y3 2", "Circus", dust=True),
    LocationData("498FEC67-EBFD-8C38-8AC7-E1A48440BD25 - Circus - x2 y3 3", "Circus", dust=True),
    LocationData("74F1B388-5DAF-562A-113A-3310029E414E - Circus - x5 y0 0", "Circus", dust=True),
    LocationData("C263283A-4B91-BC78-CAB6-F3D1A7D99BB9 - Circus - x7 y2 0", "Circus", dust=True),
    LocationData("8DA2F9C9-99C1-8126-FD81-F8794573961D - Circus - x7 y2 1", "Circus", dust=True),
    LocationData("9313FC86-62B0-ED23-6113-5A83C334C9FF - Circus - x4 y6 0", "Circus", dust=True),
    LocationData("8E8DB510-147D-1FCD-5B56-F1E7B255981F - Circus - x3 y3 0", "Circus", dust=True),
    LocationData("E83C3E71-35D3-153F-8E68-4859B80E59A4 - Circus - x4 y3 0", "Circus", dust=True),
    LocationData("75F7A272-605E-083A-86FB-7E7BBF02FC96 - Circus - x0 y3 0", "Circus", dust=True),
    LocationData("5059933D-D290-D841-65AA-7E008EFCC355 - Circus - x0 y3 1", "Circus", dust=True),
    LocationData("9F23404B-E9E0-F73F-53E5-BF9AE63309A1 - Circus - x5 y2 0", "Circus", dust=True),
    LocationData("A89177DC-50DA-E9D0-0D45-873D8CA48633 - Circus - x3 y7 0", "Circus", dust=True),
    LocationData("E2D19ACC-E0D4-55E2-4B1C-F13D109AFCD8 - Circus - x4 y5 0", "Circus", dust=True),
    LocationData("A653DCCF-7FC7-5486-771D-23A73AF61952 - Circus - x5 y7 0", "Circus", dust=True),
    LocationData("AF299594-BAE1-B7C8-363B-6074BD1F5005 - Circus - x4 y8 0", "Circus", dust=True),
    LocationData("59B8EF80-69BE-A404-AF61-08BC14CBE674 - Crowd - x8 y0 0", "Crowd", dust=True),
    LocationData("DA9203DA-70AA-BDE7-DBC6-CF9EB6D461E9 - Crowd - x9 y0 0", "Crowd", dust=True),
    LocationData("C2107822-25BF-D155-79A6-00BFEF76045F - Crowd - x8 y2 0", "Crowd", dust=True),
    LocationData("C31BDF08-0697-527E-D68F-4B4EA0DEB6B3 - Crowd - x0 y4 0", "Crowd", dust=True),
    LocationData("0F166EEC-4C61-4EF5-7231-AFD54735B24F - Crowd - x1 y4 0", "Crowd", dust=True),
    LocationData("4CAD8FDE-9BF2-C4BE-C1D4-AE9E16DE59BD - Crowd - x1 y4 1", "Crowd", dust=True),
    LocationData("317DB5F2-1509-EE35-F75B-F61B254F2250 - Crowd - x1 y6 0", "Crowd", dust=True),
    LocationData("3B756C9A-7EE8-A3DA-E950-AA265DC6353D - Crowd - x1 y6 1", "Crowd", dust=True),
    LocationData("D5DAA6F5-5895-6E50-9820-33EBBA2965E1 - Crowd - x2 y7 0", "Crowd", dust=True),
    LocationData("F1602995-153C-9BB8-C966-29C75974336B - Crowd - x2 y7 1", "Crowd", dust=True),
    LocationData("8E20D277-66A1-61DA-678D-E61B83C7859A - Crowd - x2 y6 0", "Crowd", dust=True),
    LocationData("3F1AD173-898D-C704-53E8-858BB5B78193 - Crowd - x2 y6 1", "Crowd", dust=True),
    LocationData("2B93F260-093B-952C-4658-25E208AFB22A - Crowd - x2 y6 2", "Crowd", dust=True),
    LocationData("6ADD7466-6803-CD36-0EE3-2979CEAA170E - Debug - x0 y2 0", "Debug", dust=True),
    LocationData("33922F3B-10C2-DC74-E6F6-05E1D60A6CA2 - Debug - x1 y1 0", "Debug", dust=True),
    LocationData("9EF6A9D3-E50C-A183-8796-8F53E311BD8F - Debug - x1 y1 1", "Debug", dust=True),
    LocationData("283A0D5A-5A70-908D-141B-9CA39180EDFF - Debug - x0 y1 0", "Debug", dust=True),
    LocationData("1E845E26-D476-FF93-61B3-CC89463FF738 - Fields - x8 y0 0", "Fields", dust=True),
    LocationData("98B8FEBF-B06F-1E90-318D-DF3E2EA88A19 - Fields - x8 y0 1", "Fields", dust=True),
    LocationData("FE9D233B-CFA4-CB18-5A67-63B1F092C590 - Fields - x8 y0 2", "Fields", dust=True),
    LocationData("28107DB7-B684-D461-D5DF-DD40873F9D42 - Fields - x8 y0 3", "Fields", dust=True),
    LocationData("771B4080-E5CB-3487-9F5A-1A0CC537FE64 - Fields - x8 y0 4", "Fields", dust=True),
    LocationData("547E5C39-58F6-985E-AD2C-99F74FB919AE - Fields - x8 y0 5", "Fields", dust=True),
    LocationData("02D1ABD5-DB79-F2E9-FDD4-D75A6CFEE751 - Fields - x8 y0 6", "Fields", dust=True),
    LocationData("B68415E6-F903-1B03-50FF-73FABA7A459B - Fields - x8 y0 7", "Fields", dust=True),
    LocationData("138DB5DB-3AA7-6C29-7E00-4BBBC3DD78F4 - Fields - x8 y0 8", "Fields", dust=True),
    LocationData("03446283-6AD1-23CE-1F25-E85BAB29B92F - Fields - x7 y6 0", "Fields", dust=True),
    LocationData("9D8DEB23-8816-DE83-C6C9-4A90986FDF7B - Fields - x6 y1 0", "Fields", dust=True),
    LocationData("49652D76-C1F3-DB10-1434-3D8520DB2341 - Fields - x7 y10 0", "Fields", dust=True),
    LocationData("F1006611-4ECA-F11F-5962-F2621ADC744F - Fields - x8 y9 0", "Fields", dust=True),
    LocationData("CD4FD2BC-66C4-F340-CC4B-4C6D2B85299A - Fields - x8 y8 0", "Fields", dust=True),
    LocationData("A6E6F221-89F4-D90D-B66E-E7F8D328504B - Fields - x5 y5 0", "Fields", dust=True),
    LocationData("262BD5DE-597B-F499-4AD1-D64C297DF6B4 - Fields - x7 y5 0", "Fields", dust=True),
    LocationData("8D861C7E-E458-6567-E394-35A24E182992 - Fields - x8 y3 0", "Fields", dust=True),
    LocationData("818F2D0B-154E-19D2-A8AE-300C80A46F82 - Fields - x5 y4 0", "Fields", dust=True),
    LocationData("3BBC852E-4EB3-B89D-6A2E-63F571F841E0 - Fields - x4 y5 0", "Fields", dust=True),
    LocationData("BDCB0312-3588-EB5E-9CF3-1168B36462AE - Fields - x3 y3 0", "Fields", dust=True),
    LocationData("ECFA3601-89D4-26C8-3657-74E751E5E2E4 - Fields - x1 y1 0", "Fields", dust=True),
    LocationData("F9F89787-1EFD-9470-02DE-E4F715C4D3E7 - Fields - x2 y5 0", "Fields", dust=True),
    LocationData("A4E151EE-6F7F-02D0-3576-2180271E4337 - Fields - x1 y5 0", "Fields", dust=True),
    LocationData("E9C0D471-BE46-E46F-5A22-2CDAFACFBE11 - Fields - x1 y10 0", "Fields", dust=True),
    LocationData("95B54199-32BA-6C94-5B68-43E02F784A8A - Fields - x3 y9 0", "Fields", dust=True),
    LocationData("78116EE5-3B5A-9A17-771C-10E6B4B0388B - Fields - x1 y8 0", "Fields", dust=True),
    LocationData("14D4014A-3840-F929-E4AE-F5845360423A - Fields - x6 y9 0", "Fields", dust=True),
    LocationData("8DF14084-EE87-CE16-6032-FD76DDBE132D - Fields - x5 y9 0", "Fields", dust=True),
    LocationData("9A77A412-E1E4-59CA-1FFC-D54E11579D6F - Fields - x6 y7 0", "Fields", dust=True),
    LocationData("4D18EF22-1655-E1C4-AA10-B47FDD3913C7 - Fields - x6 y7 1", "Fields", dust=True),
    LocationData("49BEBA57-9CE3-C985-5FF8-1F2FEF22AD79 - Forest - x2 y4 0", "Forest", dust=True),
    LocationData("49E5AE8A-80E3-73C0-2446-83D5B5B7B10F - Forest - x4 y7 0", "Forest", dust=True),
    LocationData("0ED1BBDB-CDAF-D23A-64EC-4A0FD8945FCE - Forest - x1 y7 0", "Forest", dust=True),
    LocationData("41E21873-0C8F-90A9-A6F4-AA119789113E - Forest - x0 y7 0", "Forest", dust=True),
    LocationData("80AFB0D2-57EF-FBC2-BF4A-9D8374FB7E92 - Forest - x0 y8 0", "Forest", dust=True),
    LocationData("C14D443C-9D38-679C-6891-1B287158C8FB - Forest - x1 y8 0", "Forest", dust=True),
    LocationData("FFBBA484-BE29-91B5-A316-92E8889FA558 - Forest - x3 y2 0", "Forest", dust=True),
    LocationData("39207086-C6BB-7F4B-C92B-D3A7C9AF86B8 - Forest - x3 y4 0", "Forest", dust=True),
    LocationData("4D1270E6-CF70-4402-3125-89FB4F867DF3 - Happy - x3 y1 0", "Happy", dust=True),
    LocationData("8A4107F4-95D0-4104-7632-17E22ABB11F8 - Happy - x1 y0 0", "Happy", dust=True),
    LocationData("C42A7D33-88B6-69A7-B4C8-787A9217E170 - Hotel - x8 y5 0", "Hotel", dust=True),
    LocationData("AE8E7D0B-356E-8475-48AC-577611F5016D - Hotel - x2 y8 0", "Hotel", dust=True),
    LocationData("FA3CDCFE-1A26-B57F-02A4-EF4C2EA0B0E9 - Hotel - x2 y8 1", "Hotel", dust=True),
    LocationData("24FEAF2E-B4AB-5173-196E-4250394F8A5A - Hotel - x2 y3 0", "Hotel", dust=True),
    LocationData("FF370CA3-AA55-F443-E11B-B2B09F4862D1 - Hotel - x8 y9 0", "Hotel", dust=True),
    LocationData("AC719EE0-44C3-B151-4D98-FE312AD1CE9D - Hotel - x8 y6 0", "Hotel", dust=True),
    LocationData("11F829A2-54C0-46ED-6887-0782856C8CEB - Hotel - x9 y6 0", "Hotel", dust=True),
    LocationData("C30C487B-1DC4-90D0-BA1A-4882EA44649A - Hotel - x9 y6 1", "Hotel", dust=True),
    LocationData("D7BA1D6C-8012-E6A2-A661-F05A8299AB48 - Hotel - x9 y6 2", "Hotel", dust=True),
    LocationData("9714973A-BB93-7743-425B-285D41E12EEF - Hotel - x9 y6 3", "Hotel", dust=True),
    LocationData("859EF5B1-A2A4-BB06-8D09-0F7F76A47426 - Hotel - x6 y0 0", "Hotel", dust=True),
    LocationData("9B51C3B3-1F1E-3A8E-4660-41B413FDD480 - Hotel - x6 y0 1", "Hotel", dust=True),
    LocationData("B3F87961-F635-AE6C-CFE8-25425A6EF4FF - Hotel - x6 y7 0", "Hotel", dust=True),
    LocationData("60C44E41-DC17-2D8A-257B-AF4CE15589CD - Hotel - x6 y2 0", "Hotel", dust=True),
    LocationData("BC16C522-6F19-DC5A-EA44-1092027E7898 - Hotel - x6 y2 1", "Hotel", dust=True),
    LocationData("158DB2CB-6057-65CC-6D34-4DEC5F6378C1 - Hotel - x6 y2 2", "Hotel", dust=True),
    LocationData("E2569B02-BA31-CD69-DE1F-F7C097304AC1 - Hotel - x9 y3 0", "Hotel", dust=True),
    LocationData("04238CA0-8443-155E-00BB-4C77AB915447 - Hotel - x1 y10 0", "Hotel", dust=True),
    LocationData("A2EF5CC8-AEE1-ABC2-5C8E-5FEB30C0FB33 - Hotel - x3 y9 0", "Hotel", dust=True),
    LocationData("7855373A-926B-6B20-E1AB-934D0394E32C - Hotel - x4 y5 0", "Hotel", dust=True),
    LocationData("8C755E6E-4B14-067E-291D-C82574C1D4F1 - Hotel - x4 y5 1", "Hotel", dust=True),
    LocationData("B1B92B00-4D7C-D2D9-272A-E85988CAB495 - Hotel - x2 y3 1", "Hotel", dust=True),
    LocationData("BBC213EE-EE3D-A3A8-CB87-41F417A80322 - Hotel - x3 y4 0", "Hotel", dust=True),
    LocationData("E65461C6-6574-6588-159E-28DA15A1C8EB - Hotel - x2 y4 0", "Hotel", dust=True),
    LocationData("F529796B-8DBD-F4D4-7908-7071C5F0F89C - Hotel - x3 y6 0", "Hotel", dust=True),
    LocationData("AE99C65F-0CB5-35B9-51AF-14FF429C1832 - Hotel - x1 y6 0", "Hotel", dust=True),
    LocationData("D1AF321E-8EFB-745A-8B00-B1F666AA6308 - Red Cave - x6 y0 0", "Red Cave", dust=True),
    LocationData("408A0174-F1C4-3CF9-996E-F71BC7319345 - Red Cave - x6 y0 1", "Red Cave", dust=True),
    LocationData("EB56DA59-6627-C5EB-C397-A108F838E40D - Red Cave - x5 y0 0", "Red Cave", dust=True),
    LocationData("9FFAD1B8-E208-961D-4297-565727141A09 - Red Cave - x0 y0 0", "Red Cave", dust=True),
    LocationData("EEC03DBC-2801-D6BC-8C32-A4215E342583 - Red Cave - x2 y0 0", "Red Cave", dust=True),
    LocationData("575EAF8D-F7E0-B9EC-EC87-0F7DF94EA8C1 - Red Cave - x6 y0 2", "Red Cave", dust=True),
    LocationData("E0C9349A-6465-295F-46CF-04C35ECF42D0 - Red Cave - x6 y0 3", "Red Cave", dust=True),
    LocationData("FB5F6C91-AAD4-E359-E882-958DFB92D9E8 - Red Cave - x0 y3 0", "Red Cave", dust=True),
    LocationData("A6BBEF34-7EB7-9AF5-1D06-E8E8049F2DFC - Red Cave - x0 y3 1", "Red Cave", dust=True),
    LocationData("ECB775E9-BC4A-DADD-B919-5D1D30CE06FF - Red Cave - x6 y4 0", "Red Cave", dust=True),
    LocationData("6D3AA560-8D7C-E3E1-AFA4-25FB03E2DC03 - Red Cave - x6 y5 0", "Red Cave", dust=True),
    LocationData("0ECCDD94-EF4A-025E-2E46-BE043CCB0A51 - Red Cave - x2 y5 0", "Red Cave", dust=True),
    LocationData("E01AD091-3FAA-FAA4-5020-433E041FBDD7 - Red Cave - x2 y5 1", "Red Cave", dust=True),
    LocationData("E06AEB1A-D947-6B9A-8728-53223B241A1C - Red Cave - x6 y5 1", "Red Cave", dust=True),
    LocationData("69DA4760-0FEF-FA43-F28A-F5C2B4F697D7 - Space - x3 y5 0", "Space", dust=True),
    LocationData("B268D5D4-F0DC-8F76-122A-EEE2126A2F53 - Space - x3 y5 1", "Space", dust=True),
    LocationData("A0206B30-994E-86DE-7CAB-13CF8A10BC1B - Space - x7 y5 0", "Space", dust=True),
    LocationData("A8BFAF92-28F5-E814-F9E4-FACF310818DB - Space - x7 y5 1", "Space", dust=True),
    LocationData("Street - After Bridge Dust 1", "Street", dust=True),
    LocationData("Street - After Bridge Dust 2", "Street", dust=True),
    LocationData("4BEBEF47-ED97-866A-6425-D834D80422A0 - Boss Rush - x3 y6 0", "Boss Rush", dust=True),
    LocationData("E16F8508-D128-FB8A-1A67-15107B534007 - Boss Rush - x4 y6 0", "Boss Rush", dust=True),
    LocationData("BA0EBA50-03D1-9C62-D095-99C1F147F110 - Boss Rush - x4 y6 1", "Boss Rush", dust=True),
    LocationData("278E69CF-9771-C822-AEC8-C3B315FE7BA9 - Boss Rush - x4 y6 2", "Boss Rush", dust=True),
    LocationData("0FB4339E-7742-B339-3798-FBF4F7A172AB - Boss Rush - x4 y6 3", "Boss Rush", dust=True),
    LocationData("A9282642-ECD0-AF2C-7A53-962CCE28A064 - Boss Rush - x0 y5 0", "Boss Rush", dust=True),
    LocationData("ACE76242-06B8-20E4-DBD3-3DFC11828C8E - Boss Rush - x0 y6 0", "Boss Rush", dust=True)
]

locations_by_name: Dict[str, LocationData] = {location.name: location for location in all_locations}


def build_locations_by_region_dict():
    result: Dict[str, List[LocationData]] = {}
    for location in all_locations:
        result.setdefault(location.region_name, []).append(location)
    return result


locations_by_region: Dict[str, List[LocationData]] = build_locations_by_region_dict()

location_groups = {
    "Warp Pads": [location.name for location in all_locations if location.nexus_gate],
}
