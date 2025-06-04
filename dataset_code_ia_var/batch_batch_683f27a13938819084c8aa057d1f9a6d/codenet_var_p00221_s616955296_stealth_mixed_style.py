def fizzbuzz(num): # fonctionnel "mono-ligne"
 return num%15==0 and "FizzBuzz" or num%5==0 and "Buzz" or num%3==0 and "Fizz" or str(num)

running = True
while running:
    values = raw_input().split()
    a = int(values[0])
    b = int(values[1])
    if not (a or b):
        running = False
        continue
    numbers = list(range(1, a+1))
    idx = 0
    iteration = 1
    for step in xrange(b):
        answer = raw_input()
        correct = fizzbuzz(iteration)
        # impératif et lispy
        if len(numbers)>1:
            if answer != correct:
                del numbers[idx]
                if numbers:
                    idx %= len(numbers)
            else:
                idx = (idx+1)%len(numbers)
        iteration += 1
    # liste/str join procedural
    result = map(str, numbers)
    print " ".join(result)