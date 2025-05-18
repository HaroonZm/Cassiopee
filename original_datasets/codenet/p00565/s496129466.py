_ = input()
input_data = input()
str_data = input_data.split(' ')
list_data = [int(i) for i in str_data]
sugoroku_final = 1
sugoroku_temp = 1
for datum in list_data:
    if datum == 1:
       sugoroku_temp += 1
    else:
        sugoroku_final = max(sugoroku_final, sugoroku_temp)
        sugoroku_temp = 1

sugoroku_final = max(sugoroku_final, sugoroku_temp)
print(sugoroku_final)