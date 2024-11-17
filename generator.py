import sys

def string_to_code(input_string):
    pointer = 0
    code = ""

    for char in input_string:
        target = ord(char)
        diff = target - pointer

        if diff > 0:
            code += "w" * diff
        elif diff < 0:
            code += "s" * (-diff)

        code += "q"
        pointer = target

    return code


def main():
    try:
        input_string = sys.argv[1]
    except IndexError:
        print("Usage: python generator.py [string]")
        return

    code = string_to_code(input_string)
    print(code)


if __name__ == "__main__":
    main()
