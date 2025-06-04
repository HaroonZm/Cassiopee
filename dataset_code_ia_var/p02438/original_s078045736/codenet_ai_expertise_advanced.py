from collections import deque
from functools import partial

class Splice:
    __slots__ = ("lists",)

    def __init__(self, num_lists: int):
        self.lists = [deque() for _ in range(num_lists)]

    def insert(self, t: int, x):
        self.lists[t].append(x)
        return self

    def dump(self, t: int):
        print(*self.lists[t])

    def splice(self, s: int, t: int):
        ls, lt = self.lists[s], self.lists[t]
        if lt:
            if len(ls) == 1:
                lt.append(ls[0])
            elif len(lt) == 1:
                ls.appendleft(lt[0])
                self.lists[t] = ls
            else:
                lt.extend(ls)
        else:
            self.lists[t] = ls
        self.lists[s] = deque()
        return self

def main():
    num_lists, num_op = map(int, input().split())
    lists = Splice(num_lists)
    ops = {
        0: lists.insert,
        1: lists.dump,
        2: lists.splice
    }
    for _ in range(num_op):
        op, *args = map(int, input().split())
        ops[op](*args)

if __name__ == "__main__":
    main()