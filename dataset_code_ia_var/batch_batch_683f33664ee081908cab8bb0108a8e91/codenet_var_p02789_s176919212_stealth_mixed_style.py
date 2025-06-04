def f():
    a, b = (int(x) for x in input().split())
    if a == b:
        print("Yes")
    else:
        from sys import stdout
        stdout.write("No\n")
f()