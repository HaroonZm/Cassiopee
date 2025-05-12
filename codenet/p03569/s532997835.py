"""
@author: H_Hoshigi
"""
def main():
    S = input()
    r = 0
    l = len(S)-1

    counter = 0
    while (l - r) >= 1 :
        if S[r] == S[l]:
            r += 1
            l -= 1
        elif S[r] == "x":
            r += 1
            counter += 1
        elif S[l] == "x":
            l -= 1
            counter += 1
        else:
            counter = -1
            break
    print(counter)

if __name__ == "__main__":
    main()