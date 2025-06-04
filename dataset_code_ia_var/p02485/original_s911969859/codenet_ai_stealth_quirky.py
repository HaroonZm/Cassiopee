done = False
lmb = lambda x, y: x + y
acc = lambda xs: reduce(lmb, xs)
ask = lambda: [int(n) for n in raw_input()]
while not done:
    got = ask()
    if got == [0]:
        done = True
    else:
        print(acc(got))