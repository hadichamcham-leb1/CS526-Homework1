class Node:
    # One box in the chain: a value and an arrow to the next node.
    def __init__(self, value):
        self.value = value
        self.next = None  # None means this is the last node


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # ---------- Create ----------

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            # empty list: the new node is both head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # attach after the old tail, then move the tail forward
            self.tail.next = new_node
            self.tail = new_node

        self.count = self.count + 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the new node at the old head, then move the head back
            new_node.next = self.head
            self.head = new_node

        self.count = self.count + 1

    def insert(self, index, value):
        # index == count is allowed: it means "add at the end"
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")

        # the two ends are handled by prepend and append
        if index == 0:
            self.prepend(value)
            return

        if index == self.count:
            self.append(value)
            return

        new_node = Node(value)

        # walk to the node just BEFORE the insertion point
        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        # connect the new node forward first, so the rest of the chain is not lost
        new_node.next = temp.next
        temp.next = new_node

        self.count = self.count + 1

    # ---------- Read ----------

    def get(self, index):
        # valid indexes are 0 to count - 1
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        # there is no stored position, so walk from the head
        temp = self.head

        for i in range(index):
            temp = temp.next

        return temp.value

    def find(self,value):
        temp = self.head
        index = 0

        # walk until a node holds the value, or the chain ends
        while temp is not None:
            if temp.value == value:
                return index

            temp = temp.next
            index += 1

        return -1

    def __len__(self):
        # special method: Python calls it for len(my_list)
        return self.count

    # ---------- Update ----------

    def update(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        temp = self.head

        for i in range(index):
            temp = temp.next

        temp.value = value

    # ---------- Delete ----------

    def delete(self,value):
        if self.head is None:
            return False

        # deleting the head: just move head forward
        if self.head.value == value:
            self.head = self.head.next
            self.count -= 1

            # the list became empty, so there is no tail either
            if self.count == 0:
                self.tail = None

            return True

        # otherwise look one node ahead, so temp stays on the node BEFORE the match
        temp = self.head

        while temp.next is not None:
            if temp.next.value == value:
                # if the removed node was the tail, the tail moves back
                if temp.next == self.tail:
                    self.tail = temp

                # skip over the removed node
                temp.next = temp.next.next
                self.count -= 1
                return True

            temp = temp.next

        return False

    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        # deleting the head: save its value, then move head forward
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.count -= 1

            if self.count == 0:
                self.tail = None

            return value

        # walk to the node just BEFORE the one being removed
        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        deleted = temp.next
        temp.next = deleted.next

        # if the removed node was the tail, the tail moves back
        if deleted == self.tail:
            self.tail = temp

        self.count -= 1

        return deleted.value

    # ---------- Print ----------

    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        # collect the values as text, then join them with arrows
        temp = self.head
        values = []

        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next

        print(" -> ".join(values))
