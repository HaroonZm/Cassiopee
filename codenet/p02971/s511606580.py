N = int(input())
ai = []
for i in range(N):
    ai.append(int(input()))
first = max(ai)
ai_ = ai[:]
ai_.remove(first)
second = max(ai_)

for x in ai:
    if x == first:
        print(second)
    else:
        print(first)