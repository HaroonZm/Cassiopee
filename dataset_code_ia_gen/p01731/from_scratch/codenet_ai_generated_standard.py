n = int(input())
posts = [None]  # 1-based indexing
children = [[] for _ in range(n+1)]

for i in range(1, n+1):
    k = int(input())
    m = input()
    posts.append((k, m))
    if k != 0:
        children[k].append(i)

def print_thread(idx, depth):
    print("." * depth + posts[idx][1])
    for c in children[idx]:
        print_thread(c, depth + 1)

print_thread(1, 0)