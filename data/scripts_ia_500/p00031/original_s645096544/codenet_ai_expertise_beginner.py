while True:
    try:
        n = int(input())
        ans = []
        for i in range(10):
            power = 2 ** (9 - i)
            if n >= power:
                ans.append(power)
                n = n - power
        ans.reverse()
        result = ""
        for num in ans:
            result = result + str(num) + " "
        print(result.strip())
    except:
        break