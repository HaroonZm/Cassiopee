from collections import deque
a = deque(list(input()))
b = deque(list(input()))
c = deque(list(input()))
dict_p = {"a":a, "b":b, "c": c}
next = "a"
while True:
    if len(dict_p[next]) == 0:
        print(next.upper())
        exit()
    next = dict_p[next].popleft()