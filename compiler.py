import sys

pointer = 0

def run_code(code):
    global pointer
    for command in code:
        if command == 'w':
            pointer += 1
        elif command == 's':
            pointer -= 1
        elif command == 'q':
            print(chr(pointer), end='')
        elif command not in ('w', 's', 'q'):
            continue

try:
    file = sys.argv[1]
    with open(file, "r") as f:
        run_code(f.read())
except:
    print(
        "Emolang compiler\n\nusage: python compile.py [filename]"
    )