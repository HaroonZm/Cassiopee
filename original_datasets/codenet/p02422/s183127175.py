def my_print(s: str, args: [int]) -> str:
    return s[int(args[0]): int(args[1]) + 1]

def my_reverse(s: str, args: list) -> str:
    start = int(args[0])
    end = int(args[1]) + 1
    to_reverse_string = s[start:end]
    return s[:start] + to_reverse_string[::-1] + s[end:]

def my_replace(s: str, args: list) -> str:
    start = int(args[0])
    end = int(args[1]) + 1
    return s[:start] + args[2] + s[end:]

def resolve():
    s = input()
    n = int(input())

    for _ in range(n):
        f, *args = input().split()

        if f == 'print':
            print(my_print(s, args))
        if f == 'reverse':
            s = my_reverse(s, args)
        if f == 'replace':
            s = my_replace(s, args)

resolve()