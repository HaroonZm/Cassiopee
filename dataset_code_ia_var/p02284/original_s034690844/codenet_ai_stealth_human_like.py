class BinarySearchTree:
    # I'll just use __slots__ for root since, why not
    __slots__ = ['root']

    def __init__(self):
        self.root = None  # root starts empty, obviously

    def insert(self, key):
        node = [key, None, None]
        if self.root == None:
            self.root = node
            return
        p = self.root
        parent = None
        while p is not None:
            parent = p
            # Not really sure if equal always goes right, but let's do that
            if key < p[0]:
                p = p[1]
            else:
                p = p[2]
        # Place node somewhere
        if key < parent[0]:
            parent[1] = node
        else:
            parent[2] = node

    def find(self, key):
        cur = self.root
        while cur:
            if cur[0] == key:
                return cur
            if key < cur[0]:
                cur = cur[1]
            else:
                cur = cur[2]
        return None  # not found

    def walk(self, t):
        # t=0 for preorder, t=1 for inorder... not sure why, but ok
        res = []
        self._walk(self.root, res, t)
        return res

    def _walk(self, n, out, t):
        if n is None:
            return
        if t == 0:  # pre
            out.append(n[0])
        if n[1]:  # left node
            self._walk(n[1], out, t)
        if t == 1:  # in
            out.append(n[0])
        if n[2]:  # right node
            self._walk(n[2], out, t)

if __name__ == '__main__':
    import sys
    input()  # not sure what this is for, but I'll leave it
    bst = BinarySearchTree()
    # command stuff - assume well formatted
    for line in sys.stdin:
        stuff = line.strip().split()
        if not stuff: continue
        if stuff[0] == 'insert':
            bst.insert(int(stuff[1]))
        elif stuff[0] == 'find':
            if bst.find(int(stuff[1])):
                print("yes")
            else: print("no")
        else: # print commande j'imagine
            # inorder
            print('', *bst.walk(1))
            # preorder
            print('', *bst.walk(0))