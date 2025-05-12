from collections import defaultdict

def II(): return int(input())
def ILI(): return list(map(int, input().split()))

def read():
    H, W = ILI()
    count = defaultdict(int)
    for __ in range(H):
        sen = str(input())
        for i in range(W):
            count[sen[i]] += 1
    return H, W, count

def solve(H, W, count):
    odd = 0
    num_2 = 0
    num_4 = 0
    for val in count.values():
        div_2, mod_2 = divmod(val, 2)
        odd += mod_2
        div_2 *= 2
        div_4, mod_4 = divmod(div_2, 4)
        num_4 += div_4 * 4
        num_2 += mod_4
    ans = 0
    if H % 2 == 0:
        if W % 2 == 0:
            if odd == 0:
                if num_4 == H * W:
                    ans = "Yes"
                else:
                    ans = "No"
            else:
                ans = "No"
        else:
            if odd != 0:
                ans = "No"
            else:
                if num_2 > H:
                    ans = "No"
                else:
                    ans = "Yes"
    else:
        if W % 2 == 0:
            if odd != 0:
                ans = "No"
            else:
                if num_2 > W:
                    ans = "No"
                else:
                    ans = "Yes"
        else:
            if odd != 1:
                ans = "No"
            else:
                if num_2 > (W - 1) + (H - 1):
                    ans = "No"
                else:
                    ans = "Yes"
    return ans

def main():
    params = read()
    print(solve(*params))

if __name__ == "__main__":
    main()