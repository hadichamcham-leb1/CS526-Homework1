import random

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def AddNode(self, value):
        if self.root is None:
            new_node = Node(value)
            self.root = new_node
        else:
            treeInsert(self.root, value)


    def DeleteNode(self, value):
        self.root = treeDelete(self.root, value)


    def FindNode(self, value):
        return findNodeInTree(self.root, value)

    def PrintTree(self):
        printSubTree(self.root)


def findNodeInTree(node, value):
    if node is None:
        return False
    if value == node.value:
        return True
    elif value < node.value:
        return findNodeInTree(node.left, value)
    else:
        return findNodeInTree(node.right, value)

def printSubTree(node):
    if node is None:
        return
    printSubTree(node.left)
    print(node.value)
    printSubTree(node.right)


def treeInsert(node, value):
    if value == node.value:
        return node
    elif value < node.value:
        if node.left is None:
            new_node = Node(value)
            node.left = new_node
            return new_node
        else:
            return treeInsert(node.left, value)
    else:
        if node.right is None:
            new_node = Node(value)
            node.right = new_node
            return new_node
        else:
            return treeInsert(node.right, value)

def getLargest(node):
    # Returns the node with the largest value in the subtree starting at this node
    while node.right is not None:
        node = node.right
    return node


def treeDelete(node, value):

    if node is None:
        # Value doesn't exist
        return None

    if value < node.value:
        # Search left
        node.left = treeDelete(node.left, value)
    elif value > node.value:
        # Search right
        node.right = treeDelete(node.right, value)
    else:
        # We found the node to delete
        # Case 1: Leaf node
        if node.left is None and node.right is None:
            return None

        # Case 2: Only right child
        elif node.left is None:
            return node.right

        # Case 2: Only left child
        elif node.right is None:
            return node.left

        # Case 3: Two children
        else:
            predecessor = getLargest(node.left)
            node.value = predecessor.value
            node.left = treeDelete(node.left, predecessor.value)
    return node


def main():

    # Generate a random number of values between 5 and 50

    size = random.randint(5, 50)

    # Generate unique numbers between 1 and 1000
    input_values = random.sample(range(1, 1001), size)

    print("Input set:", input_values)

    # Create BST
    bst = BST()

    # Insert all values
    for value in input_values:
        bst.AddNode(value)

    print("\nInitial BST:")
    bst.PrintTree()

    # Add a new value
    add_value = random.randint(1, 100)
    while add_value in input_values:
        add_value = random.randint(1, 100)

    print("\nAdd Node:", add_value)
    bst.AddNode(add_value)

    print("BST after addition:")
    bst.PrintTree()

    # Delete an existing value
    delete_value = random.choice(input_values)

    print("\nDelete Node:", delete_value)
    bst.DeleteNode(delete_value)

    print("BST after deletion:")
    bst.PrintTree()

    # Positive test: value exists
    search_value = add_value

    print("\nSearching for:", search_value)

    if bst.FindNode(search_value):
        print("Value found!")
    else:
        print("Value not found.")

    # Negative test: value does not exist
    search_value = random.randint(1, 1000)

    while bst.FindNode(search_value):
        search_value = random.randint(1, 1000)

    print("\nSearching for:", search_value)

    if bst.FindNode(search_value):
        print("Value found!")
    else:
        print("Value not found.")

if __name__ == '__main__':
    main()