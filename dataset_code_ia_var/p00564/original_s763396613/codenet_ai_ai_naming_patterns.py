val_input_1, val_input_2, val_input_3, val_input_4, val_input_5 = map(int, input().split())

res_method_1 = ((val_input_1 // val_input_2) * val_input_3) if val_input_1 % val_input_2 == 0 else ((val_input_1 // val_input_2 + 1) * val_input_3)
res_method_2 = ((val_input_1 // val_input_4) * val_input_5) if val_input_1 % val_input_4 == 0 else ((val_input_1 // val_input_4 + 1) * val_input_5)

print(min(res_method_1, res_method_2))