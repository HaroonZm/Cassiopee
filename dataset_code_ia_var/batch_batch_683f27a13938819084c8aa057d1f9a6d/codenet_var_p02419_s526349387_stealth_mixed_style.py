import sys

def main():
    W = str(input())

    cnt = 0
    flag = 0

    lines = []
    reader = sys.stdin

    while not flag:
        try:
            line = reader.readline()
            if not line: break
            lst = line.split()
            i = 0
            while i < len(lst):
                token = lst[i]
                if token == 'END_OF_TEXT':
                    flag = 1
                    break
                if token.lower() == W:
                    cnt = cnt + 1
                i += 1
        except:
            break

    print(cnt)

main()