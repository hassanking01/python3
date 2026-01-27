import math

destination = (0, 0, 0)
position1 = (10, 20, 5)
x1, y1, z1 = destination
x2, y2, z2 = position1

print("=== Game Coordinate System ===\n")

print("Position created:", position1)
des_len = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
print(f"Distance between {destination} and {position1}: {des_len:.2f}")

parsing_position = "3,4,0"
position2 = tuple([int(i) for i in parsing_position.split(",")])
x3, y3, z3 = position2
des_len = math.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2)
print()
print("Parsing coordinates:", f"\"{parsing_position}\"")
print("Parsed position:", position2)
print(f"Distance between {destination} and {position2}: {des_len:.1f}")
print()

invalid_parsing = "abc,def,ghi"
print("Parsing invalid coordinates:", f"\"{invalid_parsing}\"")
try:
    position3 = tuple([int(i) for i in invalid_parsing.split(",")])
except Exception as e:
    print("Error parsing coordinates:", e)
    print("Error details - Type: ValueError, Args:", e.args)

print()
print("Unpacking demonstration:")
X, Y, Z = position2
print(f"Player at x={X}, y={Y}, z={Z}")
print(f"Coordinates: X={X}, Y={Y}, Z={Z}")
