class BinarySearchTree:
    """
    A class representing a binary search tree (BST).
    Supports insertion and inorder/preorder traversal with detailed process logging.
    """

    def __init__(self):
        """
        Initializes an empty binary search tree.
        """
        self.root = None        # The root node of the BST
        self.order_list = []    # List to store the order of traversed keys

    def insert(self, z):
        """
        Inserts a new node with a given key into the BST.

        Args:
            z (Node): The node to be inserted.
        """
        y = None               # Will be the parent of the new node
        x = self.root          # Start from the root of the BST

        # Traverse the tree to find the right parent for the new node
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left     # Move to the left child if the key is smaller
            else:
                x = x.right    # Move to the right child otherwise

        z.parent = y           # Set the parent of the new node

        # Insert the node in the correct position
        if y is None:          # Tree was empty, so new node is the root
            self.root = z
        elif z.key < y.key:
            y.left = z         # Insert as the left child
        else:
            y.right = z        # Insert as the right child

    def walk_preorder(self, node):
        """
        Performs a preorder traversal (root, left, right) of the BST,
        starting from the given node. The keys are appended to 'order_list'.

        Args:
            node (Node): The current node in traversal.

        Returns:
            None
        """
        if node is None:
            return None
        self.order_list.append(node.key)         # Visit node (root)
        self.walk_preorder(node.left)            # Traverse left subtree
        self.walk_preorder(node.right)           # Traverse right subtree

    def walk_inorder(self, node):
        """
        Performs an inorder traversal (left, root, right) of the BST,
        starting from the given node. The keys are appended to 'order_list'.

        Args:
            node (Node): The current node in traversal.

        Returns:
            None
        """
        if node is None:
            return None
        self.walk_inorder(node.left)             # Traverse left subtree
        self.order_list.append(node.key)         # Visit node (root)
        self.walk_inorder(node.right)            # Traverse right subtree

    def print_nodes(self):
        """
        Prints the keys of the BST nodes as two lines:
        - The first line is the inorder traversal (sorted order).
        - The second line is the preorder traversal.

        Returns:
            None
        """
        # Print inorder traversal
        self.order_list = []
        self.walk_inorder(self.root)
        inorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(inorder_str))

        # Print preorder traversal
        self.order_list = []
        self.walk_preorder(self.root)
        preorder_str = ' '.join(map(str, self.order_list))
        print(' {}'.format(preorder_str))


class Node:
    """
    A class representing a single node in a binary search tree.

    Attributes:
        key (int): The value of the node.
        parent (Node): The parent node.
        left (Node): The left child node.
        right (Node): The right child node.
    """
    def __init__(self, key):
        """
        Initializes a node with a given key.
        
        Args:
            key (int): The value to be stored in the node.
        """
        self.key = key          # The node's key value
        self.parent = None      # Parent node
        self.left = None        # Left child
        self.right = None       # Right child


# Main execution section: Builds and manages the binary search tree
n = int(input())              # Number of operations to perform
tree = BinarySearchTree()     # Create an empty BST

for _ in range(n):
    command = input().split(' ')
    # If the input line has only one part, it's the 'print' command
    if len(command) == 1:
        tree.print_nodes()
    else:
        opecode, operand = command[0], int(command[1])
        node = Node(operand)
        tree.insert(node)