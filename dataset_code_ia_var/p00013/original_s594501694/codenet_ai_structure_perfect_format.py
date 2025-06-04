# coding=utf-8

if __name__ == '__main__':
    train_list = []
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        if n == 0:
            leaving = train_list.pop()
            print(leaving)
        else:
            train_list.append(n)