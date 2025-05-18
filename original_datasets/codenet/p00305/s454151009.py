from sys import stdin
from itertools import accumulate

def solve():
    file_input = stdin
    
    N = int(file_input.readline())
    G = tuple(tuple(map(int, line.split())) for line in file_input)
    
    # accumulated rows
    ar = ((0,) + tuple(accumulate(line)) for line in G)
    
    # accumulated columns
    ac = ((0,) + tuple(accumulate(line)) for line in zip(*G))
    ac_1 = next(ac)
    ac = tuple(zip(*ac))
    
    ans = 0
    for i, t1 in enumerate(zip(G, ar, ac, ac_1)):
        G_i, ar_i, ac_i, ac_1i = t1
        ar_ii = ar_i[i]
        for j, t2 in enumerate(zip(G[i:], ar_i[i+1:], ac[i+1:], ac_1[i+1:]), start=i):
            G_j, ar_ij, ac_j, ac_1j = t2
            if ar_ij - ar_ii > ans:
                ans = ar_ij - ar_ii
                
            if i == j:
                continue
            
            col_max = ac_1j - ac_1i
            
            for ac_jk, ac_ik, G_ik, G_jk in zip(ac_j, ac_i, G_i[1:], G_j[1:]):
                col = ac_jk - ac_ik
                
                if col_max > 0:
                    c_ans = col_max + col
                    if c_ans > ans:
                        ans = c_ans
                else:
                    if col > ans:
                        ans = col
                
                t_col_max = col_max + G_ik + G_jk
                if t_col_max > col:
                    col_max = t_col_max
                else:
                    col_max = col
    print(ans)

solve()