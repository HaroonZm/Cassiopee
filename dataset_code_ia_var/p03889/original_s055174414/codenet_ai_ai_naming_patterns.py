import sys
input_func = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

input_string = input_func().rstrip()

transformed_string = input_string[::-1]
transformed_string = transformed_string.replace('b', '_tmp1_').replace('d', 'b').replace('_tmp1_', 'd')
transformed_string = transformed_string.replace('p', '_tmp2_').replace('q', 'p').replace('_tmp2_', 'q')

is_symmetric = 'Yes' if input_string == transformed_string else 'No'
print(is_symmetric)