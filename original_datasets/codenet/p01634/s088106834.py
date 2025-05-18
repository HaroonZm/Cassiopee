p=raw_input()
print "INVALID" if len(p)<6 or p.islower() or p.isupper() or p.isalpha() or p.isdigit() else "VALID"