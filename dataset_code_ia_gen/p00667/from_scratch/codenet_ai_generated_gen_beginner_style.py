mod = 100000007

# 各数字が表す文字数
chars = {
    '1':5,
    '2':5,
    '3':5,
    '4':5,
    '5':5,
    '6':5,
    '7':5,
    '8':3,
    '9':5,
    '0':3
}

import sys

for line in sys.stdin:
    s = line.strip()
    if s == '#':
        break
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = 1
    i = 1
    while i <= n:
        # 一文字目
        dp[i] = (dp[i] + dp[i-1]) % mod
        # 前の文字と同じならまとめてとる
        j = i-1
        while j > 0 and s[j-1] == s[i-1]:
            length = i - j + 1 - 1
            length = i - j + 1 - 1
            length = i - j + 1 - 1
            # だけど重複処理はいらない,ここは次にまとめるのでスキップ
            j -= 1
        i += 1

    # 考え方を変える: DPで可能な区切りで文字列に分割して、
    # 各区間は同じ数字の連続で、連続数を何通りに分けるか?という問題
    # よって以下に書き直す

import sys

mod = 100000007

chars = {
    '1':5,
    '2':5,
    '3':5,
    '4':5,
    '5':5,
    '6':5,
    '7':5,
    '8':3,
    '9':5,
    '0':3
}

for line in sys.stdin:
    s = line.strip()
    if s == '#':
        break
    n = len(s)
    dp = [0]*(n+1)
    dp[0] = 1
    i = 0
    while i < n:
        c = s[i]
        length = chars[c]
        j = i+1
        while j <= n and j - i <= length and j <= n and s[i:j] == c*(j - i):
            dp[j] = (dp[j] + dp[i]) % mod
            j += 1
        i += 1
    print(dp[n] % mod)