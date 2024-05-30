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

small_key_item_count = {
    "Small Key (Apartment)": 4,
    "Small Key (Temple of the Seeing One)": 3,
    "Small Key (Circus)": 4,
    "Small Key (Mountain Cavern)": 4,
    "Small Key (Hotel)": 7,
    "Small Key (Red Cave)": 6,
    "Small Key (Street)": 1,
}

big_keys = [
    "Green Key",
    "Red Key",
    "Blue Key",
]

statue_items = [
    "Temple of the Seeing One Statue",
    "Red Cave Statue",
    "Mountain Cavern Statue",
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
    "Progressive Red Cave",
    *statue_items,
    "Progressive Swap",
]

progression_items = [
    "Broom",
    "Swap",
    "Jump Shoes",
    *cards,
    *small_key_item_count.keys(),
    *big_keys,
    "Cardboard Box",
    "Biking Shoes",
    "Progressive Red Cave",
    *statue_items,
    "Progressive Swap",
]

useful_items = [
    "Widen",
    "Extend",
    "Health Cicada",
]

trap_items = [
]

filler_items = [
    *secret_items,
]

item_groups = {
    "Cards": cards
}
