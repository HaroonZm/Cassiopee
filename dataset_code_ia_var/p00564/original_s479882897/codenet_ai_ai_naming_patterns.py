input_n, input_a, input_b, input_c, input_d = map(int, input().split())

packs_a_count = input_n // input_a
packs_a_remainder = input_n % input_a

if packs_a_remainder > 0:
    total_cost_a = (packs_a_count + 1) * input_b
else:
    total_cost_a = packs_a_count * input_b

packs_c_count = input_n // input_c
packs_c_remainder = input_n % input_c

if packs_c_remainder > 0:
    total_cost_c = (packs_c_count + 1) * input_d
else:
    total_cost_c = packs_c_count * input_d

if total_cost_a > total_cost_c:
    print(total_cost_c)
else:
    print(total_cost_a)