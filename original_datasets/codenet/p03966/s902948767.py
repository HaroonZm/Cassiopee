def main():
    n = int(input())
    x,y = 1,1
    for _ in range(n):
        t,a = map(int,input().split())
        z = -1*min(-x//t,-y//a)
        x = z*t
        y = z*a
        # print(x,y)
    print(x+y)

main()