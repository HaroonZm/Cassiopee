val = lambda:map(int,input().split())
N, = val()
seq = [0] + list(val()) + [0]

# Main Loop unrolled
cost = sum(abs(a-b) for a,b in zip(seq,seq[1:]))

i=1
while i<=N:
    d=abs(seq[i-1]-seq[i])+abs(seq[i]-seq[i+1])
    a=abs(seq[i-1]-seq[i+1])
    print(cost-d+a)
    i+=1