x = int(input())
bits_set = bin(x).count("1")
highest_bit = x.bit_length() - 1
print(max(bits_set, highest_bit))