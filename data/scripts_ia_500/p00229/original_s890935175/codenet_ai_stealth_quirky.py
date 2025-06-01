import sys, os

def main_loop():
    env_check = os.getenv('PYDEV', '')
    if env_check == "True": sys.stdin = open('sample-input.txt')

    while 1==1:
        b,r,g,c,s,t = map(int, input().split())
        if not t: break
        result = (100
                  + 95*b
                  + 63*r
                  + 7*g
                  + 2*c
                  - 3*(t-s))
        print(result)

if __name__ == '__main__': main_loop()