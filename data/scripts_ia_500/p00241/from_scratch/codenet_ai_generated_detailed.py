# 四元数の乗算を行うプログラム

# 四元数 q = x + y i + z j + w k の積は以下の式で計算できる。
# q1 = x1 + y1 i + z1 j + w1 k
# q2 = x2 + y2 i + z2 j + w2 k
#
# 積 q3 = q1 * q2 = x3 + y3 i + z3 j + w3 k
#
# i, j, k の積のルール
# i^2 = j^2 = k^2 = -1
# ij = k   ji = -k
# jk = i   kj = -i
# ki = j   ik = -j
#
# よって積は、
# x3 = x1*x2 - y1*y2 - z1*z2 - w1*w2
# y3 = x1*y2 + y1*x2 + z1*w2 - w1*z2
# z3 = x1*z2 - y1*w2 + z1*x2 + w1*y2
# w3 = x1*w2 + y1*z2 - z1*y2 + w1*x2

def quaternion_multiply(q1, q2):
    x1, y1, z1, w1 = q1
    x2, y2, z2, w2 = q2
    x3 = x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2
    y3 = x1 * y2 + y1 * x2 + z1 * w2 - w1 * z2
    z3 = x1 * z2 - y1 * w2 + z1 * x2 + w1 * y2
    w3 = x1 * w2 + y1 * z2 - z1 * y2 + w1 * x2
    return (x3, y3, z3, w3)

def main():
    import sys

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        n = line.strip()
        if n == '0':
            # 入力の終わり
            break
        n = int(n)
        for _ in range(n):
            data = sys.stdin.readline().strip().split()
            # x1, y1, z1, w1, x2, y2, z2, w2
            q1 = tuple(map(int, data[0:4]))
            q2 = tuple(map(int, data[4:8]))
            x3, y3, z3, w3 = quaternion_multiply(q1, q2)
            print(x3, y3, z3, w3)

if __name__ == "__main__":
    main()