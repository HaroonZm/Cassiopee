while True:
    
    try:
        input_values = input().split()
        value_a, value_b, value_c, value_d, value_e, value_f = map(int, input_values)
        
        denominator = (value_b * value_d) - (value_a * value_e)
        numerator_x = (value_c * value_d) - (value_a * value_f)
        
        solution_x = numerator_x / denominator
        solution_y = (value_c - value_b * solution_x) / value_a
        
        print("{:.3f} {:.3f}".format(solution_y, solution_x))
        
    except:
        break