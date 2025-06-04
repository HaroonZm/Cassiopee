(lambda Q: (__import__('sys').stdout.write(Q[0]+str(len(Q)-2)+Q[-1]+'\n')))(
    (lambda *x: (lambda _:_[0].strip().upper() if _ else 'NONE')(
            [input()]) )()
)