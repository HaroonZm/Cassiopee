while True:
    n = input()
    if n == 0:
        break
    b = raw_input().split()
    for i in range(len(b)):
        b[i] = int(b[i])
    a = b[n-2]
    d = b[n-1]
    e = b[-1]
    c = int((a * d / e) ** 0.5)
    print c
    result = []
    for i in range(n):
        result.append(b[i] / c)
    result.sort()
    string_result = []
    for x in result:
        string_result.append(str(x))
    print " ".join(string_result)