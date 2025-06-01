ans = 1;

def one_count(data, i, count):
    global ans
    
    count+=1
    
    if data[i+1] == 1:
        one_count(data, i+1, count)
    elif ans <= count:
        ans = count+1
    
N = int(input())
data = list(map(int, input().split()))
data.append(0)

for i in range(N):
    count = 0;
    if data[i] == 1:
        one_count(data, i, count)

print(ans)