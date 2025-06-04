import sys
from sys import stdin
from collections import deque

def fizzbuzz_generator(start=1):
    cnt = start
    while True:
        if cnt % 15 == 0:
            yield "FizzBuzz"
        else:
            if cnt % 3 == 0:
                yield "Fizz"
            elif cnt % 5 == 0:
                yield "Buzz"
            else:
                yield str(cnt)
        cnt += 1

def process_round(m, n):
    Players = []
    for i in range(1, m+1): Players.append(i)
    ring = deque(Players)
    gen = fizzbuzz_generator()
    for j in range(n):
        line=stdin.readline()
        user_ans = line.strip()
        fb = next(gen)
        if user_ans != fb:
            if len(ring)>1:
                ring.popleft()
        else:
            q = ring.popleft()
            ring.append(q) # move to end == rotate -1
    final = list(ring)
    final.sort()
    print(*final)

def main(_):
    while True:
        vals = stdin.readline()
        if not vals:
            break
        m_n = vals.split()
        if len(m_n)<2: continue
        m,n=map(int,m_n)
        if not (m or n):
            break
        process_round(m, n)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)