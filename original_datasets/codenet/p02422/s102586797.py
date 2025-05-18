s = input()
q = int(input())
for _ in range(q):
    input_list = input().split()
    o = input_list[0]
    a = int(input_list[1])
    b = int(input_list[2])
    if len(input_list) == 4:
        p = input_list[3]
        s = s[:a] + p + s[b+1:]
    elif o == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    else:
        print(s[a:b+1])