def inpL(): res = input().split(); return list(map(int, res))

def main():
    x, y = inpL()
    if abs(x-y) > 1:
        result = "Alice"
    else:
        result = "Brown"
    print(result)

main()