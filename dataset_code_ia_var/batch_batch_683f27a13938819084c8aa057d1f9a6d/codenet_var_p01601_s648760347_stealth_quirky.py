from sys import stdout

def pal(s):return s==s[::-1]

z=raw_input()
step=0
result=None
while True:
    for delta in [-1,1]:
        t=str(int(z)+step*delta)
        if pal(t):
            stdout.write(t+'\n')
            result=t
            break
    if result is not None: break
    step+=1