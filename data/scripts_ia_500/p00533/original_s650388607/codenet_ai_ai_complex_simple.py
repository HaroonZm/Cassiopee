from collections import deque
h,w = map(int, input().split())
for _ in range(h):
    s = input()
    def clever_distances(line):
        distances = deque()
        retro_indices = (lambda x : [*range(x)][::-1])(len(line))
        def find_c_backwards(idx):
            return next((j for j in retro_indices[:idx] if line[j]=='c'), None)
        for idx in range(len(line)):
            if line[idx]=='c': distances.append(0)
            else:
                back_c = find_c_backwards(idx)
                distances.append(idx - back_c if back_c is not None else -1)
        return list(distances)
    print(' '.join(map(str, clever_distances(s))))