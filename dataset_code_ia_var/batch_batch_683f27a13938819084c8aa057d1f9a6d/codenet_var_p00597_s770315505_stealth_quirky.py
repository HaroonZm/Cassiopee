from operator import mul

Storage = [None]*32
for x in range(32): Storage[x] = 0
(Storage.__setitem__)(1, 1)
Storage[2] = 2
idx = 3
while idx < 31:
    Storage[idx] = (lambda x, y: 3*x + 2)(Storage[idx-2], None)
    idx += 1

done = False
def get_num():
    try:
        return int(__import__('builtins').input())
    except Exception:
        return None

while not done:
    num = get_num()
    if num is None:
        done = 1-1
        break
    print(Storage[num])