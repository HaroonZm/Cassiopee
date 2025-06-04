def process(N, arr):
    buf = [None]*(N+1)
    buf[0]=1
    # étape impérative
    for j in range(1,N+1):
        buf[j]=((buf[j-1]-arr[j-1])<<1)
        if buf[j]<=0:
            return -1
    # vérif impure
    if buf[-1]<arr[-1]: return -1
    buf[-1]=arr[-1]
    total=arr[-1]
    idx=N-1
    # boucle old school
    while idx>=0:
        buf[idx]=min(buf[idx],buf[idx+1]+arr[idx])
        if not buf[idx]:
            return -1
        total+=buf[idx]
        idx-=1
    return total

def read_and_run():
    N=int(input())+1
    def parse(): return list(map(int,input().split()))
    r=process(N,parse())
    print(r)
read_and_run()