input_count = input()
token_list = raw_input().split()
DYNAMIC_TABLE = [[0]*3 for index_main in xrange(input_count)]
DYNAMIC_TABLE[0] = [int(token_list[0]), -10**18, -10**18]
for index_token in xrange(1, input_count):
    operator_token, value_token = token_list[2*index_token-1: 2*index_token+1]
    numeric_value = int(value_token)
    if operator_token is "+":
        DYNAMIC_TABLE[index_token][0] = max(DYNAMIC_TABLE[index_token-1][0]+numeric_value, DYNAMIC_TABLE[index_token-1][1]-numeric_value, DYNAMIC_TABLE[index_token-1][2]+numeric_value)
        DYNAMIC_TABLE[index_token][1] = max(                                DYNAMIC_TABLE[index_token-1][1]-numeric_value, DYNAMIC_TABLE[index_token-1][2]+numeric_value)
        DYNAMIC_TABLE[index_token][2] =                                         DYNAMIC_TABLE[index_token-1][2]+numeric_value
    else:
        DYNAMIC_TABLE[index_token][0] = max(DYNAMIC_TABLE[index_token-1][0]-numeric_value, DYNAMIC_TABLE[index_token-1][1]+numeric_value, DYNAMIC_TABLE[index_token-1][2]-numeric_value)
        DYNAMIC_TABLE[index_token][1] = max(DYNAMIC_TABLE[index_token-1][0]-numeric_value, DYNAMIC_TABLE[index_token-1][1]+numeric_value, DYNAMIC_TABLE[index_token-1][2]-numeric_value)
        DYNAMIC_TABLE[index_token][2] = max(                                DYNAMIC_TABLE[index_token-1][1]+numeric_value, DYNAMIC_TABLE[index_token-1][2]-numeric_value)
print max(DYNAMIC_TABLE[-1])