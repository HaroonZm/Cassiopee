from sys import stdin

def check(*args):
    if args[4] <= args[2] <= args[0]-args[4] and args[4] <= args[3] <= args[1]-args[4]:
        return True
    return False

params = list(map(int, stdin.readline().split()))
result = ""
while True:
    match check(*params):
        case True:
            result = "Yes"
            break
        case _:
            result = "No"
            break

for c in result:
    print(c, end="")
print()