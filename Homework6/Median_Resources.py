import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None      # left child  (None = no child)
        self.right = None     # right child (None = no child)
        self.parent = None    # node above  (None for the root)

class MinHeap:
    def __init__(self):
        self.root = None      # top node (None while the heap is empty)
        self.size = 0         # number of values; also the position of the last node

    def __len__(self):        # makes len(heap) work
        return self.size

    # Added helper function to adjust to a MaxHeap
    def _before(self, a, b):
        # True if value a belongs above value b in the heap
        return a < b

    def is_empty(self):
        return self.size == 0

    # navigation helper
    def _node_at(self, position):
        # Walk from the root to the node at the given position (1-based).
        # bin(6) = '0b110'; [3:] drops '0b' and the leading 1 -> '10'.
        # O(log n): one step per binary digit.
        path = bin(position)[3:]
        node = self.root
        for digit in path:
            if digit == '0':
                node = node.left
            else:
                node = node.right
        return node

    def _add_node(self, value):
        # Attach a new node at the next free spot (position size + 1) WITHOUT
        # reordering values. This keeps the complete shape (rule 2).
        new_node = Node(value)

        if self.root is None:             # first node becomes the root
            self.root = new_node
            self.size = 1
            return new_node

        position = self.size + 1          # compute before increasing size
        parent = self._node_at(position // 2)   # parent's position is position // 2
        last_digit = bin(position)[-1]    # last path digit: left (0) or right (1)
        new_node.parent = parent
        if last_digit == '0':
            parent.left = new_node
        else:
            parent.right = new_node
        self.size += 1
        return new_node

    def _upheap(self, node):
        # Move a value up while it is strictly smaller than its parent's value.
        # We swap the values stored in the nodes, not the nodes themselves,
        # so no links have to be rewired. The check "node.parent is not None"
        # must come first so the root (which has no parent) stops the loop.
        while node.parent is not None and self._before(node.value, node.parent.value):
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def _downheap(self, node):
        # Move a value down: find the smallest among the node and its existing
        # children. If a child is smaller, swap values with it and continue
        # from that child. Choosing the SMALLER child guarantees the new parent
        # is <= its other child, so the heap order is restored.
        while True:
            smallest = node
            if node.left is not None and self._before(node.left.value, smallest.value):
                smallest = node.left
            if node.right is not None and self._before(node.right.value, smallest.value):
                smallest = node.right
            if smallest is node:          # no child is smaller: done
                break
            node.value, smallest.value = smallest.value, node.value
            node = smallest

    def insert(self, value):
        # Add at the next free spot, then bubble up.
        new_node = self._add_node(value)
        self._upheap(new_node)

    def peek(self):
        # The root always holds the smallest value.
        if self.root is None:
            raise IndexError("heap is empty")
        return self.root.value

    def extract_min(self):
        # 1. Save the root's value (the minimum) to return it.
        # 2. Copy the last node's value into the root and detach the last node
        #    (this keeps the complete shape).
        # 3. Bubble the new root value down.
        if self.root is None:
            raise IndexError("heap is empty")

        smallest = self.root.value

        if self.size == 1:                # only one node: heap becomes empty
            self.root = None
            self.size = 0
            return smallest

        last = self._node_at(self.size)   # find it before decreasing size
        self.root.value = last.value
        if last is last.parent.left:      # detach the last node from its parent
            last.parent.left = None
        else:
            last.parent.right = None
        self.size -= 1
        self._downheap(self.root)
        return smallest

    def _find(self, node, value):
        # Return a node holding value, or None. A heap has no left/right order,
        # so we may have to look in both subtrees. Shortcut: if a node's value
        # is already larger than the target, everything below it is larger too,
        # so that whole subtree is skipped.
        if node is None:
            return None
        if node.value == value:
            return node
        if self._before(value, node.value):
            return None
        found = self._find(node.left, value)
        if found is not None:
            return found
        return self._find(node.right, value)

    def delete(self, value):
        # Remove one copy of value. Returns True if removed, False otherwise.
        # Same idea as extract_min: the last node's value fills the gap and the
        # last node is detached. The moved value might be too small for its new
        # spot (needs to go UP) or too large (needs to go DOWN), so we try both;
        # only one of them can actually change anything.
        target = self._find(self.root, value)
        if target is None:
            return False

        if self.size == 1:
            self.root = None
            self.size = 0
            return True

        last = self._node_at(self.size)   # find it before decreasing size
        if last is last.parent.left:
            last.parent.left = None
        else:
            last.parent.right = None
        self.size -= 1

        if target is last:                # we just removed the node itself
            return True

        target.value = last.value
        self._upheap(target)
        self._downheap(target)
        return True

    def build(self, values):
        # Replace the heap's contents with values "all at once":
        #   1. create all nodes in position order, no reordering (shape is right);
        #   2. run _downheap on every node that has a child, from the last one
        #      (position size // 2) back to the root. Going bottom-up means that
        #      when a node is fixed, the subtrees below it are already heaps.
        self.root = None
        self.size = 0
        for v in values:
            self._add_node(v)
        for p in range(self.size // 2, 0, -1):
            self._downheap(self._node_at(p))

    def heap_sort(self):
        # Return all values in increasing order without changing this heap:
        # copy the values into a temporary heap and extract from the copy.
        values = []
        for p in range(1, self.size + 1):
            values.append(self._node_at(p).value)

        temp = type(self)()
        temp.build(values)

        result = []
        while not temp.is_empty():
            result.append(temp.extract_min())
        return result

    # ----- drawing -------------------------------------------------------------
    def print_heap(self):
        # Row of a node = its depth. Column of a node = its place in a
        # left-to-right (in-order) walk, times a cell width W. With an in-order
        # walk a parent always lands between its left and right children.
        # '/' or '\' is placed halfway between a child and its parent.
        if self.root is None:
            print("(empty)")
            return

        order = []        # nodes from left to right
        depth = {}        # node -> its level (root = 0)

        def walk(node, d):
            if node is None:
                return
            walk(node.left, d + 1)
            order.append(node)
            depth[node] = d
            walk(node.right, d + 1)

        walk(self.root, 0)

        W = max(len(str(n.value)) for n in order) + 2   # cell width
        col = {}
        for i, node in enumerate(order):
            col[node] = i * W

        H = max(depth.values()) + 1                     # number of levels
        width = len(order) * W
        rows = [[" "] * width for _ in range(2 * H - 1)]  # value rows + slash rows

        for node in order:
            c = col[node]
            d = depth[node]
            for offset, ch in enumerate(str(node.value)):
                rows[2 * d][c + offset] = ch
            if node.parent is not None:
                pc = col[node.parent]
                if node is node.parent.left:
                    rows[2 * d - 1][(c + pc) // 2] = "/"
                else:
                    rows[2 * d - 1][(c + pc) // 2] = "\\"

        for row in rows:
            print("".join(row).rstrip())

class MaxHeap(MinHeap):
    # same heap, but the largest value is on top
    # peek() and extract_min() return the top value, so here it is the largest
    def _before(self, a, b):
        return a > b

def running_medians(sales):
    low = MaxHeap()
    high = MinHeap()
    medians = []

    for x in sales:
        if low.is_empty() or x <= low.peek():
            low.insert(x)
        else:
            high.insert(x)

        if len(low) > len(high) + 1:
            high.insert(low.extract_min())
        elif len(high) > len(low):
            low.insert(high.extract_min())

        if len(low) > len(high):
            medians.append(float(low.peek()))
        else:
            medians.append((low.peek() + high.peek()) / 2)

    return medians

def parse_line(line):
    inner = line.strip()[1:-1].strip()   # drop the [ and ]
    if inner == "":
        return []                        # the line was "[]"
    return [int(piece) for piece in inner.split(",")]

if __name__ == "__main__":
    sales = parse_line(sys.stdin.readline())
    print(running_medians(sales))

