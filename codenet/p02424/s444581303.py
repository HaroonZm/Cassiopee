#前問題の解答参照
a,b = map(int, input().split( ))
##<<左桁ずらし

print("{:032b}".format(a&b))
print("{:032b}".format(a|b))
print("{:032b}".format(a^b))