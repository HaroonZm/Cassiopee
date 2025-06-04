while True:
    try:
        inputs = input().split(" ")
        a = int(inputs[0])
        b = int(inputs[1])
        result = a + b
        output = len(str(result))
        print(output)
    except:
        break