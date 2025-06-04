class Node:
    """
    Represents a single node within a binary search tree.
    
    Attributes:
        key (int): Value held by the node.
        left (Node): Reference to the left child.
        right (Node): Reference to the right child.
        parent (Node): Reference to the parent node.
    """
    def __init__(self, key=None):
        """
        Initializes a new Node with optional key, no children, and no parent.

        Args:
            key (int, optional): Value to be stored in the node. Defaults to None.
        """
        self.left = None      # Pointer to left child node
        self.right = None     # Pointer to right child node
        self.parent = None    # Pointer to parent node
        self.key = key        # Value stored at this node

def insert(T, z):
    """
    Inserts a node z into the binary search tree with root T.

    Args:
        T (Node): The root of the binary search tree.
        z (Node): The node to be inserted.

    Returns:
        Node: The (possibly new) root of the binary search tree after insertion.
    """
    x = T         # Start traversal at root
    y = None      # y will track the parent of the current node x
    # Traverse the tree to find the correct location for z
    while isinstance(x, Node):
        y = x
        if z.key < x.key:    # Go left if the key to insert is less than the current node's key
            x = x.left
        else:
            x = x.right      # Otherwise, go right
    z.parent = y             # Set the parent of z to y
    if y is None:
        T = z               # The tree was empty; the new node is now the root
    elif z.key < y.key:
        y.left = z          # Attach z as left child
    else:
        y.right = z         # Attach z as right child
    return T

def preorder(u):
    """
    Performs a preorder traversal (Root-Left-Right) of the binary tree.

    Appends the string representation of visited keys to the global pripre list.

    Args:
        u (Node): The current node being visited.
    """
    if not isinstance(u, Node):
        return
    pripre.append(str(u.key))  # Visit the root node
    preorder(u.left)           # Traverse left subtree
    preorder(u.right)          # Traverse right subtree

def inorder(u):
    """
    Performs an inorder traversal (Left-Root-Right) of the binary tree.

    Appends the string representation of visited keys to the global priin list.

    Args:
        u (Node): The current node being visited.
    """
    if not isinstance(u, Node):
        return
    inorder(u.left)           # Traverse left subtree
    priin.append(str(u.key))  # Visit the root node
    inorder(u.right)          # Traverse right subtree

# Main driver code
try:
    # Read the number of commands to be processed
    m = int(input())
except:
    # For Python 2 compatibility, use raw_input if input fails (not required in Python 3+)
    m = int(raw_input())

root = None  # Initialize the root of the binary search tree to None

for i in range(m):  # Iterate over the number of commands
    try:
        # Read the user command as a list of strings; for Python 3 use input()
        cmd = input().split()
    except:
        # For Python 2 compatibility, use raw_input
        cmd = raw_input().split()
    if cmd[0] == "print":
        # If the command is 'print', output the inorder and preorder traversals
        pripre = []   # List to hold preorder traversal result
        priin = []    # List to hold inorder traversal result
        preorder(root)
        inorder(root)
        # Print inorder traversal (sorted order for BST)
        print(' ' + ' '.join(priin))
        # Print preorder traversal (root-left-right)
        print(' ' + ' '.join(pripre))
    else:
        # Insert command: second argument is the key to insert
        key = int(cmd[1])
        z = Node(key)       # Create a new node with the given key
        root = insert(root, z)  # Insert the node and update the root if necessary