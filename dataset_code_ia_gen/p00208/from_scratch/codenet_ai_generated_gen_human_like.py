import sys

def old_to_new(n):
    # 新部屋番号は4と6を除いた数字で表現されるため、4と6をカウントしない7進法のような数体系として考える
    # マッピング中の数字候補は 1,2,3,5,7,8,9,10,11 (ただし数字自体は4と6を除く)
    # 実際は「4」と「6」を飛ばした10進数の変換を7進数変換に置き換える要領
    # 新部屋番号の数字は7つの数字：1,2,3,5,7,8,9 (順番は1～9のうち4と6を除いたもの)
    # n-1 を7進数に変換し、その各桁を数字の配列で置き換えて合成する

    digits = [1,2,3,5,7,8,9]
    n -= 1
    if n < 0:
        return 1

    result = 0
    mul = 1
    while n >= 0:
        r = n % 7
        result += digits[r] * mul
        mul *= 10
        n //= 7
        if n == 0:
            break
    return result

for line in sys.stdin:
    line=line.strip()
    if line == '0':
        break
    n = int(line)
    print(old_to_new(n))