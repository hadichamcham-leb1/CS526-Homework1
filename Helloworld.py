import sys

def main():
    # This loop automatically reads EVERY line in the input file,
    # whether it has 1 line or 1,000 lines.
    for line in sys.stdin:
        print(line, end='')

if __name__ == "__main__":
    main()
