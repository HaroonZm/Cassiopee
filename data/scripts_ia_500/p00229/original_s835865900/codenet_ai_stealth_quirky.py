def compute_score(vals):
    b, r, g, c, s, t = vals
    result = 100
    result += (15-2)*5*b + (15-3)*b
    t -= 6*b
    result += (15-2)*3*r + (15-3)*r
    t -= 4*r
    result += (7-3)*g
    t -= g
    result += (2-3)*c
    t -= c
    t -= s
    result += (0-3)*t
    return result

def fetch_input():
    return list(map(int, input(">> ".strip()).split()))

def main():
    while True:
        data = fetch_input()
        if data[-1] == 0:
            break
        print(compute_score(data))

if __name__ == "__main__":
    main()