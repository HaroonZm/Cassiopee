def main():
    while True:
        n = int(input())
        if n == 0:
            break
        groups = {}
        for _ in range(n):
            line = input()
            gname, members_str = line.split(":")
            members_str = members_str[:-1]  # remove trailing '.'
            members = members_str.split(",")
            groups[gname] = members
        visited = set()
        def get_members(group):
            res = set()
            for m in groups[group]:
                if m in groups:
                    res |= get_members(m)
                else:
                    res.add(m)
            return res
        print(len(get_members(list(groups.keys())[0])))
if __name__=="__main__":
    main()