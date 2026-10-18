import sys


def is_palindrome(text):
    # base case: nothing or one character left, so nothing can disagree
    if len(text) <= 1:
        return True
    # base case: the two ends differ (case matters: "A" and "a" are different)
    if text[0] != text[-1]:
        return False
    # recursive case: the ends match
    return is_palindrome(text[1:-1])


def main():
    count = 0
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue
        # spaces between the characters do not change the answer
        text = line.replace(" ", "")
        result = is_palindrome(text)
        print(result)
        if result:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
