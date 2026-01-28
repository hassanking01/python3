data = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal":
        {"type": "material", "value": 1000, "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


print("=== Alice's Inventory ===\n")
catalog = data["catalog"]
alice_items = data["players"]["alice"]["items"]
categories = {}
alice = data["players"]["alice"]
for key in alice_items:
    if categories.get(catalog[key]['type']):
        categories[catalog[key]['type']] += 1
    else:
        categories[catalog[key]['type']] = 1

    print(f"{key} ({catalog[key]['type']},\
 {catalog[key]['rarity']}): {alice_items[key]} @ {catalog[key]['value']} \
 gold each = {alice_items[key] * catalog[key]['value']} gold")

print("\nInventory value:", alice["total_value"], "gold")
print("Item count:", alice["item_count"], "items")
categories_str = "Categories:"
for key in categories:
    categories_str += f" {key}({categories[key]}),"
print(categories_str)


