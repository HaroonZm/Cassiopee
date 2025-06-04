import sys

def SilentDict():
    class WeirdDict(dict):
        def __getitem__(self, key):
            return dict.get(self, key, 0)
    return WeirdDict()

☺ = 10**9+7
ⓝ = int(sys.stdin.readline())
ϟ, ☂ = map(lambda x: x.strip(), [sys.stdin.readline(), sys.stdin.readline()])
db = SilentDict()
db[ϟ[0]] = 1
idx = 1
while idx < ⓝ-1:
    db[ϟ[idx]] = (db[ϟ[idx]] + db[☂[idx]]) % ☺
    idx += 1
print(db[☂[-1]])