H,W= map(int,input().split())
region = [input() for _ in range(H)]
R,C= map(int,input().split())
pattern = [input() for _ in range(R)]

base = 257
mod = 10**9+7

def compute_hash(s):
    h = 0
    for ch in s:
        h = (h*base + ord(ch)) % mod
    return h

pow_base = [1]*(max(W,C)+1)
for i in range(1,len(pow_base)):
    pow_base[i] = (pow_base[i-1]*base)%mod

pattern_row_hash = [compute_hash(row) for row in pattern]

region_row_hash = []
for row in region:
    h = 0
    rolling = []
    for i in range(C):
        h = (h*base + ord(row[i]))%mod
    rolling.append(h)
    for i in range(C,W):
        h = (h - ord(row[i-C])*pow_base[C-1])%mod
        h = (h*base + ord(row[i]))%mod
        rolling.append(h)
    region_row_hash.append(rolling)

res = []
base_r = pow_base
for col in range(W-C+1):
    h = 0
    col_hashes = []
    for i in range(R):
        h = (h*base + region_row_hash[i][col])%mod
    col_hashes.append(h)
    for i in range(R, H):
        h = (h - region_row_hash[i-R][col]*pow_base[R-1])%mod
        h = (h*base + region_row_hash[i][col])%mod
        col_hashes.append(h)
    for i,rhash in enumerate(col_hashes):
        if rhash == 0:
            continue
        # Check actual pattern to avoid collisions
        match = True
        for k in range(R):
            if region[i+k][col:col+C] != pattern[k]:
                match = False
                break
        if match:
            res.append((i,col))

pattern_hash = 0
for hrow in pattern_row_hash:
    pattern_hash = (pattern_hash*base + hrow)%mod

# re-check hash equality and output
final_res = []
for i,j in res:
    # Double check hash to be sure
    hcheck = 0
    for k in range(R):
        hcheck = (hcheck*base + region_row_hash[i+k][j])%mod
    if hcheck == pattern_hash:
        final_res.append((i,j))

final_res.sort()
for i,j in final_res:
    print(i,j)