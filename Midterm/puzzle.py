import sys
from math import sqrt

def validate_board(board, n, allowed_symbols):
    # Create empty tracking sets for each row, col, and sub-board
    row_sets = [set() for row_idx in range(n)]
    col_sets = [set() for col_idx in range(n)]
    box_sets = {}  # maps box_key -> set()

    s = int(sqrt(n))

    # The loop: Visit every single cell (r, c) in the grid
    for r in range(n):
        for c in range(n):
            val = board[r][c]

            if val == '.':
                continue

            if val not in allowed_symbols:
                return False

            # Using floor division to get a value from 0 to s - 1
            box_key = (r // s, c // s)
            if box_key not in box_sets:
                box_sets[box_key] = set()

            # The check happens cell by cell as the loops run
            if val in row_sets[r] or val in col_sets[c] or val in box_sets[box_key]:
                return False  # Found a duplicate!

            # Record this symbol in our memory sets
            row_sets[r].add(val)
            col_sets[c].add(val)
            box_sets[box_key].add(val)

    return True  # If loops complete without returning False, board is valid


def main():
    line = sys.stdin.readline()
    if not line:
        return

    n = int(line.strip())

    line2 = sys.stdin.readline()
    if not line2:
        return

    allowed_symbols = set(line2.strip().split(","))

    board = []
    for line in sys.stdin:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        parts = line.strip().split(",")
        board.append(parts)

    # Execute validation and print output
    if validate_board(board, n, allowed_symbols):
        print("The board is valid")
    else:
        print("The board is invalid")

if __name__ == "__main__":
    main()