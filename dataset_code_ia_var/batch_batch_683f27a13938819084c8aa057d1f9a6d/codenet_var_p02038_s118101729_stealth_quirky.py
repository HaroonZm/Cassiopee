n = int(input())
s = input().split()
tf_stack = list(reversed(s))
while len(tf_stack) > 1:
    pick = tf_stack.pop()
    peek = tf_stack.pop()
    if pick == "T" and peek == "F":
        tf_stack.append("F")
    else:
        tf_stack.append("T")
print(tf_stack[-1])