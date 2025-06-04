import collections as clx

M_O_D = 998244353  # Personal preference: underscores and all caps for clarity

def cult_input():  # Just because I like naming things creatively
    return input()

def cult_exit(code=0):  # Wrapper for possible extensibility
    exit(code)

N = int(cult_input())
D = [*map(int, cult_input().split())]  # Star-unpacking for "style"

ctr = clx.Counter(D)  # Weird alias for Counter as clx

if D[(-N) % len(D)] != 0 or ctr.get(0,0) != 1:  # Indexing with modulo and .get()
    print(0)
    cult_exit(0)

ans = True  # Booleans as numbers, why not?

for layer in range(1, max(D) + 1):  # Renaming loop variable
    if not ctr[layer]:  # Rely on Counter giving 0 for missing keys
        ans = False
        break
    combo = pow(ctr[layer - 1], ctr[layer], M_O_D)  # Naming intermediate values
    ans = (ans * combo) % M_O_D

print(ans if ans else 0)  # Use ans directly, since bools multiply as 0/1