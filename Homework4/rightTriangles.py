import sys
import math


def count_right_triangles(points):
    total_triangles = 0
    n = len(points)

    for i in range(n):
        px, py = points[i] # P, the point we test as the right-angle corner
        freq = {}          # direction from P : number of points in that direction

        # Step 1: direction from P to every other point
        for j in range(n):
            if i == j:
                continue
            qx, qy = points[j]
            dx = qx - px
            dy = qy - py

            # Use math.gcd : reduce (dx, dy) to its simplest integer form by
            # dividing by the gcd. This gives all points on the same ray P the
            # same key. We get integers only , so no rounding problems.
            g = math.gcd(dx, dy)
            vec = (dx // g, dy // g)

            # Check if vector is already in our dictionary
            if vec in freq:
                freq[vec] += 1
            else:
                freq[vec] = 1

        # Step 2: match direction with its perpendicular direction
        for (dx, dy), count in freq.items():
            # (dx, dy) rotate 90 degrees counter-clockwise
            perp_vec = (-dy, dx)
            if perp_vec in freq:
                # One point from each group gives a right angle at P. Only
                # the direction matters, not the distance.
                total_triangles += count * freq[perp_vec]

    return total_triangles

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    # Read the n points, two numbers (x and y) at a time
    points = []

    idx = 1
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        points.append((x, y))
        idx += 2

    result = count_right_triangles(points)
    print(f"The number of right triangles is: {result}")


if __name__ == "__main__":
    main()