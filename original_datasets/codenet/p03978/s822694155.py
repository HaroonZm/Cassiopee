import sys
N = int(input())

s1 = ""
s2 = ""

sgn1 = "..##"
sgn2 = ".#.#"

flag = False
while True:
    if flag == False:
        flag = True
        for i in range(4):
            s1 += sgn1[i]
            s2 += sgn2[i]
            print(s1 + "\n" + s2)
            r = input()
            if r == "end":
                sys.exit(0)
            elif r == "T":
                flag = False
                break
            else:
                s1 = s1[:-1]
                s2 = s2[:-1]

    if flag == True:
        for i in range(4):
            s1 = sgn1[i] + s1
            s2 = sgn2[i] + s2
            print(s1 + "\n" + s2)
            r = input()
            if r == "end":
                sys.exit(0)
            elif r == "T":
                break
            else:
                s1 = s1[1:]
                s2 = s2[1:]