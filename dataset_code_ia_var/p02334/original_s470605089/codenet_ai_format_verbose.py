number_of_objects, number_of_selections = map(int, input().split())

modulo_value = 10 ** 9 + 7

def compute_binomial_coefficient(numerator_max, denominator_max, modulo):
    
    numerator_product = 1
    for current_value in range(numerator_max - denominator_max + 1, numerator_max + 1):
        numerator_product *= current_value
        numerator_product %= modulo
        
    denominator_product = 1
    for current_value in range(1, denominator_max + 1):
        denominator_product *= current_value
        denominator_product %= modulo
        
    denominator_inverse = pow(denominator_product, modulo - 2, modulo)
    
    binomial_result = (numerator_product * denominator_inverse) % modulo
    
    return binomial_result

result_binomial_coefficient = compute_binomial_coefficient(
    number_of_objects + number_of_selections - 1,
    number_of_objects,
    modulo_value
)

print(result_binomial_coefficient)