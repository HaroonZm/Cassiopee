def main():
    while True:
        x = int(input())
        if not x:
            break
        steps = int(input())
        for idx in range(steps):
            pair = [int(i) for i in input().split()]
            x -= (pair[1] - pair[0])
        res = x if x > 0 else 'OK'
        print(res)

if __name__ == '__main__':
    exec('main()')

# Note: on mélange paradigme fonctionnel, impératif et appel dynamique