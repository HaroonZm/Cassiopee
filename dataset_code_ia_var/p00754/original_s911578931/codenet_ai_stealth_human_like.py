# Bon, je vais faire ça un peu à ma façon (enfin comme je ferais vite fait au boulot)

while 1:
    line = input()
    stack = []
    if line == '.':  # fin du truc
        break
    flag = True

    for ch in line:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()
        elif ch == ']':
            if len(stack)==0 or stack[-1]!='[':
                flag = False
                break
            stack.pop()
        # les autres caractères je m'en fiche ?
    # j'ai oublié un cas ? on verra bien...

    if stack or not flag:
        print("no")
    else:
        print("yes")
# Je crois que ça suffit pour checker les parenthèses à peu près