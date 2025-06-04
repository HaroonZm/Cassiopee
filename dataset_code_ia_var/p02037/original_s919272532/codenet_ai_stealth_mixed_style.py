def read_vals():
    return list(map(int, input().split()))
H, W = read_vals()
(A,B) = tuple(map(lambda x: int(x), input().split(' ')))
remove = 0
for i in range(H//A):
    remove += B * (W//B)
result = H*W - (A*(H//A)*B*(W//B))
print(result)