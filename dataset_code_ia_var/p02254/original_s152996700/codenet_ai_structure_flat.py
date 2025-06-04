import heapq

S = input()

chars = [[0, n] for n in range(256)]
for s in S:
    chars[ord(s)][0] += 1

counts = []
for char in chars:
    if not char[0]:
        continue
    heapq.heappush(counts, [char[0], char[1], None, None, char])

while len(counts) > 1:
    a = heapq.heappop(counts)
    b = heapq.heappop(counts)
    heapq.heappush(counts, [a[0] + b[0], -1, a, b])

root = heapq.heappop(counts)
codes = {}
stack = [(root, "")]
while stack:
    node, code = stack.pop()
    if node[1] < 0:
        stack.append((node[2], code + "0"))
        stack.append((node[3], code + "1"))
    else:
        codes[chr(node[1])] = code

count = 0
for s in S:
    count += len(codes[s])

if len(set(S)) == 1:
    print(len(S))
else:
    print(count)