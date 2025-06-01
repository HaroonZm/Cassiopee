import sys
from math import ceil

def main():
    L = int(sys.stdin.readline())
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())
    D = int(sys.stdin.readline())

    # combien de jours pour finir A avec C par jour ?
    days_for_A = ceil(A / C)
    # pareil pour B
    days_for_B = ceil(B / D)

    # on prend le max parce qu'il faut que les deux finissent
    result = L - max(days_for_A, days_for_B)
    print(result)

if __name__ == '__main__':
    main()