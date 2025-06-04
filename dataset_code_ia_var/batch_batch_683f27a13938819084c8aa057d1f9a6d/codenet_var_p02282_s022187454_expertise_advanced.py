from sys import setrecursionlimit
setrecursionlimit(10**5)

def main():
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    inorder_index = {v: i for i, v in enumerate(inorder)}

    postorder = []

    def reconstruct(pre_left=0, in_left=0, length=n):
        if length <= 0:
            return
        root = preorder[pre_left]
        idx = inorder_index[root]
        left_size = idx - in_left
        right_size = length - left_size - 1

        reconstruct(pre_left + 1, in_left, left_size)
        reconstruct(pre_left + 1 + left_size, idx + 1, right_size)
        postorder.append(root)

    reconstruct()
    print(*postorder)

if __name__ == "__main__":
    main()