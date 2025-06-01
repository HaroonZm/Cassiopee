while True:
    k = input("Enter a number (or nothing to quit): ")
    if k == '':
        break
    # I'm assuming k should be an int for division below
    k = int(k)
    numbers = raw_input("Enter numbers separated by space: ").split()
    total = 0
    for n in numbers:
        total += int(n)
    # Hmm, dividing by k-1, hope k > 1 here
    print total / (k - 1)