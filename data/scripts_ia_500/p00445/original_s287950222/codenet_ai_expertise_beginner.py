import sys

for line in sys.stdin:
    s_real = 0
    s_imag = 0
    length = len(line)
    for i in range(length - 2):
        substring = line[i:i+3]
        if substring == "JOI":
            s_real += 1
        if substring == "IOI":
            s_imag += 1
    print(s_real)
    print(s_imag)