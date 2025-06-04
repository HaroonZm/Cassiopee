input_length = int(input())
input_sequence = list(map(int, input().split()))
trend_marker = 1
peak_indices = []
trough_indices = []

for idx in range(input_length - 1):
    if input_sequence[idx] < input_sequence[idx + 1]:
        trough_indices.append(0)
        break
    elif input_sequence[idx] > input_sequence[idx + 1]:
        peak_indices.append(0)
        break

for idx in range(input_length - 1):
    if input_sequence[idx] > input_sequence[idx + 1]:
        if trend_marker == 1:
            peak_indices.append(idx)
            trend_marker = -1
    elif input_sequence[idx] < input_sequence[idx + 1]:
        if trend_marker == -1:
            trough_indices.append(idx)
            trend_marker = 1

for idx in range(input_length - 1, 0, -1):
    if input_sequence[idx - 1] < input_sequence[idx]:
        peak_indices.append(input_length - 1)
        break
    elif input_sequence[idx - 1] > input_sequence[idx]:
        trough_indices.append(input_length - 1)
        break

total_money = 1000
stock_count = 0
peak_count = len(peak_indices)
trough_count = len(trough_indices)

for trough_idx in range(trough_count):
    continue_trading = True
    peak_pointer = trough_idx
    while continue_trading:
        if peak_pointer >= peak_count:
            continue_trading = False
            break
        elif peak_pointer < peak_count:
            if peak_indices[peak_pointer] < trough_indices[trough_idx]:
                peak_pointer += 1
            else:
                break
    if continue_trading:
        purchased = total_money // input_sequence[trough_indices[trough_idx]]
        stock_count += purchased
        total_money -= purchased * input_sequence[trough_indices[trough_idx]]
        total_money += stock_count * input_sequence[peak_indices[peak_pointer]]
        stock_count = 0
print(total_money)