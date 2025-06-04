N, K = map(int, input().split())
S = input()

# Ok, we need to process S by grouping same chars together... don't love this style but whatever
blocs = []
block_ct = 1
last = S[0]
count = 1

for j in range(1, N-1):
    if S[j] == last:
        count += 1
    else:
        blocs.append(count)
        count = 1
        last = S[j]
        block_ct += 1

if S[N-1] == last:
    count += 1
    blocs.append(count)
else:
    blocs.append(count)
    count = 1
    last = S[N-1]
    blocs.append(count)
    block_ct += 1

# print(blocs) # Debug, just in case

num = 2*K + 1

# Ya it's kind of brute force
if block_ct == 1 or block_ct == 2 or num >= block_ct:
    print(N-1)
elif num < block_ct:
    left = block_ct - num
    print(N - left - 1)
# probably missed a weird edge case? oh well