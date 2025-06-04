_ = input
LAMBDA = lambda s: [int(i) for i in s.split()]
numbers = LAMBDA(_())
numbers.sort() if numbers else None
print(sum(numbers[:len(numbers)-1]))