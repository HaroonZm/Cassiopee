notes = dict(C=0,C_=1, D=2, D_=3, E=4, F=5, F_=6, G=7, G_=8, A=9, A_=10, B=11)
notes["C#"]=notes.pop("C_")
notes["D#"]=notes.pop("D_")
notes["F#"]=notes.pop("F_")
notes["G#"]=notes.pop("G_")
notes["A#"]=notes.pop("A_")

def get_int(): return int(input())
ask = get_int()

for __ in range(ask):
    n2,m2=[int(k) for k in input().split()]
    tmp = [-100]
    for e in input().split():
        tmp.append(notes[e])
    source=[notes[s] for s in input().split()][::-1]

    def check(st):
        while st:
            if type(st)==tuple: 
                st = [st]
            idx1, idx2 = st.pop()
            if idx2 == m2:
                if idx1==0:
                    return True
                continue
            if not (1<=idx1<=n2): continue
            check_note = tmp[idx1]
            v = source[idx2]
            calc = (v-check_note) % 12
            if calc==1: st.append((idx1-2,idx2+1))
            if calc==0: st.append((idx1-1,idx2+1))
            if calc==11: st.append((idx1+1,idx2+1))
        return False

    st = [(n2,0),(n2-1,0)]
    ans = None
    import functools
    def tryit(): return check(st)
    if functools.reduce(lambda a,b: a or b, [tryit()]):
        print("Yes")
    else:
        print("No")