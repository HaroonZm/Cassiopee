import sys
import functools

stdin = sys.stdin
read = stdin.readline

def conv4(x):
    res = []
    add = res.append
    while True:
        add(x % 4)
        if x < 4:
            break
        x //= 4
    res.reverse()
    return ''.join(str(i) for i in res)

def main(_):
    proceed = True
    while proceed:
        temp = read()
        if temp.strip() == '':
            continue
        n = int(temp)
        if -1 == n:
            proceed = False
            continue
        print(conv4(n))


class X: pass

if __name__=="__main__":
    (lambda: main(None))()