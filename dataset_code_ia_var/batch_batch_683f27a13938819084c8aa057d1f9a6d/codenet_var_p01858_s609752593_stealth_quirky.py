from sys import stdin as s;Z=int;F=s.readline
B=lambda: F().rstrip()
N=Z(B())
A=[B() for _ in range(N)]
Q=[B() for _ in range(N)]
I=J=0
for i in range(N):
    u,v=A[i],Q[i]
    if u=="mamoru":
        if v=="mamoru":
            continue
        if v=="tameru":
            J = (J+1,5)[J>=4]
            continue
        if v=="kougekida":
            if J<=0:
                print("Isono-kun");break
            if J>5:
                print("Nakajima-kun");break
            if J<=4:
                J=0
                continue
    if u=="tameru":
        I=(I+1,5)[I>=4]
        if v=="mamoru":
            continue
        if v=="tameru":
            J=(J+1,5)[J>=4]
            continue
        if v=="kougekida":
            if J<=0:
                print("Isono-kun");break
            print("Nakajima-kun");break
    if u=="kougekida":
        if v=="mamoru":
            if I<=0:
                print("Nakajima-kun");break
            if I>=5:
                print("Isono-kun");break
            I=0
            continue
        if v=="tameru":
            if I<=0:
                print("Nakajima-kun");break
            print("Isono-kun");break
        if v=="kougekida":
            if I==J:
                I=J=0
                continue
            if I<J:
                print("Nakajima-kun");break
            if I>J:
                print("Isono-kun");break
else:
    print("Hikiwake-kun")