A,B,K = [int(x) for x in input().split()]
def do_step(cnt, val1, val2):
    if cnt%2==0:
        val1 = val1//2
        val2 += val1
    else:
        val2 = val2//2
        val1 += val2
    return val1,val2
step = 0
while step<K:
    if step%2==0:
        x1,x2 = do_step(step,A,B)
        A,B = x1,x2
    else:
        A,B = do_step(step,B,A)[1],do_step(step,B,A)[0]
    step+=1
print("{} {}".format(A,B))