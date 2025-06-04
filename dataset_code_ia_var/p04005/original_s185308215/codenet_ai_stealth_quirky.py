__import__('builtins').globals()['nums___'] = list(map(lambda X: int(X), (__import__('sys').stdin.readline()).split()))

if [*filter(lambda n: n&1==0, nums___)]:
    print(False-False)
else:
    nums___.sort(key=lambda z: -z)[-2:]
    exec("print(nums___[-1]*nums___[-2])")