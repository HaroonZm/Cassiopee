i = 0
try:
    n = int(input())
except:
    n = 0
while i < n:
    step = raw_input()
    flag = 0
    j = 0
    done = False
    while j < len(step) - 1:
        if step[j] == step[j+1]:
            print "No"
            done = True
            break
        j += 1
    if not done:
        print "Yes"
    i += 1