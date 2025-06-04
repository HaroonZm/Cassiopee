import sys
import math

MAX_M = 10**6

def sieve(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    for i in range(2,int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i,n+1,i):
                prime[j] = False
    return prime

prime = sieve(MAX_M)

def neighbors(c):
    # from c you can go down to c+current_level, c+current_level+1 or c+current_level-1
    # we must find the row of c and the row below to determine possible next caves
    # the cave numbering spirals but effectively caves are arranged in rows
    # Number of caves in each row increases by 6 each time:
    # row 1: 1 cave (#1)
    # row 2: 6 caves (#2 to #7)
    # row 3: 12 caves (#8 to #19)
    # row 4: 18 caves (#20 to #37)
    # ...
    # Number of caves in row k = 6*(k-1), except row 1 which has 1 cave
    # Cumulative caves up to row k:
    # sum_{i=1}^k row_caves(i) = 1 + 6(1+2+...+(k-1)) = 1 + 3*k*(k-1)
    # So cumulative(k) = 1 + 3*k*(k-1)
    # We can find row of cave c by binary search on k such that cumulative(k-1) < c <= cumulative(k)
    
    # We find the row of c
    if c == 1:
        current_row = 1
    else:
        # Solve 1 + 3*k*(k-1) >= c
        # 3k^2 -3k +1 - c >= 0
        # 3k^2 - 3k + (1 - c) >= 0
        # Use formula for k
        # Because k is row >=1
        # Find smallest k s.t 1+3*k*(k-1)>=c
        # k^2 - k + (1-c)/3 >=0
        # Discriminant: D = 1 -4*(1-c)/3 = 1 -4/3 +4c/3 = (3 -4 +4c)/3 = (4c -1)/3
        D = 4*c -1
        k = int(math.ceil((1 + math.sqrt(D/3))/2))
        current_row = k
    
    # cumulative(k) = 1 + 3*k*(k-1)
    # cumulative(k-1) = 1 + 3*(k-1)*(k-2)
    prev_cumulative = 1 + 3*(current_row-1)*(current_row-2) if current_row >1 else 0
    row_start = prev_cumulative +1
    idx_in_row = c - row_start  # zero-based index in current row
    row_len = 1 if current_row ==1 else 6*(current_row-1)
    next_row = current_row +1
    next_row_len = 6*(next_row-1)
    next_row_start = 1 + 3*next_row*(next_row-1-1)  # 1 + 3*next_row*(next_row-1), adjusted
    
    # The caves directly below c are in next row, their indices:
    # From problem description descend down to either:
    # - directly below => same idx_in_row in next row
    # - one left of directly below => idx_in_row - 1 in next row if >=0
    # - one right of directly below => idx_in_row + 1 in next row if < next_row_len
    next_caves = []
    base = 1 + 3*next_row*(next_row-1)  # cumulative(next_row-1) + 1 = start of next row
    if next_row_start != base:
        # recalc next row start correctly:
        next_row_start = base
    for ni in [idx_in_row -1, idx_in_row, idx_in_row +1]:
        if 0 <= ni < next_row_len:
            nc = next_row_start + ni
            next_caves.append(nc)
    return next_caves

def main():
    input = sys.stdin.readline
    memo = {}

    def dfs(c):
        if c > m:
            return (0,0)  # no prime caves on path
        if c in memo:
            return memo[c]
        nxts = neighbors(c)
        best_count = 0
        best_end = 0
        for nc in nxts:
            ccount, cend = dfs(nc)
            if ccount > best_count or (ccount == best_count and cend > best_end):
                best_count = ccount
                best_end = cend
        if prime[c]:
            best_count += 1
            best_end = c
        memo[c] = (best_count,best_end)
        return memo[c]

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        m,n = map(int,line.split())
        if m==0 and n==0:
            break
        memo.clear()
        # Global m for dfs
        global m
        m = m
        cnt,end = dfs(n)
        if cnt ==0:
            print("0 0")
        else:
            print(cnt,end)

if __name__=="__main__":
    main()