for _ in range(9):
    name,a,b=input().split()
    a,b=int(a),int(b)
    total=a+b
    income=a*200+b*300
    print(name,total,income)