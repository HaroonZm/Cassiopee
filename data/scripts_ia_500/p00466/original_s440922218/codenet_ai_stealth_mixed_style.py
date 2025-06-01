def main():
    import sys
    s = None
    while True:
        try:
            s = input()
            if s == '0':
                break
            s = int(s)
            for i in range(9):
                s = s - int(input())
            print(s)
        except EOFError:
            break

main()