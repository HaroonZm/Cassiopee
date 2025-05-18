ans_list = []
# m:1000, c:100. x:10, i:1
n = int(input())

mcxi = list("mcxi")[::-1]

def value(string):
    res = 0
    for i in range(4):
        index = string.find(mcxi[i])
        if index != -1:
            if string[index-1] in mcxi:
                res += pow(10,i)
            else:
                res += int(string[index-1]) * pow(10,i)
    return res

def MCXI(integer):
    res = ""
    for i in range(4):
        remain = integer % 10
        integer //= 10
        if remain == 1:
            res = mcxi[i] + res
        elif remain == 0:
            pass
        else:
            res = str(remain) + mcxi[i] + res
    return res

for _ in range(n):
    s,t = input().split()
    ans = MCXI(value(s) + value(t))
    ans_list.append(ans)

for ans in ans_list:
    print(ans)