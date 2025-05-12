#演習2-18

def solve(N,P,Q,menu):
    all_happy = [P*(Q-i) - menu[i] for i in range(N)] 
    all_happy = sorted(all_happy, reverse = True) 
    happy = [sum(menu)] 
    for i in range(N):
        happy.append(happy[-1] + P*i*2 + all_happy[i])
    return(max(happy))

while True:
    try:
        
        N,P,Q = map(int,input().split())
        menu = []
        for i in range(N):
            menu.append(int(input()))
        print(solve(N,P,Q,menu))
    except:
        break