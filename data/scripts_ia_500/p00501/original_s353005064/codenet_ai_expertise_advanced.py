N = int(input())
name = input()
nlen = len(name)
S = [input() for _ in range(N)]

ans = sum(
    any(
        any(
            all((k + l * wide) < len(s) and s[k + l * wide] == name[l] for l in range(nlen))
            for k in range(len(s))
        )
        for wide in range(1, 101)
    )
    for s in S
)

print(ans)