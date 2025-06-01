while True:
    try:
        line1 = input()
        numbers = line1.split()
        num = int(numbers[0])
        size = int(numbers[1])
        
        line2 = input()
        arr_str = line2.split()
        arr = []
        for s in arr_str:
            arr.append(int(s))
        
        arr.sort()
        arr.reverse()
        
        i = size - 1
        while i < num:
            arr[i] = 0
            i += size
        
        total = 0
        for value in arr:
            total += value
        
        print(total)
    except:
        break