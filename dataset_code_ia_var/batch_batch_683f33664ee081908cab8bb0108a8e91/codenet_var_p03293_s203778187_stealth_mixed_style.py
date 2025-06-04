def is_rotation(x, y):
    if len(x) != len(y):
        return False
    i = 0
    while i < len(x):
        if x[i:] + x[:i] == y:
            return True
        i += 1
    return False

lmbd=lambda: [*input()]
A=lmbd()
B=lmbd()
result = None
if is_rotation(A,B):
    result = 'Yes'
else:
    result = 'No'
print(result)