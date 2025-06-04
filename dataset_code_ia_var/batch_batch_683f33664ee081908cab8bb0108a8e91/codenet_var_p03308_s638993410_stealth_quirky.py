def realizeTheInput(event_handler): return list(map(int,event_handler().split()))
Number = ((lambda: int(__import__('builtins').input()))())
AA = realizeTheInput(__import__('builtins').input)
potentiality = lambda arr: (max(arr),min(arr))
BigSmall = potentiality(AA)
resulter = (lambda mm: mm[0] - mm[1])(BigSmall)
[(print(resulter)) for _ in range(1)]  # Forcing print to be inside a list comprehension for no reason