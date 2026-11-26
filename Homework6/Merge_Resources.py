import sys

class MinHeap:
    def __init__(self):
        self.data = []       # list of (key, value) entries

    # index arithmetic (0-based)
    def _parent(self, i): return (i-1)//2
    def _left(self, i): return (i*2+1)
    def _right(self, i): return (i*2+2)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def min(self):
        # Peek at the smallest entry without removing it (not needed by
        # merge_logs, but part of the usual priority queue interface).
        if self.is_empty():
            raise IndexError("heap is empty")
        return self.data[0]

    def insert(self, key, value=None):
        # Add the entry at the end (the next free spot keeps the tree
        # complete), then bubble it up to repair the heap order.
        # self.data.append((key, value)) # 1. add at the next free spot
        self._upheap(len(self.data)-1)

    def _upheap(self, i):
        # Swap the entry with its parent while its key is STRICTLY smaller.
        # Stop at the root (i == 0) or when the parent is smaller or equal.
        while i > 0:
            p = self._parent(i)
            if self.data[i][0] < self.data[p][0]:
                self._swap(i, p)
                i = p
            else:
                break

    def remove_min(self):
        # Remove and return the entry with the smallest key. O(log n).
        # Trick: swap the root with the last entry, pop the last entry (that
        # is the old minimum), then bubble the new root down.
        if self.is_empty():
            raise IndexError("heap is empty")
        self._swap(0, len(self.data)-1)
        smallest = self.data.pop()
        if not self.is_empty():       # nothing to repair if the heap is now empty
            self._downheap(0)
        return smallest

    def _downheap(self, i):
        # Find the smallest key among the entry and its existing children.
        # If a child is smaller, swap with it and continue from there.
        # Picking the smaller child keeps the heap order correct.
        n = len(self.data)
        while True:
            left, right = self._left(i), self._right(i)
            smallest = i
            if left < n and self.data[left][0] < self.data[smallest][0]:
                smallest = left       # "left < n" checks that the child exists
            if right < n and self.data[right][0] < self.data[smallest][0]:
                smallest = right
            if smallest == i:         # neither child is smaller: done
                break
            self._swap(i, smallest)
            i = smallest


def parse_line(line):
    inner = line.strip()[1:-1].strip()      # drop the [ and ]
    if inner == "":
        return []                           # the line was "[]"
    return [int(piece) for piece in inner.split(",")]


def read_logs():
    # Returns a list of logs:
    logs = []
    for line in sys.stdin:
        if line.strip() == "":
            continue
        logs.append(parse_line(line))
    return logs


def merge_logs(logs):
    k = len(logs)
    heap = MinHeap()
    next_index = [0] * k    # next unused sale position for each register
    result = []

    # Seed: first sale from each non-empty register.
    # r is the LIST position (0-based); the register NUMBER is r + 1.
    for r in range(k):
        if len(logs[r]) > 0:
            heap.insert((logs[r][0], r + 1))
            next_index[r] = 1

    # Repeatedly take the earliest remaining sale, then refill the heap from
    # the register it came from.
    while not heap.is_empty():
        key = heap.remove_min()[0]          # key = (time, register_number)
        time, reg = key
        result.append(key)

        pos = reg - 1                       # register number -> list position
        i = next_index[pos]
        if i < len(logs[pos]):              # does this register have more sales?
            heap.insert((logs[pos][i], pos + 1))
            next_index[pos] = i + 1

    return result


if __name__ == "__main__":
    logs = read_logs()
    merged = merge_logs(logs)               # run the merge once, reuse the result
    print(f"Registers: {len(logs)}")
    print(f"Total sales: {len(merged)}")
    print(f"Merged log: {merged}")
