import sys
from problem2 import SinglyLinkedList

# directive -> how the line should look (the argument count is taken from this text)
USAGE = {
    "append": "append <value>",
    "prepend": "prepend <value>",
    "insert": "insert <index> <value>",
    "get": "get <index>",
    "find": "find <value>",
    "len": "len",
    "update": "update <index> <value>",
    "delete": "delete <value>",
    "delete_at": "delete_at <index>",
    "print_list": "print_list",
}

# directives whose FIRST argument is an index (must be a whole number)
INDEX_DIRECTIVES = ("insert", "get", "update", "delete_at")


def to_value(text):
    """Turn '12' into the number 12; leave anything else as text."""
    try:
        return int(text)
    except ValueError:
        return text


def main():
    my_list = SinglyLinkedList()

    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue

        parts = line.split()
        directive = parts[0]
        args = [to_value(a) for a in parts[1:]]

        if directive not in USAGE:
            print(f"line {line_number}: unknown directive '{directive}'")
            continue

        usage = USAGE[directive]
        if len(args) != len(usage.split()) - 1:
            print(f"line {line_number}: expected '{usage}', got '{line}'")
            continue

        if directive in INDEX_DIRECTIVES and not isinstance(args[0], int):
            print(f"line {line_number}: index must be a whole number, got '{line}'")
            continue

        try:
            if directive == "len":
                print(f"len = {len(my_list)}")
            else:
                result = getattr(my_list, directive)(*args)
                if directive in ("get", "find", "delete_at"):
                    print(f"{directive}({args[0]}) = {result}")
                elif directive == "delete" and result is False:
                    print(f"line {line_number}: value {args[0]} not found in the list")
        except IndexError:
            print(f"line {line_number}: index {args[0]} out of range")

    print("Final list: ", end="")
    my_list.print_list()

if __name__ == "__main__":
    main()