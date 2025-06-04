n = int(input())
pre = [int(x) for x in input().split()]
ino = [int(x) for x in input().split()]
post = []

def build_postorder(l, r, pre_index):
    if l >= r:
        return pre_index
    root = pre[pre_index]
    pre_index += 1
    m = 0
    for i in range(l, r):
        if ino[i] == root:
            m = i
            break
    pre_index = build_postorder(l, m, pre_index)
    pre_index = build_postorder(m + 1, r, pre_index)
    post.append(root)
    return pre_index

build_postorder(0, n, 0)
print(' '.join(str(x) for x in post))