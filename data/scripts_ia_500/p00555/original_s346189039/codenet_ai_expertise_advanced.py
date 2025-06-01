n, m, d = map(int, input().split())
field = [input() for _ in range(n)]

def count_slots(lines):
    return sum(len(segment) - d + 1 for line in lines for segment in line.split('#') if len(segment) >= d)

ans = count_slots(field) + count_slots(zip(*field))
print(ans)