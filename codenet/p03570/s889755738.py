"""
奇数文字存在する文字がキモ
最低でも答えは奇数文字存在する文字の種類数以上
各ブロックに1つだけ奇数文字の文字を奇数個入れるのが良い

左に１つだけ奇数文字がある & 右に少なくとも一つの奇数文字が残っている
→切断すべき

数だけわかればいい
→分割が必要になる条件を考えればよい？

acababcb
a|ab|ab|b ←分割可能ポイント

2文字の間でどこなら分割を置いていいかは求められる
各範囲に最低1つ置いて

26C2かぁ…ちょっとでかくね→3s?

a|bbb|ccc|a

abc
000

a
100
b
110
b
100

abb  -  a   = bb
100 xor 100 = 000

0 xor 0 = 0
1 xor 0 = 1
1 xor 1 = 0

abcdefghijklmnopqrstuvwxyz
10010000000000000000000000
"""

s = input()

alp = "abcdefghijklmnopqrstuvwxyz"
alpdic = {}

for i in range(26):
    alpdic[alp[i]] = i

dic = {}
now = 0
dic[now] = 0

for i in range(len(s)):

    nalp = alpdic[s[i]]
    now ^= 2 ** nalp

    #print (format(now,"b").zfill(26))

    #dic[now]がokなのは all0かある桁&nalpの桁が1

    ans = float("inf")
    if now in dic:
        ans = dic[now]

    for i in range(26):

        nserch = (2 ** i) ^ now
        if nserch in dic:
            ans = min(ans , dic[nserch])

    if now in dic:
        dic[now] = min(dic[now] , ans + 1)

    else:
        dic[now] = ans + 1

print (max(1,dic[now]))