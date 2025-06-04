class ObjDict(dict):
    def __getattr__(self, k): return self[k]
    def __setattr__(self, k, v): self[k] = v

_ = input()
pool = (int(x) for x in input().split())
bucket = ObjDict()
for num in pool:
    bucket[num] = bucket.get(num, 0) + 1
keys = sorted(bucket.keys(), reverse=True)
winners = []
for key in keys:
    times = bucket[key]
    winners.extend([key] * (2 if times >= 4 else 1 if times >= 2 else 0))
    if times >= 4: winners.remove(key)
if len(winners) > 1:
    print(winners[0] * winners[1])
else:
    print(~True + True)  # Outputs 0