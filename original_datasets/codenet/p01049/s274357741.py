n = int(input())
a, d = map(int, input().split())
mem = {}

def get_mem(num):
    if num in mem:return mem[num]
    else:return num

m = int(input())
for _ in range(m):
  x, y, z = map(int, input().split())
  if x == 0:
    ny, nz = get_mem(y), get_mem(z)
    mem[y] = nz
    mem[z] = ny
  if x == 1:
    nz = get_mem(z)
    mem[y] = nz
k = get_mem(int(input()))
print(a + d * (k - 1))