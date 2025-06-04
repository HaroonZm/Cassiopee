A, B, C = (lambda x: (int(x[0]), int(x[1]), int(x[2])))(input().split())
x=[A+B,B+C,C+A];print(sorted(x)[0])