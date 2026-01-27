rowdata = {
    "alice": ["first_kill", "level_10", "treasure_hunter", "speed_demon"],
    "bob": ["first_kill", "level_10", "boss_slayer", "collector"],
    "charlie":
    ["level_10",
     "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"]
}


data = {}
for key in rowdata:
    data[key] = set(rowdata[key])

print("=== Achievement Tracker System ===\n")

for key in data:
    print(f"Player {key} achievements:", data[key])
unique_achievements = set()
Common_Achievement = set()
for key in data:
    unique_achievements = unique_achievements.union(data[key])
for key in data:
    if not Common_Achievement:
        Common_Achievement = data[key]
    else:
        Common_Achievement = Common_Achievement.intersection(data[key])

print("\n=== Achievement Analytics ===\n")
print("All unique achievements:", unique_achievements)
print("Total unique achievements:", len(unique_achievements))
print("\nCommon to all players:", Common_Achievement)

rare_achievements = set()
count = 0
for key in data:
    this_player = set(data[key])
    for key2 in data:
        if key == key2:
            continue
        this_player = this_player.difference(data[key2])
    rare_achievements = rare_achievements.union(this_player)
    if this_player:
        count += 1

print(
    f"Rare achievements ({len(rare_achievements) // count} \
player) :", rare_achievements)
print()

print("Alice vs Bob common:", set(data['alice']).intersection(data['bob']))
print("Alice unique:", set(data['alice']).difference(data['bob']))
print("Bob unique:", set(data['bob']).difference(data['alice']))
