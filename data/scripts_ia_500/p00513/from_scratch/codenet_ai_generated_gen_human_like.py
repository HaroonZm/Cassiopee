import sys

def is_valid_area(area):
    # area = 2xy + x + y
    # = (2x + 1)(2y + 1)/2 - 1/2 は整数ではないので違う形で考える
    # 式変形すると area + 1 = (2x + 1)(y + 1) - x - y
    # でもわかりにくいので、ループしてxを固定し、yを求める方法を使う方が良い
    # ただし、x,yは正整数なのでx,y>=1
    # 1LDKの面積の式は 2xy + x + y
    # y = (area - x) / (2x + 1) かつ yは正整数

    # xは正整数なので 1 <= x <= area
    # 最大xは式よりある程度絞れる
    max_x = int((area//2)**0.5) + 2
    for x in range(1, max_x):
        denom = 2*x + 1
        nom = area - x
        if nom <= 0:
            continue
        if nom % denom == 0:
            y = nom // denom
            if y >= 1:
                return True
    return False

input = sys.stdin.readline
N = int(input())
count_invalid = 0
for _ in range(N):
    area = int(input())
    if not is_valid_area(area):
        count_invalid += 1
print(count_invalid)