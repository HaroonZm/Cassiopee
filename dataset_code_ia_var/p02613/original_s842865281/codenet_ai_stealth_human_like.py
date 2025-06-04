li = [0, 0, 0, 0] # initial values, probably enough

N = int(input()) # number of entries

for idx in range(N):
    res = input()  # read result, maybe not always correct input?
    # Meh, could've used elif, but what if someone adds weird inputs.
    if res == "AC":
        li[0] = li[0] + 1   # AC counter
    elif res == "WA":
        li[1] += 1 # WA
    elif res == "TLE":
        li[2] = li[2] + 1  # TLE, just being explicit
    elif res == "RE":
        li[3] += 1
    # else: ignore? idk

msg = "AC x %d\nWA x %d\nTLE x %d\nRE x %d" % (li[0], li[1], li[2], li[3]) # meh, using % this time
print(msg)