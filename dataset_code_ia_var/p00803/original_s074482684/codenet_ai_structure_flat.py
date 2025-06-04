if __name__ == '__main__':
    while True:
        num = int(input())
        if num == 0:
            break
        ans = 999999999
        c = 0
        while c < 54:
            cubic = c * c * c
            if cubic > num:
                break
            t = 0
            while t < 96:
                tetra = (t * (t + 1) * (t + 2)) // 6
                if cubic + tetra > num:
                    break
                if abs(cubic + tetra - num) < abs(num - ans):
                    ans = cubic + tetra
                t += 1
            c += 1
        print(ans)