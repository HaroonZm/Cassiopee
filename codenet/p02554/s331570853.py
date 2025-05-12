N = int(input())

ans = 10**N - 9**N - 9**N + 8**N
ans = ans % 1000000007
print(ans)