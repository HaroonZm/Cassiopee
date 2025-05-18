while True:
    n = int(input())

    if n == 0:
        break
    
    on_mark = 0

    for i in range(int(n/4)):
        on_mark += int(input())
    
    print(on_mark)