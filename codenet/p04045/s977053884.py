n, k = map(int, input().split())                            
array = list(map(int, input().split()))
 
def jadgesuruo():
    for i in range(k):
        if str(n).find(str(array[i])) >= 0:
            return False
            break
    return True
 
for i in range(10**5):
    if jadgesuruo():
        print(n)
        break
    else:
        n = n + 1