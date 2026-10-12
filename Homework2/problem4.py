class Node:
    # One box in the chain: a value, an arrow back (prev) and an arrow forward (next).
    def __init__(self, value):
        self.value = value
        self.next = None  # None for the last node
        self.prev = None  # None for the first node

class SortedDoublyLinkedList:
    # Keeps its values in ascending order. Duplicates are allowed.
    # _size counts the nodes (named _size so it does not clash with the count() method).
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            # empty list: the new node is both head and tail
            self.head = new_node
            self.tail = new_node
        elif new_node.value <= self.head.value:
            # new smallest value (or equal to it): goes at the front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif new_node.value > self.tail.value:
            # new largest value: goes at the end
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            # Case 4: Insert somewhere in the middle
            curr = self.head
            # Walk until we find a node with a value larger than or equal to new_node.value
            while curr is not None and curr.value < new_node.value:
                curr = curr.next

            # Insert new_node right BEFORE curr
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node

        self._size += 1
        return True


    def delete(self, value):
        if self.head is None:
            return False
        # Walk until we reach a value >= target or run off the end of list
        curr = self.head
        while curr is not None and curr.value < value:
            curr = curr.next
        #check if we found the exact match safely
        if curr is None or curr.value != value:
            return False
        # curr is the head node:
        if curr == self.head:
            self.head = self.head.next
            if self.head is None: # List had only 1 node
                self.tail = None
            else: # List has remaining nodes
                self.head.prev = None
        # curr is the tail node:
        elif curr == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        # curr is a middle node
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

        self._size -= 1
        return True

    def exists(self, value):
        return self._exists_helper(self.head, value)
    def _exists_helper(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        # stop early: the list is sorted, so we have passed where the value could be
        if node.value > value:
            return False

        return self._exists_helper(node.next, value)

    def print_list(self):
        if self.head is None:
            print("(empty)")
        else:
            self._print_helper(self.head)
            print()

    def _print_helper(self, node):
        # base case : stop when there are no more nodes
        if node is None:
            return

        # check if this node is the last one in the list (the tail)
        if node.next is None:
            print(node.value, end="")
        else:
            # print the value followed by double arrows for a doubly linked list
            print(f"{node.value} <-> ", end="")

        # recursive step: call the helper on the next node.
        self._print_helper(node.next)

    def total(self):
        return self._total_helper(self.head)

    def _total_helper(self, node):
        # base case: when we reach past the tail, there are no more numbers to reach
        if node is None:
            return 0

        # recursive step : current node's value + total remaining nodes
        return node.value + self._total_helper(node.next)

    def sum_middle_three(self):
        # value error if size smaller than 3
        if self._size < 3:
            raise ValueError("List must have at least 3 nodes")

        # calculate the mid point and walk to it
        mid = self._size // 2
        curr = self.head
        for i in range(mid):
            curr = curr.next

        # if n is odd: nodes at mid-1, mid, mid+1
        if (self._size % 2 != 0):
            return (curr.value + curr.next.value + curr.prev.value)
        # if n is even: nodes at mid-2, mid-1, mid
        else:
            return (curr.value + curr.prev.value + curr.prev.prev.value)

    def median(self):
        if self._size == 0:
            raise ValueError("The list is empty")

        # calculate mid point and walk to it
        mid = self._size // 2
        curr = self.head
        for i in range(mid):
            curr = curr.next

        # if n is odd: the middle value itself
        if (self._size % 2 != 0):
            return curr.value
        # if n is even: average of the two middle values (/ always gives a float, e.g. 9.0)
        else:
            return (curr.prev.value + curr.value) / 2

    def count(self, value):
        return self._count_helper(self.head, value)

    def _count_helper(self, node, value):
        # Base case: empty list, reached end, or passed where value could exist
        if node is None or node.value > value:
            return 0
        if node.value == value:
            return 1 + self._count_helper(node.next, value)

        # Value is still smaller than target: pass along the result from node.next
        return self._count_helper(node.next, value)
