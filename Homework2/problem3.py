def ways(n):
    # number of ways to climb n steps, taking 1, 2 or 3 steps at a time
    if n < 0:
        return 0  # overshot the top: not a valid path
    if n == 0:
        return 1  # landed exactly on the top: one valid path

    # the first move is 1, 2 or 3 steps; then count the ways to climb what is left
    return ways(n - 1) + ways(n - 2) + ways(n - 3)


if __name__ == "__main__":
    print("ways(3) =", ways(3))
    print("ways(5) =", ways(5))
    print("ways(10) =", ways(10))
