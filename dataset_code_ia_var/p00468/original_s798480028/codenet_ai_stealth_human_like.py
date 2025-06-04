import sys
import itertools

readline = sys.stdin.readline

# ok, let's go through input until both are zero
while True:
    N = int(readline())
    M = int(readline())
    if N == 0 and M == 0:
        break

    pairs = set()
    for _ in range(M):  # I just use range, I don't like xrange
        # unpacking stuff
        nums = readline().split()
        a = int(nums[0])
        b = int(nums[1])
        pairs.add((a, b))
        pairs.add((b, a))  # it's undirected I think?

    count = 0  # I like calling things 'count'
    for i in range(2, N+1):  # not sure if inclusive but let's trust it
        if (1, i) in pairs:
            count += 1
        else:
            for j in range(2, N+1):
                if (1, j) in pairs and (j, i) in pairs:
                    count += 1
                    break  # only counting once per i I think

    print(count)  # in python3, need parens!