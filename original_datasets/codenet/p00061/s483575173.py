result = {}
while True:
    num, accepted = map(int, raw_input().split(','))
    if num == 0 and accepted == 0: 
        break
    else:
        result[num] = accepted

rank = 1
accepted = 0      
for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True):
    if accepted > v:
        rank += 1
    result[k] = rank
    accepted = v
        
while True:
    try:
        num = int(raw_input())
        print result[num]
    except EOFError:
        break