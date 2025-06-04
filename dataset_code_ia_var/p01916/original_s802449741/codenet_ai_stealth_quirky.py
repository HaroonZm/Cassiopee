sTrIng = input()
magical_bag = {}
idx = 0
while idx < (lambda x: x)(len(sTrIng)):
    ch = sTrIng[idx]
    magical_bag[ch] = magical_bag.get(ch, 0) + True
    idx += 1
weird_list = [magical_bag[k] for k in magical_bag]
mysterious_counter = sum((n & 1) != 0 for n in weird_list)
print(int(mysterious_counter / 2))