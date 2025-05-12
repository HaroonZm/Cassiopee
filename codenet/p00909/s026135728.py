def solve():
    def measurement(a, b, w):
        a_root = root[a]
        b_root = root[b]
        if a_root != b_root:
            a_member = member[a_root]
            b_member = member[b_root]
            offset = w - (weight[b] - weight[a])
            if len(a_member) > len(b_member):
                a_member.extend(b_member)
                for n in b_member:
                    root[n] = a_root
                    weight[n] += offset
            else:
                b_member.extend(a_member)
                for n in a_member:
                    root[n] = b_root
                    weight[n] -= offset
    
    def inquiry(a, b):
        if root[a] == root[b]:
            return weight[b] - weight[a]
        else:
            return 'UNKNOWN'
    
    def operation(line):
        if line[0] == '!':
            a, b, w = map(int, line[2:].split())
            measurement(a, b, w)
        else:
            a, b = map(int, line[2:].split())
            return inquiry(a, b)
    
    import sys
    file_input = sys.stdin.readlines()
    
    while True:
        N, M = map(int, file_input[0].split())
        if N == 0:
            break
        
        root = [i for i in range(N + 1)]
        member = [[i] for i in range(N + 1)]
        weight = [0] * (N + 1)
        
        ans = (operation(line) for line in file_input[1:M+1])
        ans = filter(lambda x: x != None, ans)
        print(*ans, sep='\n')
        
        del file_input[:M+1]

solve()