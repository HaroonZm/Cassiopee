while True:
    vote_n = int(input())
    if vote_n == 0:
        break
    vote_lst = [v for v in input().split()]
    
    vote_cnt = {}
    for i, v in enumerate(vote_lst):
        if not v in vote_cnt:
            vote_cnt[v] = 1
        else:
            vote_cnt[v] += 1
        
        first = 0
        second = 0
        first_key = None
        for k in vote_cnt:
            if first < vote_cnt[k]:
                second = first
                first = vote_cnt[k]
                first_key = k
            elif second < vote_cnt[k]:
                second = vote_cnt[k]
        
        if first - second > vote_n - (i + 1):
            print(first_key, i + 1)
            break
    if first == second:    
        print('TIE')