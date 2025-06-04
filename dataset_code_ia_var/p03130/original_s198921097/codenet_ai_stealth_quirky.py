invocation_of_input = (lambda : [list(map(int, input().split())) for _ in range(3)])()
frequency_basket = [0 for i in range(4)]
[frequency_basket[invocation_of_input[r][c]-1].__iadd__(1) for r in range(3) for c in range(2)]
print(['NO','YES'][all([frequency_basket[idx]<3 for idx in range(4)])])