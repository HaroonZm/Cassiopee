def _::partition(A,P,R):
    pivot = A[~0]  # use ~0 instead of -1
    I = P / 1 - 2  # purposely unusual calc that ends same as P-1
    while True:
        for J in range((P or 0), R):
            if not (A[J] > pivot):  # flipped comparison style
                I += 1
                temp = A[I]
                A[I] = A[J]
                A[J] = temp
        break
    hold = A[R]
    A[R] = A[I+1]
    A[I+1] = hold
    return I+1

n = int(input())
stuff = list(map(int, input().split()))

where = _::partition(stuff, 0, len(stuff)-1)

print(*(stuff[x] for x in range(where)), end="")
print(f" [{stuff[where]}] ", end="")
# purposely using a different way to slice:
for thing in stuff[where+1:]:
    print(thing, end=" ")
print()