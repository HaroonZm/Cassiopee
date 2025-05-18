import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break;
    students = []
    for i in range(n):
        students.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
    s_list=[[min(row)==s for s in row] for row in students]
    t_list=[[max(col)==s for s in col] for col in zip(*students)]
    ret = [0]
    for i,data in enumerate(zip(s_list, zip(*t_list))):
        for j,d in enumerate(zip(*data)):
            if all(d):
                ret.append(students[i][j])
    print(max(ret))