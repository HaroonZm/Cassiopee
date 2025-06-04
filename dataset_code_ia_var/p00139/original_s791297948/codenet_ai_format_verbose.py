from re import match

pattern_type_A = r"^>'(=+)#\1~$"
pattern_type_B = r"^>\^(Q=)+~~$"

number_of_test_cases = input()

for test_case_index in xrange(number_of_test_cases):

    input_string = raw_input()

    if match(pattern_type_A, input_string) is not None:

        print "A"

    elif match(pattern_type_B, input_string) is not None:

        print "B"

    else:

        print "NA"