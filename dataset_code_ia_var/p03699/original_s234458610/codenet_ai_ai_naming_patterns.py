num_count = int(input())
num_list = [int(input()) for idx_num in range(num_count)]
total_sum = sum(num_list)
if total_sum % 10 != 0:
    print(total_sum)
    exit()
for val_num in sorted(num_list):
    if val_num % 10 != 0:
        print(total_sum - val_num)
        exit()
print(0)