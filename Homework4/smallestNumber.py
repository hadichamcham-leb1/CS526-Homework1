import sys


def find_smallest_count(arr, target):

    # Sort a copy, largest first. The original array stays in input order
    # because main() has to print it in that order.
    sorted_arr = sorted(arr, reverse=True)

    current_sum = 0
    count = 0

    for val in sorted_arr:
        current_sum += val
        count += 1
        if current_sum > target:
            return count

    return count


def main():

    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # The first value is n, the second is the target T
    n = int(input_data[0])
    target = int(input_data[1])
    original_arr = [int(x) for x in input_data[2 : 2 + n]]


    answer = find_smallest_count(original_arr, target)

    array_str = ",".join(map(str, original_arr))
    print(f"Input: {array_str} Target: {target} Answer: {answer}")


if __name__ == "__main__":
    main()