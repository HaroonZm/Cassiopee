import sys

def is_ok(food, limit):
    name, p, q, r = food
    cal = p * 4 + q * 9 + r * 4
    if p <= limit[0] and q <= limit[1] and r <= limit[2] and cal <= limit[3]:
        return True
    return False

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        foods = []
        for _ in range(n):
            foods.append(list(map(int, input().split())))
        limit = list(map(int, input().split()))
        answer = []
        for food in foods:
            if is_ok(food, limit):
                answer.append(food[0])
        if len(answer) == 0:
            print('NA')
        else:
            for name in answer:
                print(name)

if __name__ == "__main__":
    main(sys.argv[1:])