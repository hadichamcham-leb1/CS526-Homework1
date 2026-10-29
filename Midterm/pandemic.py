import sys

def main():
    line = sys.stdin.readline()
    if not line:
        return

    n = int(line.strip())

    infected_counties = set()

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        r = int(parts[0])
        c = int(parts[1])

        infected_counties.add((r, c))

    #  Simulate the infection spread
    while True:
        new_infected_counties = set()

        # Iterate over existing counties to find diagonal pairs
        for r,c in infected_counties:
            offsets = [(-1,-1), (-1,1), (1,-1), (1,1)]
            for dr, dc in offsets:
                r_diag, c_diag = r + dr, c + dc

                # Step 1: Check if the diagonal neighbor is infected
                if (r_diag, c_diag) in infected_counties:

                    # Step 2: Define the two shared corners
                    corner1 = (r, c_diag)
                    corner2 = (r_diag, c)

                    # Step 3: Check boundaries and add to new_infected_countries if valid!
                    if 0 <= r < n and 0 <= c_diag < n and corner1 not in infected_counties:
                        new_infected_counties.add(corner1)
                    if 0 <= r_diag < n and 0 <= c < n and corner2 not in infected_counties:
                        new_infected_counties.add(corner2)



        if not new_infected_counties:
            break

        # Otherwise, add today's new infections to our set for tomorrow
        infected_counties.update(new_infected_counties)

    if len(infected_counties) == n * n:
        print("There are no healthy counties left")
    else:
        print("There are healthy counties left")


if __name__ == "__main__":
    main()


