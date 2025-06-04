s = raw_input()
true_s = 'CODEFESTIVAL2016'
error_number = 0
for i in range(16):
    if s[i] != true_s[i]:
        error_number += 1
print error_number