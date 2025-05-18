import collections

class Splice():
    def __init__(self, num_lists):
        self.lists = [collections.deque() for i in range(0, num_lists, 1)]

    def insert(self, t, x):
        self.lists[t].append(x)
        return self

    def dump(self, t):
        print(' '.join(map(str, self.lists[t])))

    def splice(self, s, t):
        if self.lists[t]:
            if len(self.lists[s]) == 1:
                self.lists[t].append(self.lists[s][0])
            elif len(self.lists[t]) == 1:
                self.lists[s].appendleft(self.lists[t][0])
                self.lists[t] = self.lists[s]
            else:
                self.lists[t].extend(self.lists[s])
        else:
            self.lists[t] = self.lists[s]
        self.lists[s] = collections.deque()
        return self

num_lists, num_op = map(int, input().split(' '))
lists = Splice(num_lists)

for op in range(0, num_op):
    op = tuple(map(int, input().split(' ')))
    if op[0] == 0:
        lists.insert(op[1], op[2])
    elif op[0] == 1:
        lists.dump(op[1])
    elif op[0] == 2:
        lists.splice(op[1], op[2])