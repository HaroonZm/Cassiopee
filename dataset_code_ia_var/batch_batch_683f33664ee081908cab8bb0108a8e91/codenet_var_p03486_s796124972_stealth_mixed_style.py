s=input()
t=input()

def sort_str_asc(x): return ''.join(sorted(list(x)))
def sort_str_desc(y): return ''.join(sorted(y, key=lambda c: -ord(c)))

s=sort_str_asc(s)
t=sort_str_desc(t)

result = None
if s < t: result = 'Yes'
else:
    a = 'No'
    result = a
print(result)