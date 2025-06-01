N = int(input())
A_data = list(map(int, input().split()))
X, A_members = A_data[0], set(A_data[1:])
B_data = list(map(int, input().split()))
Y, B_members = B_data[0], set(B_data[1:])
C_data = list(map(int, input().split()))
Z, C_members = C_data[0], set(C_data[1:])

all_members = set(range(1, N+1))
not_A = all_members - A_members

result = (not_A & C_members) | (B_members & C_members)
print(len(result))