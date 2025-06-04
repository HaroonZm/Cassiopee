d=int(input())
for case_i in range(1,d+1):
    s=int(input())
    print(f"Case {case_i}:")
    for _ in range(10):
        sq=str(s*s).zfill(8)
        s=int(sq[2:6])
        print(s)