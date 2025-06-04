import sys

def solve(f):
    # Lire les deux premiers entiers
    temp = f.read_int_list()
    n = temp[0]
    s = temp[1]
    # Lire les n lignes suivantes dans x
    x = []
    for i in range(n):
        x.append(f.read_int_list())

    ans = 0
    side = 0
    l = 0
    r = n - 1

    while True:
        if x[l][0] > s:
            return ans + x[r][0] - s
        elif x[r][0] < s:
            return ans + s - x[l][0]
        else:
            if x[l][1] >= x[r][1]:
                x[l][1] += x[r][1]
                if side != 1:
                    ans += x[r][0] - x[l][0]
                side = 1
                r -= 1
            else:
                x[r][1] += x[l][1]
                if side != -1:
                    ans += x[r][0] - x[l][0]
                side = -1
                l += 1

class Reader:
    def __init__(self, filename=None):
        if filename:
            self.file = open(filename, 'r')
        else:
            self.file = None
        self.case = 1

    def __readline(self):
        if self.file:
            return self.file.readline().strip()
        else:
            return input()

    def next_case(self):
        if self.file:
            self.file.readline()
            self.case += 1

    def read_int(self):
        return int(self.__readline())

    def read_float(self):
        return float(self.__readline())

    def read_str(self):
        return self.__readline()

    def read_int_list(self):
        return list(map(int, self.__readline().split()))

    def read_float_list(self):
        return list(map(float, self.__readline().split()))

    def read_str_list(self):
        return self.__readline().split()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = None
    f = Reader(filename)
    if f.file:
        while True:
            print("Case #%d" % f.case)
            print(solve(f))
            try:
                f.next_case()
            except Exception:
                break
    else:
        print(solve(f))