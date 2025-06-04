import re

while True:

    number_of_rules, number_of_records = map(int, raw_input().split())

    if number_of_rules == 0 and number_of_records == 0:
        break

    rules_list = [0] * number_of_rules

    for rule_index in range(number_of_rules):
        policy_and_pattern, string_pattern, digit_pattern = raw_input().replace("?", "[0-9]").split()
        compiled_regex = re.compile(string_pattern + digit_pattern)
        is_permit_rule = 1 if policy_and_pattern[0] == "p" else 0
        rules_list[rule_index] = [compiled_regex, is_permit_rule]

    permitted_records = []

    for record_index in range(number_of_records):
        string_record, digit_record, user_name = raw_input().split()
        for compiled_regex, is_permit_rule in reversed(rules_list):
            if compiled_regex.search(string_record + digit_record):
                if is_permit_rule:
                    permitted_records.append([string_record, digit_record, user_name])
                break

    print len(permitted_records)

    for string_record, digit_record, user_name in permitted_records:
        print string_record, digit_record, user_name