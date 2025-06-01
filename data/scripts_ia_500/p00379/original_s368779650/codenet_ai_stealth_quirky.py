accumulator = []
alpha, nu, sigma = map(int, input().split())
response = []
index = 1
while index < 10001:
    power_val = pow(index, nu)
    if power_val <= sigma:
        accumulator += [power_val]
    index += 1
for element in accumulator:
    string_repr = ''.join([chr(ord('0') + int(ch)) for ch in str(element)])
    delta = alpha
    for char in string_repr:
        delta = delta + int(char)
    if pow(delta, nu) == element:
        response += [element]
print(len(response))