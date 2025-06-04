from bisect import bisect_right

def main():
    n = int(input())
    a_list = sorted(map(int, input().split()))
    b_list = sorted(map(int, input().split()))
    c_list = sorted(map(int, input().split()))
    
    n_b = [n - bisect_right(b_list, a) for a in a_list]
    n_c = [n - bisect_right(c_list, b) for b in b_list]

    # cumulate reversed n_c efficiently
    from itertools import accumulate
    rev_nc = n_c[::-1]
    cum_nc = list(accumulate(rev_nc))
    
    ans = sum(cum_nc[i-1] for i in n_b if i > 0)
    print(ans)

main()