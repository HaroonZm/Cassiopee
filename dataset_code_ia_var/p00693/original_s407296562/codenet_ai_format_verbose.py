import re

while True:
    number_of_rules, number_of_items = map(int, raw_input().split())
    
    if number_of_rules == 0 and number_of_items == 0:
        break

    compiled_rules = [None] * number_of_rules

    for rule_index in range(number_of_rules):
        rule_prefix, rule_pattern, rule_suffix = raw_input().replace("?", "[0-9]").split()
        regex_pattern = re.compile(rule_pattern + rule_suffix)
        is_positive_rule = rule_prefix[0] == "p"
        compiled_rules[rule_index] = [regex_pattern, is_positive_rule]

    matching_items = []

    for item_index in range(number_of_items):
        item_pattern, item_suffix, item_name = raw_input().split()
        for regex, is_positive_rule in compiled_rules[::-1]:
            if regex.search(item_pattern + item_suffix):
                if is_positive_rule:
                    matching_items.append([item_pattern, item_suffix, item_name])
                break

    print len(matching_items)
    for item_pattern, item_suffix, item_name in matching_items:
        print item_pattern, item_suffix, item_name