# Input Candidates

def compare(x, y):
    if x[1] == y[1]:
        return cmp(x[0], y[0])
    else:
        return cmp(x[1], y[1]) * -1

while True:
    n = int(raw_input())
    if n == 0:
        break

    dic = {}
    for i in range(n):
        words = raw_input().strip().split()
        for word in words:
            dic[word] = dic.setdefault(word, 0) + 1

    candidate = []
    key = raw_input().strip()
    for k, v in dic.items():
        if k.startswith(key):
            candidate.append((k, v))

    candidate.sort(compare)

    if candidate:
        print ' '.join([word[0] for word in candidate[:5]])
    else:
        print 'NA'