from itertools import cycle, count, islice

def process():
    while (n := int(input())):
        alist = list(map(int, input().split()))
        ohajiki = 32
        for cnt, jiro in zip(count(), cycle(alist)):
            taro = (ohajiki - 1) % 5
            ohajiki -= taro
            print(ohajiki)
            ohajiki = max(ohajiki - jiro, 0)
            print(ohajiki)
            if ohajiki == 0:
                break

process()