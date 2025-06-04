#!/usr/bin/env python3

first_interval_length, second_interval_length, target_value = map(int, input().split())

modulo_value = int(1e9 + 7)

if target_value < first_interval_length:
    
    result = target_value % modulo_value

else:
    
    full_cycles_completed = (target_value - second_interval_length) // (first_interval_length - second_interval_length)
    
    result = target_value + second_interval_length * full_cycles_completed
    
    result = result % modulo_value

print(result)