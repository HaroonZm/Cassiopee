n = int(input())
for i in range(n):
    s = input()
    m = len(s)

    ans = set()
    for j in range(1, m):
        head = s[0:j]
        tail = s[j:m]

        ans.add(head + tail)
        ans.add(tail + head)

        head = head[::-1]
        ans.add(head + tail)
        ans.add(tail + head)

        tail = tail[::-1]
        ans.add(head + tail)
        ans.add(tail + head)

        head = head[::-1]
        ans.add(head + tail)
        ans.add(tail + head)

    print(len(ans))