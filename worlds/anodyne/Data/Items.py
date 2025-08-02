from collections import defaultdict

from . import Locations
from .Locations import LocationType
from .Regions import RegionEnum, Bedroom, Red_Cave, Crowd, Blue, Happy

cards = [
    # Type 0
    "Card (Edward)",
    "Card (Annoyer)",
    "Card (Seer)",
    "Card (Shieldy)",
    "Card (Slime)",
    "Card (PewLaser)",
    "Card (Suburbian)",
    "Card (Watcher)",
    "Card (Silverfish)",
    "Card (Gas Guy)",
    # Type 10
    "Card (Mitra)",
    "Card (Miao)",
    "Card (Windmill)",
    "Card (Mushroom)",
    "Card (Dog)",
    "Card (Rock)",
    "Card (Fisherman)",
    "Card (Walker)",
    "Card (Mover)",
    "Card (Slasher)",
    # Type 20
    "Card (Rogue)",
    "Card (Chaser)",
    "Card (Fire Pillar)",
    "Card (Contorts)",
    "Card (Lion)",
    "Card (Arthur and Javiera)",
    "Card (Frog)",
    "Card (Person)",
    "Card (Wall)",
    "Card (Blue Cube King)",
    # Type 30
    "Card (Orange Cube King)",
    "Card (Dust Maid)",
    "Card (Dasher)",
    "Card (Burst Plant)",
    "Card (Manager)",
    "Card (Sage)",
    "Card (Young)",
    "Card (Carved Rock)",
    "Card (City Man)",
    "Card (Intra)",
    # Type 40
    "Card (Torch)",
    "Card (Triangle NPC)",
    "Card (Killer)",
    "Card (Goldman)",
    "Card (Broom)",
    "Card (Rank)",
    "Card (Follower)",
    "Card (Rock Creature)",
    # Type 49
    "Card (Null)",
]

postgame_cards = [
    "Card (Young)",
    "Card (Carved Rock)",
    "Card (City Man)",
    "Card (Intra)",
    "Card (Torch)",
    "Card (Triangle NPC)",
    "Card (Killer)",
    "Card (Broom)",
    "Card (Rank)",
    "Card (Follower)",
    "Card (Rock Creature)",
    "Card (Null)",
]

secret_items = [
    "Golden Poop",
    "Spam Can",
    "Glitch",
    "Heart",
    "Electric Monster",
    "Cat Statue",
    "Melos",
    "Marina",
    "Black Cube",
    "Red Cube",
    "Green Cube",
    "Blue Cube",
    "White Cube",
    "Golden Broom",
]

early_secret_items = [
    "Golden Poop",
    "Heart",
]

secret_items_secret_paths = [
    "Glitch",
    "Spam Can",
    "Electric Monster"
]

small_key_count:defaultdict[type[RegionEnum],int] = defaultdict(int)
for location in Locations.all_locations:
    if location.small_key:
        small_key_count[location.region.__class__] += 1

small_key_item_count = {
    f"Small Key ({dungeon.area_name()})":value for dungeon,value in small_key_count.items()
}

big_keys = [
    "Green Key",
    "Red Key",
    "Blue Key",
]

key_rings = [
    f"Key Ring ({dungeon.area_name()})" for dungeon in small_key_count.keys()
]

statue_items = [
    f"{Bedroom.area_name()} Statue",
    f"{Red_Cave.area_name()} Statue",
    f"{Crowd.area_name()} Statue",
]

non_secret_filler_items = [
    "Heal",
    "Big Heal"
]

def region_to_nexus_gate(region:RegionEnum):
    return f"Nexus Gate ({region.area_name()})"


nexus_gate_items = {
    region_to_nexus_gate(location.region):location.region for location in Locations.nexus_pad_locations
}

trap_items = [
    "Person Trap",
    "Gas Trap"
]

fountains = [
    f"{Blue.area_name()} Fountain",
    f"{Happy.area_name()} Fountain"
]

# This array must maintain a consistent order because the IDs are generated from it.
all_items = [
    "Broom",
    "Jump Shoes",
    "Widen",
    "Extend",
    "Swap",
    # Cards
    *cards,
    # Secrets
    *secret_items,
    # Keys
    *small_key_item_count.keys(),
    *big_keys,
    "Health Cicada",
    "Cardboard Box",
    "Biking Shoes",
    f"Progressive {Red_Cave.area_name()}",
    *statue_items,
    "Progressive Swap",
    *non_secret_filler_items,
    *nexus_gate_items.keys(),
    *trap_items,
    *key_rings,
    "Miao",
    *fountains
]

progression_items = [
    "Broom",
    "Widen",
    "Extend",
    "Swap",
    "Jump Shoes",
    *cards,
    *small_key_item_count.keys(),
    *big_keys,
    "Cardboard Box",
    "Biking Shoes",
    f"Progressive {Red_Cave.area_name()}",
    *statue_items,
    "Progressive Swap",
    *nexus_gate_items.keys(),
    *key_rings,
    "Miao",
    *fountains
]

useful_items = [
    "Health Cicada",
]

filler_items = [
    *secret_items,
    *non_secret_filler_items,
]

brooms = [
    "Broom",
    "Widen",
    "Extend"
]

item_groups = {
    "Cards": cards,
    "Nexus Gates": nexus_gate_items.keys(),
    "Keys": small_key_item_count.keys(),
    "Key Rings": key_rings,
    "Big Keys": big_keys,
    "Statues": statue_items,
    "Brooms": brooms,
    "Fountains": fountains
}
