import sys


def main():
    n = int(sys.stdin.readline())

    # read every pair as four numbers: Ghostbuster (bx, by) and ghost (gx, gy)
    streams = []
    for line in sys.stdin:
        parts = line.split()
        if not parts:                 # skip a blank line
            continue
        bx = int(parts[1])
        by = int(parts[2])
        gx = int(parts[4])
        gy = int(parts[5])
        streams.append((bx, by, gx, gy))

    # direction of the first stream
    bx, by, gx, gy = streams[0]
    dx = gx - bx
    dy = gy - by

    offsets = set()
    for bx, by, gx, gy in streams:
        ex = gx - bx
        ey = gy - by
        # parallel test by cross-multiplying (no division, so vertical streams work)
        if dx * ey - dy * ex != 0:
            print("All Ghosts: were not eliminated")
            return                    # not parallel: they cross, no need to look further

        # label of the line this stream lies on: equal labels mean the same line
        offsets.add(dx * by - dy * bx)

    # a repeated label means two streams share a line, which counts as crossing
    if len(offsets) == len(streams):
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")


if __name__ == "__main__":
    main()
