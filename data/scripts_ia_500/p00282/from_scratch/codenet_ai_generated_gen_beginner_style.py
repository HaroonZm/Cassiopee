units = ["", "Man", "Oku", "Cho", "kei", "Gai", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo", "Jo"]

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    num = pow(m, n)
    num_str = str(num)[::-1]
    result = []
    length = len(num_str)

    for i in range(0, length, 4):
        part = num_str[i:i+4][::-1]
        if int(part) != 0:
            result.append(part + units[i//4])

    result = result[::-1]
    print("".join(result))