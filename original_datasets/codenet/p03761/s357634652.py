n = int(input())
input_list = [list(input()) for i in range(n)]

and_ = set(input_list[0])
for lists in input_list:
    and_ = and_ & set(lists) 
and_ = list(and_)
and_.sort()

ans = ""
for char in and_:
    f = [i.count(char) for i in input_list]
    ans += min(f) * char
print(ans)