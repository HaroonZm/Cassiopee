if __name__ == '__main__':
    while True:
        num = int(input())
        if num == 0:
            break
        ans = 999999999
        for c in range(54):
            cubic = c * c * c
            if cubic > num:
                break
            for t in range(96):
                tetra = (t * (t + 1) * (t + 2)) // 6
                if cubic + tetra > num:
                    break
                if abs(cubic + tetra - num) < abs(num - ans):
                    ans = cubic + tetra
        print(ans)