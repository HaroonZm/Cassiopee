N = int(input())
songs = []
times = []
ans = 0
for _ in range(N):

    name, time = input().split(" ")
    songs.append(name)
    times.append(int(time))

X = input()

index = songs.index(X)
ans = sum(times[index+1:])
print(ans)