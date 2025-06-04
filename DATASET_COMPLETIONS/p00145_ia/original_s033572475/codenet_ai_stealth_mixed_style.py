n = int(raw_input())
Card = list()
Cost = dict()
for i in xrange(n):
    line = raw_input()
    Card.append(map(int, line.split()))
    Cost[i, i] = 0
def compute_cost(start, end):
    if start == end:
        return 0
    candidates = []
    for mid in range(start, end):
        cost_val = (Card[start][0] * Card[mid][1] * Card[end][1] +
                    Cost[start, mid] + Cost[mid + 1, end])
        candidates.append(cost_val)
    return min(candidates)
length = 1
while length < n:
    pos = 0
    while pos + length < n:
        Cost[(pos, pos + length)] = min([
            Card[pos][0] * Card[k][1] * Card[k + 1][0] * Card[pos + length][1] +
            Cost[(pos, k)] + Cost[(k + 1, pos + length)] for k in range(pos, pos + length)
        ])
        pos += 1
    length += 1
print Cost[0, n - 1]