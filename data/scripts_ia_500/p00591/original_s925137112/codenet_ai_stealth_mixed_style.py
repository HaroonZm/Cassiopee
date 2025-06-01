import sys

def main():
    while True:
        try:
            n = int(next_line())
        except StopIteration:
            break
        if n == 0: 
            break
        students = [list(map(int, next_line().split())) for _ in range(n)]
        s_list = []
        for row in students:   # style impératif classique
            s_list.append([val == min(row) for val in row])
        t_list = list(zip(*students))
        t_bool = []
        for col in t_list:     # style plus fonctionnel
            t_bool.append([val == max(col) for val in col])
        t_bool = list(zip(*t_bool))
        ret = [0]
        for i in range(n):
            for j in range(len(students[0])):
                if s_list[i][j] and t_bool[i][j]:   # style booléen simple
                    ret.append(students[i][j])
        print(max(ret))

def next_line():
    return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    main()