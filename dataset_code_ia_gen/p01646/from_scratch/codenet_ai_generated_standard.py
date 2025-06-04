def can_be_sorted_lex(words):
    from collections import defaultdict, deque
    graph = defaultdict(set)
    indegree = {c:0 for c in set(''.join(words))}
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break
        else:
            if len(w1) > len(w2):
                return False
    q = deque([c for c in indegree if indegree[c]==0])
    count = 0
    while q:
        u = q.popleft()
        count += 1
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    return count == len(indegree)

while True:
    n = int(input())
    if n == 0:
        break
    words = [input().strip() for _ in range(n)]
    print("yes" if can_be_sorted_lex(words) else "no")