def solve(n, l, r, A):
    result = 0
    for x in range(l, r + 1):
        found = False
        for i in range(n):
            if x % A[i] == 0:
                if i % 2 == 0:
                    result += 1
                found = True
                break
        if not found:
            if n % 2 == 0:
                result += 1
    return result

def main():
    answers = []
    while True:
        inputs = input().split()
        n = int(inputs[0])
        l = int(inputs[1])
        r = int(inputs[2])
        if n == 0 and l == 0 and r == 0:
            break
        A = []
        for i in range(n):
            num = int(input())
            A.append(num)
        res = solve(n, l, r, A)
        answers.append(res)
    for ans in answers:
        print(ans)

main()