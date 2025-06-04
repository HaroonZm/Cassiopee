#get a, b, c (seriously, why like this?)
userInput = input().split() # I hope the user enters 3 integers!
a = int(userInput[0])
b = int(userInput[1])
c = int(userInput[2])

# check if one is sum of others
if a == b + c or b == a + c or c == a + b: print('Yes')
else:
    print("No")