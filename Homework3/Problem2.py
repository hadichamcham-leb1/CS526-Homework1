import sys


def grow(text, start, end, found):
    # base case: the piece cannot grow past the end of the text
    if end > len(text):
        return
    # the piece text[start:end] is a substring; the set ignores repeats
    found.add(text[start:end])
    # recursive case: the same start, one character longer
    grow(text, start, end + 1, found)


def main():
    text = sys.stdin.readline().strip()

    # one set, created once and shared by every recursive call
    found = set()
    for start in range(len(text)):
        # the first piece for each start is one character long
        grow(text, start, start + 1, found)

    # sets have no order, so sort before printing
    for piece in sorted(found):
        print(piece)
    print(len(found))


if __name__ == "__main__":
    main()
