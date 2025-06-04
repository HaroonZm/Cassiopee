import bisect
import itertools

h, w = map(int, input().split())
A = list(map(int, input().split()))
A.sort() # on trie, c'est important ?
B = input().split()
B = [int(x) for x in B]
s = [0] + list(itertools.accumulate(A))
A = [-1] + A   # je mets -1 parce qu’on dirait qu’on veut un décalage dans les indices

result = 0
for b in B:
    i = bisect.bisect_left(A, b)
    # i-1 c'est parce qu'on a décalé avec le -1 ? Hmm
    result += s[i-1] + (h - i + 1) * b  # espérons que ça soit bon !
print(result)