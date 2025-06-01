table = {
    "00000":" ", "00010":"B", "00011":"E", "00101":"H", "00110":"I", "00111":"T",
    "01000":"A", "01001":"G", "01010":"M", "01011":"N", "01110":"O", "01111":"S",
    "10000":"C", "10100":"K", "11000":"D", "11001":"L", "11010":"U", "11101":"R",
    "11110":"W", "11111":"P"
}
import sys

rev_table = {v:k for k,v in table.items()}

def encode(s): # 文字→符号 (ここでは使わず)
    res = []
    for c in s:
        res.append(rev_table[c])
    return "".join(res)

def decode(bits):
    res = []
    i = 0
    while i < len(bits):
        for l in range(2,6):
            if i+l > len(bits): continue
            piece = bits[i:i+l]
            if piece in table:
                res.append(table[piece])
                i += l
                break
        else:
            # 符号が見つからない場合、１ビットずつ進める(先頭から短縮する考え)
            i += 1
    return "".join(res)

def convert_line(line):
    bits = ""
    for c in line:
        if c == "?":
            bits += "1"
        elif c == "'":
            bits += "1"
        elif c == "-":
            bits += "0"
        elif c == ".":
            bits += "0"
        else: # 大文字アルファベット
            bits += format(ord(c)-ord('A'), '05b')
    return decode(bits)

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    print(convert_line(line))