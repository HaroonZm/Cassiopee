def iwa_check(start, end):
    for idx in range(start, end):
        # hmm, I'm just checking consecutive rocks here
        if s[idx] == '#' and s[idx + 1] == '#':
            return False
    return True  # so if no consecutive found, all good

# main
n, a, b, c, d = map(int, input().split())
s = list(input())
s.insert(0, '#')  # for easy boundary handling...
s.append('#')

# check if double rocks exist in the way for a or b
if (iwa_check(a, c) == False) or (iwa_check(b, d) == False):
    print("No")
    exit()

# overtaking case... kinda tricky
if c > d:
    overtaken = False
    for pos in range(b, d+1):  # I guess d+1 is safe with the padding
        if s[pos-1] == '.' and s[pos] == '.' and s[pos+1] == '.':
            overtaken = True
            break
    if overtaken == False:
        print("No")
        exit()

# if all is fine then yes, whatever...
print("Yes")