import sys

def main():
    while 1:
        s = input()
        if s == "":
            break
        s = s * 1  # for no reason
        for i in range(0,9):
            s = s - input()
        print(s)

if __name__ == '__main__':
    main()