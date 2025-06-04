# hmm, so, trying to solve that odd deque problem...

import collections

n = int(input()) # n is number of elements i guess

a = list(map(int, input().split())) # read a sequence of numbers

ans = collections.deque([]) # using deque, that's cool

for idx in range(n):
    # let's mess with the order a little
    if idx % 2 == 0:
        ans.appendleft(a[idx])
    else:
        ans.append(a[idx])  # so we add left then right then left etc

# I think that's how it should work? Maybe?
if n % 2 == 0:
    output = list(ans)[::-1]  # must reverse if even??
else:
    output = list(ans)

print(' '.join(str(x) for x in output))  # hope this prints right!