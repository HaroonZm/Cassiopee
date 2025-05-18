#import sys
#input = sys.stdin.readline
def main():
    a, b = map( int, input().split())
    if max((b-1+a-2)//(a-1), (b+a-1)//a) < (a+b)/a:
        print(max((b-1+a-2)//(a-1), (b+a-1)//a)*a)
    else:
        print(-1)
if __name__ == '__main__':
    main()