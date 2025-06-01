now = 'A'
while True :
    try :
        a, b = input().split(',')
        if   now == a : now = b
        elif now == b : now = a
    except : break
print(now)