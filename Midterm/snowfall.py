import sys

def snowfall(n, A):
    if n < 3:
        return False

    threshold = A[-1] / 2 # Total snow across all n days divided by 2

    # Check the very first 3-day window (days 1 to 3)
    if A[2] > threshold:
        return True

    # Check remaining 3-day window from Day 2 onwards

    for i in range (1, n-2):
            snow_fall = A[i+2] - A[i-1]
            if snow_fall > threshold:
                return True

    return False


def main():
    input_data = sys.stdin.read().splitlines()

    if not input_data or not input_data[0].strip():
        print("Error: File empty")
        return

    # Parse line 1: Convert string to integer
    n = int(input_data[0].strip())

    # Parse line 2: Split space-separated string into float/int list
    A = [int(x) for x in input_data[1].split()]

    result = snowfall(n, A)
    if result == False:
        result = "NO"
    else:
        result = "YES"
    print(f'{" ".join(str(x) for x in A)} solution: {result}')

if __name__ == '__main__':
    main()


