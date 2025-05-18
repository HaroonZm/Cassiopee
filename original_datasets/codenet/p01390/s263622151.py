print("?za")
use=["za"]
can=[chr(i) for i in range(98, 98+24)]
can.extend(["a"+chr(i) for i in range(97, 97+26)])
while 1:
    s=input()
    if s[0]!="a" or s in use:
        print("!OUT")
        break
    use.append(s)
    if s=="a":
        p="aa"
    elif s=="aa":
        p="a"
    else:
        p=s[-1]+can.pop(0)+"a"
    print("?"+p)
    use.append(p)