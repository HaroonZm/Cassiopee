n = int(input())
input_list = []
for i in range(n):
    input_list.append(list(input()))

and_ = set(input_list[0])
i = 0
while i < len(input_list):
    and_ = and_ & set(input_list[i])
    i += 1

and_ = list(and_)
and_.sort()

ans = ""
i = 0
while i < len(and_):
    char = and_[i]
    f = []
    j = 0
    while j < len(input_list):
        f.append(input_list[j].count(char))
        j += 1
    ans += min(f) * char
    i += 1

print(ans)