def main():
    s = ""
    while True:
        s = input()
        if s == "0": 
            break
        n = int(s)
        i = 0
        while i < 9:
            n -= int(input())
            i += 1
        print(n)

main()