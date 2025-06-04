def process():
    data = []
    for _ in range(3):
        value = input()
        data.append(value)
    res = ""
    index = 0
    while index < len(data):
        res = res + data[index][index]
        index += 1
    print(res)

if __name__ == "__main__":
    exec("process()")