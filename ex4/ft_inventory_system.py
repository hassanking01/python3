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


def getplayer_inventory(player):
    catalog = data["catalog"]
    player_items = data["players"][player]["items"]
    categories = {}
    player = data["players"][player]
    for key in player_items:
        if categories.get(catalog[key]['type']):
            categories[catalog[key]['type']] += 1
        else:
            categories.update({catalog[key]['type']: 1})

        print(f"{key} ({catalog[key]['type']},{catalog[key]['rarity']})"
              f": {player_items[key]} @ {catalog[key]['value']}"
              f"gold each = {player_items[key] * catalog[key]['value']} gold")

    print("\nInventory value:", player["total_value"], "gold")
    print("Item count:", player["item_count"], "items")
    categories_str = "Categories:"
    for key in categories:
        categories_str += f" {key}({categories[key]}),"
    print(categories_str)


print("=== Alice's Inventory ===\n")
getplayer_inventory("alice")


def send_items(sender_name, receiver_name, item, count):
    item_data = data["catalog"][item]
    sender = data["players"].get(sender_name)
    receiver = data["players"].get(receiver_name)
    if sender and receiver:
        if sender["items"].get(item):
            if sender["items"].get(item) >= count:
                sender["items"][item] -= count
                if receiver["items"].get(item):
                    receiver["items"][item] += count
                else:
                    receiver["items"].update({item: count})
                receiver["item_count"] += count
                receiver["item_count"] -= count
                sender["total_value"] -= item_data["value"]
                receiver["total_value"] -= item_data["value"]
                print("Transaction successful!")
            else:
                print(f"not enough {item} in {sender_name}'s inventory")


print("\n=== Transaction: Alice gives Bob 2 quantum_ring ===")
send_items("alice", "bob", "quantum_ring", 2)


def get_item_count(player_name, item):
    if data["players"][player_name]["items"].get(item):
        print(f"{player_name} {item}: \
 {data['players'][player_name]['items'][item]}")


print("\n=== Updated Inventories ===")
get_item_count('alice', 'quantum_ring')
get_item_count('bob', 'quantum_ring')


def analytics():
    players = data["players"]
    mostgold = {"player": "none", "gold": 0}
    mostitems = {"player": "none", "items": 0}
    allitems = {}
    for key in players:
        if players[key]["total_value"] > mostgold["gold"]:
            mostgold["gold"] = players[key]["total_value"]
            mostgold["player"] = key
        if players[key]["item_count"] > mostitems["items"]:
            mostitems["items"] = players[key]["item_count"]
            mostitems["player"] = key
        for item in players[key]["items"]:
            if allitems.get(item):
                allitems[item] += players[key]["items"][item]
            else:
                allitems[item] = players[key]["items"][item]
    most_item = 0
    for key in allitems:
        if most_item < allitems[key]:
            most_item = allitems[key]
    rarest_valu = most_item
    for key in allitems:
        if rarest_valu > allitems[key]:
            rarest_valu = allitems[key]
    rares_items = {}
    for key in allitems:
        if allitems[key] == rarest_valu:
            rares_items[key] = allitems[key]
    print(f"Most valuable player: {mostgold['player']} ({mostgold['gold']} \
 gold)")
    print(f"Most items: {mostitems['player']} ({mostitems['items']} items)")
    print("Rarest items:", end="")
    rarest_str = ""
    for key in rares_items:
        rarest_str += f" {key},"
    if rarest_str:
        print(rarest_str[:-1])


print("\n=== Inventory Analytics ===")
analytics()
