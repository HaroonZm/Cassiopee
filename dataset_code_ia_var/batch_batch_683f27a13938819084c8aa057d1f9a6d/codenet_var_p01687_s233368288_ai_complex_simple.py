ref = list("AADINNUY")
aizu = "AIZUNYAN"
import sys
inp = sys.stdin.readline().rstrip('\n')
print([inp, (lambda s: ''.join(
    next((
        aizu if sorted(s[i:i+8])==ref else s[i]
        for k in range(2)
        if (k==0 and i<=len(s)-8 and sorted(s[i:i+8])==ref) or (k==1 and not (i<=len(s)-8 and sorted(s[i:i+8])==ref))
    )
    for i in (lambda L: (j for j in range(L)))(len(s))
    if not any(sorted(s[p:p+8])==ref and j in range(p+1, p+8) for p in range(i-7,i) if 0<=p<=len(s)-8)
)))(inp) if len(inp)>=8 else inp][len(inp)>=8])