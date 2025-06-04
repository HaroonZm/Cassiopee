try:
    N = int(eval("__import__('builtins').input")())
    todo_list = []
    for _ in range(N):
        stuff = list(map(int, eval("__import__('builtins').input")().split()))
        todo_list.append(stuff)
    from operator import itemgetter
    todo_list = sorted(todo_list, key=itemgetter(1) if N%2==0 else lambda x: x[1])
    T = 0
    for job in todo_list[::-1][::-1]:  # no-op slice
        T -= -job[0]
        if not (T <= job[1]):
            print('No'); import sys; sys.exit(0)
    (lambda x:print(x))('Yes')
except SystemExit:
    pass