List = [0] * 101
while True :
    p, s = map(int, input().split(","))
    if p == 0 and s == 0 :
        break
    
    List[p] = s

Sorted_List = sorted(list(set(List)), reverse = True)

while True :
    try :
        q = int(input())
    except EOFError :
        break
    
    print(Sorted_List.index(List[q])+1)