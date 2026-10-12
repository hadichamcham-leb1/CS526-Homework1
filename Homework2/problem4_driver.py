import sys
from problem4 import SortedDoublyLinkedList

# directive -> how the line should look (the argument count is taken from this text)
USAGE = {
    "add": "add <value>",
    "delete": "delete <value>",
    "exists": "exists <value>",
    "count": "count <value>",
    "print_list": "print_list",
    "total": "total",
    "sum_middle_three": "sum_middle_three",
    "median": "median",
}

# what to print when the list raises a ValueError
VALUE_ERROR_TEXT = {
    "sum_middle_three": "sum_middle_three needs at least 3 nodes",
    "median": "median of an empty list",
}


def to_number(text):
    """Return text as an int or a float, or None if it is not a number."""
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        return None


def main():
    my_list = SortedDoublyLinkedList()

    for line_number, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue

        parts = line.split()
        directive = parts[0].lower()
        args = parts[1:]

        if directive not in USAGE:
            print(f"line {line_number}: unknown directive '{directive}'")
            continue

        usage = USAGE[directive]
        if len(args) != len(usage.split()) - 1:
            print(f"line {line_number}: expected '{usage}', got '{line}'")
            continue

        value = None
        if args:                      # add, delete, exists and count take one number
            value = to_number(args[0])
            if value is None:
                print(f"line {line_number}: value must be a number, got '{line}'")
                continue

        if directive == "add":
            my_list.add(value)
            print(f"add({value})")
        elif directive == "delete":
            if my_list.delete(value):
                print(f"delete({value})")
            else:
                print(f"line {line_number}: {value} not found, nothing deleted")
        elif directive == "exists":
            print(f"exists({value}) = {my_list.exists(value)}")
        elif directive == "count":
            print(f"count({value}) = {my_list.count(value)}")
        elif directive == "print_list":
            my_list.print_list()
        else:                         # total, sum_middle_three, median: no argument
            try:
                result = getattr(my_list, directive)()
                print(f"{directive} = {result}")
            except ValueError:
                print(f"line {line_number}: {VALUE_ERROR_TEXT[directive]}")

    print("Final list: ", end="")
    my_list.print_list()


if __name__ == "__main__":
  main()