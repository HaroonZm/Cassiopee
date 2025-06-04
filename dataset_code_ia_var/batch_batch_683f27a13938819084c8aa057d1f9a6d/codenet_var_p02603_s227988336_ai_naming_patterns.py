input_length = int(input())
input_sequence = list(map(int, input().split()))
initial_money = 1000
compressed_sequence = [input_sequence[0]]
transaction_points = []

for idx in range(input_length - 1):
    if input_sequence[idx] != input_sequence[idx + 1]:
        compressed_sequence.append(input_sequence[idx + 1])

trend_status = 0
if len(compressed_sequence) < 2:
    print(initial_money)
    exit()

for idx in range(len(compressed_sequence) - 1):
    if trend_status == 0 and compressed_sequence[idx] < compressed_sequence[idx + 1]:
        trend_status = 1
        transaction_points.append(compressed_sequence[idx])
    elif trend_status == 1 and compressed_sequence[idx] > compressed_sequence[idx + 1]:
        trend_status = 0
        transaction_points.append(compressed_sequence[idx])

if ((compressed_sequence[-1] > compressed_sequence[-2] and trend_status == 1) or
    (compressed_sequence[-1] < compressed_sequence[-2] and trend_status == 0)):
    transaction_points.append(compressed_sequence[-1])

if len(transaction_points) < 2:
    print(initial_money)
    exit()

if transaction_points[-1] < transaction_points[-2]:
    transaction_points.pop()

current_stocks = 0
current_money = initial_money
for idx, price_point in enumerate(transaction_points):
    if idx % 2 == 0:
        current_stocks = current_money // price_point
        current_money = current_money % price_point
    else:
        current_money += current_stocks * price_point
        current_stocks = 0

print(current_money)