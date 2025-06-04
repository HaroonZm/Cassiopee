while True:
    n = int(input())
    if n == 0:
        break
    b = input().split()
    for j in range(len(b)):
        b[j] = int(b[j])
    last1 = b[n-2]
    last2 = b[n-1]
    last = b[-1]
    c = int((last1 * last2 / last) ** 0.5)
    print(c)
    a_list = []
    for i in range(n):
        a_list.append(b[i] // c)
    a_list.sort()
    result = ""
    for x in a_list:
        result += str(x) + " "
    print(result.strip())