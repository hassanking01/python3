import sys

print("=== Command Quest ===")
arguments_len = len(sys.argv) - 1
if not arguments_len:
    print("No arguments provided!")

print("Program name:", sys.argv[0])
if arguments_len:
    print("Arguments received:", arguments_len)
i = 1

while i <= arguments_len:
    print(f"Argument {i}:", sys.argv[i])
    i += 1
print("Total arguments:", arguments_len + 1)
