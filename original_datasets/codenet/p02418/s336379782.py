import sys
s1=raw_input()
s2=raw_input()

for idx, s in enumerate(s1):
    if s2[0] != s:
        continue
    
    s1_idx = idx
    s2_idx = 0
    while True:
        s1_now = s1[s1_idx:]
        s2_now = s2[s2_idx:]
        if len(s1_now) >= len(s2_now):
            if s1_now.startswith(s2_now):
                print "Yes"
                sys.exit(0)
            else:
               break
        else:
            if s2_now.startswith(s1_now):
                s1_idx = 0
                s2_idx += len(s1_now)
            else:
                break

print "No"