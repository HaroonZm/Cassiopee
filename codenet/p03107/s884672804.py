S=[int(x) for x in input()]
o = sum(S)
z = abs(len(S)-o)
print(min(o,z)*2)