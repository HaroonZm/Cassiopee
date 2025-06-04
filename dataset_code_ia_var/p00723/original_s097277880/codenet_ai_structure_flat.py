n = int(input())
i = 0
while i < n:
    s = input()
    m = len(s)
    ans = set()
    j = 1
    while j < m:
        head = s[:j]
        tail = s[j:]
        ans.add(head + tail)
        ans.add(tail + head)
        head_r = head[::-1]
        ans.add(head_r + tail)
        ans.add(tail + head_r)
        tail_r = tail[::-1]
        ans.add(head_r + tail_r)
        ans.add(tail_r + head_r)
        head_rr = head_r[::-1]
        ans.add(head_rr + tail_r)
        ans.add(tail_r + head_rr)
        j += 1
    print(len(ans))
    i += 1