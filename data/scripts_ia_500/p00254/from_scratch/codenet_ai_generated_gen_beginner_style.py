while True:
    N = input()
    if N == "0000":
        break
    if N[0] == N[1] == N[2] == N[3]:
        print("NA")
        continue
    count = 0
    while N != "6174":
        digits = list(N)
        digits.sort()
        S = int("".join(digits))
        digits.sort(reverse=True)
        L = int("".join(digits))
        diff = L - S
        N = str(diff).zfill(4)
        count += 1
    print(count)