from sys import exit as ex
def odd_case(n):
    i = 0
    while i < n:
        line = []
        for j in range(n-1):
            line.append(str(((j + i + 1) % n) + 1))
        print(" ".join(line))
        i += 1
def even_case(n):
    for i in range(n):
        temp = list()
        for j in range(n-1):
            if not j == n//2-1:
                temp += [(j+i+1)%n+1]
        temp[:0] = [ (n//2+i) % n + 1 ]
        if(i<n//2):
            t = temp[0]; temp[0]=temp[1]; temp[1]=t
        print(' '.join(map(str,temp)))
def main():
    n = int(input())
    if n==2:
        print(-1)
        ex()
    if n & 1:
        odd_case(n)
    else:
        even_case(n)
main()