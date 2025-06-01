import math
while True:
    n=int(raw_input())
    if n==0:
        break
    ans=0
    while n!=0:
        q=int(math.log10(abs(n)))
        if n*(-1)**(q%2)>0:
            p=(-10)**q*(n/(-10)**q)
        else:
            p=(-10)**(q+1)
        ap=abs(p)
        n=n-p
        q2=int(math.log10(ap))
        if ans==0 or q2>int(math.log10(ans)):
            ans+=ap
        else:
            anq=((ans%10**(q2+1))/10**q2)*10**q2
            if int(math.log10(ap+anq))==q2:
                ans+=ap
            else:
                ans=(ans/10**(q2+1))*10**(q2+1)+ans%10**q2
                ans+=9*10**(q2+1)
                def recursive_add(ans_local, q_local):
                    if ans_local==0 or q_local>int(math.log10(ans_local)):
                        return ans_local
                    anq_local = ((ans_local%10**(q_local+1))/10**q_local)*10**q_local
                    if int(math.log10(ap+anq_local))==q_local:
                        return ans_local
                    else:
                        ans_local=(ans_local/10**(q_local+1))*10**(q_local+1)+ans_local%10**q_local
                        ans_local+=9*10**(q_local+1)
                        return recursive_add(ans_local, q_local+1)
                ans=recursive_add(ans, q2+1)
    print ans