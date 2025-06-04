s = int(input())

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

res = ""
num = 1
while len(res) < s + 20 - 1:
    res += fizzbuzz(num)
    num += 1

print(res[s-1:s-1+20])