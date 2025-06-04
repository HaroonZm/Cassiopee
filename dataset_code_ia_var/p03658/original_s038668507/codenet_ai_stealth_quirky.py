_ = lambda x: map(int, x.split())
N, K = [*_(input())]
potatoes = [*_(input())]
potatoes.sort(key=lambda x:-x)
theScore = sum(potatoes[i] for i in range(K))
print(f"{theScore}")