def main():
    while 1:
        p_o = list(input())
        if p_o == ["0"]:
            break
        a, b = 0, 0
        [a:=a+1 if x=="A" else b:=b+1 for x in p_o[1:]]
        (a, b) = ((a+1, b) if a > b else (a, b+1))
        print(a, b)
main()