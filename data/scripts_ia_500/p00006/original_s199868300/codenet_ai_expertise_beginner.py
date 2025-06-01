instr = input()
reversed_instr = ""
for i in range(len(instr)-1, -1, -1):
    reversed_instr += instr[i]
print(reversed_instr)