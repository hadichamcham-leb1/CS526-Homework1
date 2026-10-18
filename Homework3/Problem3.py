class Node:
    # shared by both linked stacks (the singly linked one never uses prev)
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class ArrayStack:
    # stack stored in a Python list; the END of the list is the top
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def bottom_to_top(self):
        return self.items


class SinglyLinkedStack:
    # stack stored as a singly linked list; the top is the head,
    # so push and pop never have to walk the list
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            raise IndexError("peek from empty stack")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def bottom_to_top(self):
        return self._collect(self.head)

    def _collect(self, node):
        # the bottom is the LAST node, so collect the rest first, then this node
        if node is None:
            return []
        return self._collect(node.next) + [node.value]


class DoublyLinkedStack:
    # stack stored as a doubly linked list; the top is the tail,
    # and prev lets pop move the tail back without walking
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        node = Node(item)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.tail is None:
            raise IndexError("pop from empty stack")
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None        # the stack became empty
        else:
            self.tail.next = None
        return value

    def peek(self):
        if self.tail is None:
            raise IndexError("peek from empty stack")
        return self.tail.value

    def is_empty(self):
        return self.tail is None

    def bottom_to_top(self):
        return self._collect(self.head)

    def _collect(self, node):
        # the bottom is the head, so this node comes first
        if node is None:
            return []
        return [node.value] + self._collect(node.next)


# The two functions below use only push, pop and is_empty,
# so the same code reverses all three kinds of stack.

def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)                 # base case: the item becomes the bottom
    else:
        top = stack.pop()                # take the top off and keep it
        insert_at_bottom(stack, item)    # put the item under everything else
        stack.push(top)                  # put the kept item back on top


def reverse(stack):
    if stack.is_empty():
        return                           # base case: nothing to reverse
    top = stack.pop()                    # take the top off and keep it
    reverse(stack)                       # reverse everything underneath
    insert_at_bottom(stack, top)         # the old top becomes the new bottom


def show(stack):
    return ", ".join(map(str, stack.bottom_to_top()))


def main():
    for stack in (ArrayStack(), SinglyLinkedStack(), DoublyLinkedStack()):
        for number in range(1, 11):
            stack.push(number)
        print("Before:", show(stack))
        reverse(stack)
        print("After:", show(stack))


if __name__ == "__main__":
    main()
