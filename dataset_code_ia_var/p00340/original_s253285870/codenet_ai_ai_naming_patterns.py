num_1, num_2, num_3, num_4 = map(int, input().split())
if (num_1 == num_2 and num_3 == num_4) or (num_1 == num_3 and num_2 == num_4) or (num_1 == num_4 and num_2 == num_3):
    print("yes")
else:
    print("no")