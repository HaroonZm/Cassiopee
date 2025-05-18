def get_input():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break

N = list(get_input())
for l in range(0,len(N),2):
    a = [int(i) for i in N[l].split()]
    b = [int(i) for i in N[l+1].split()]

    hit = 0
    blow = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == j:
                    hit = hit+1
                else:
                    blow = blow+1
    print(hit,blow)