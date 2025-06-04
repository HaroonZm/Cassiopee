from sys import stdin
from array import array

def main():
    N = int(stdin.readline()) + 1
    C = array('i', [0]*360)

    for _ in range(1, N):
        m, d, l, s = map(int, stdin.readline().split())
        i_start = (m - 1) * 30 + d - 1
        i_end = i_start + l - 1

        seg_strength = int(s)
        for idx in range(i_start, i_end + 1):
            j = idx % 360
            if C[j] < seg_strength:
                C[j] = seg_strength

        for k in range(1, seg_strength + 1):
            left = (i_start - k) % 360
            right = (i_end + k) % 360
            strength = seg_strength - k

            if C[left] < strength:
                C[left] = strength
            if C[right] < strength:
                C[right] = strength

    print(min(C))

if __name__ == "__main__":
    main()