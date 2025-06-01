def check_list(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def dfs(a, b, c, index):
    if len(b) + len(c) == 10:
        if check_list(b) and check_list(c):
            return True
        else:
            return False

    b_copy = b[:]
    c_copy = c[:]
    b_copy.append(a[index])
    c_copy.append(a[index])

    if dfs(a, b_copy, c, index + 1):
        return True
    if dfs(a, b, c_copy, index + 1):
        return True

    return False

def main():
    n = int(input())
    for _ in range(n):
        data = input().split()
        numbers = []
        for num in data:
            numbers.append(int(num))
        result = dfs(numbers, [], [], 0)
        if result:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()