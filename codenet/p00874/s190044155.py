from collections import Counter
while True:
    W, D = map(int, input().split())
    if not (W | D):
        break
    hw = [int(x) for x in input().split()]
    hd = [int(x) for x in input().split()]

    cnt_hw = Counter(hw)
    cnt_hd = Counter(hd)
    print(min(sum(hw) + sum(max(0, v - cnt_hw[k]) * k for k, v in cnt_hd.items()),
              sum(hd) + sum(max(0, v - cnt_hd[k]) * k for k, v in cnt_hw.items())))