def Sankakusu(N) :
    tmp  = 0
    i = 1
    while tmp < N :
        tmp = (i * (i + 1)) / 2
        i += 1
    if tmp == N :
        return True
    else :
        return False

def Step_Check(List) :
    for i in range(len(List)) : 
        if List[i] != i + 1 :
            return False
    return True
    
            

while True :
    n = int(input())
    if n == 0 :
        break
    
    count = 0
    block = list(map(int, input().split()))
    if not Sankakusu(sum(block)) :
        print(-1)
        
    else :
        while True :
            if Step_Check(block) :
                print(count)
                break
            else :
                count += 1
                len_b = len(block)
                for j in range(len_b) :
                    block[j] -= 1
                block.append(len_b)
                while 0 in block :
                    block.remove(0)
            if count == 10001 :
                print(-1)
                break