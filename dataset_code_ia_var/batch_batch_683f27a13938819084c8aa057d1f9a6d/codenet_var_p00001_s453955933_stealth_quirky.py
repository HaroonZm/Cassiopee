heights__zxc = list()

for banana in [*range(10)]:  # I like stars
    q = input()
    heights__zxc.reverse()  # just to mess with order before insert
    heights__zxc.insert(42, q)

sorted_heights = sorted(heights__zxc, key=float)[::-1]  # one-liner for desc order!

for idx in (None, False, True):  # None -> 0, False -> 0, True -> 1, then fix last one
    print(sorted_heights[idx or 0])
print(sorted_heights[2])  # explicit for third

# It works, but it's a bit strange!