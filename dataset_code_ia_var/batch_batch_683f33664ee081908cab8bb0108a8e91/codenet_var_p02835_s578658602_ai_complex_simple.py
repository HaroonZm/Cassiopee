import functools,operator

res = ["win","bust"][(lambda x: x>=22)(functools.reduce(operator.add,map(int,input().split())))]
print(res)