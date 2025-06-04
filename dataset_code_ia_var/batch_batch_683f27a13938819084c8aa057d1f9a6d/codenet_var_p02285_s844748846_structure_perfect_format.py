class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def delete_connect(self, parent, child):
        if parent:
            if parent.val > self.val:
                parent.left = child
            else:
                parent.right = child
        if child:
            child.parent = parent

    def delete(self):
        left = self.left
        right = self.right
        if not left and not right:
            self.delete_connect(self.parent, None)
        elif not left and right:
            self.delete_connect(self.parent, right)
        elif left and not right:
            self.delete_connect(self.parent, left)
        else:
            next_node = right.get_leftmost()
            self.val = next_node.val
            next_node.delete()

    def get_leftmost(self):
        if self.left:
            return self.left.get_leftmost()
        return self

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node: Node):
        if not self.root:
            self.root = node
            return
        cur = self.root
        while cur:
            if node.val > cur.val:
                if cur.right:
                    cur = cur.right
                    continue
                else:
                    cur.right = node
                    node.parent = cur
                    return
            else:
                if cur.left:
                    cur = cur.left
                    continue
                else:
                    cur.left = node
                    node.parent = cur
                    return

    def find(self, val):
        cur = self.root
        while cur:
            if cur.val == val:
                return "yes"
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return "no"

    def find_node(self, val):
        cur = self.root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def delete(self, val):
        node = self.find_node(val)
        if node:
            node.delete()

def main():
    preorder = []
    def preorder_walk(node):
        preorder.append(str(node.val))
        if node.left:
            preorder_walk(node.left)
        if node.right:
            preorder_walk(node.right)
    inorder = []
    def inorder_walk(node):
        if node.left:
            inorder_walk(node.left)
        inorder.append(str(node.val))
        if node.right:
            inorder_walk(node.right)
    n = int(input())
    bst = BinarySearchTree()
    for _ in range(n):
        op = input().strip().split()
        if op[0] == "insert":
            bst.insert(Node(int(op[1])))
        elif op[0] == "print":
            preorder = []
            inorder = []
            preorder_walk(bst.root)
            inorder_walk(bst.root)
            print(" " + " ".join(inorder))
            print(" " + " ".join(preorder))
        elif op[0] == "find":
            print(bst.find(int(op[1])))
        elif op[0] == "delete":
            bst.delete(int(op[1]))

if __name__ == "__main__":
    main()