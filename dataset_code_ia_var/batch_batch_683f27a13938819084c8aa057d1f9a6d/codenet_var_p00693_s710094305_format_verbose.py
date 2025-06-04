def ip_matches_rule(source_ip, rule_ip_pattern):
    """
    Compare source_ip and rule_ip_pattern character by character.
    If a character in rule_ip_pattern is not '?', it must match the corresponding character in source_ip.
    Returns 1 if the match is successful, 0 otherwise.
    """
    is_match = 1
    for character_index in range(8):
        if rule_ip_pattern[character_index] != '?':
            is_match *= (source_ip[character_index] == rule_ip_pattern[character_index])
    return is_match

def rule_applies_to_message(source_ip, dest_ip, rule):
    """
    Checks if a rule applies to the message defined by source_ip and dest_ip.
    """
    rule_source_ip_pattern = rule[1]
    rule_dest_ip_pattern = rule[2]
    return ip_matches_rule(source_ip, rule_source_ip_pattern) and ip_matches_rule(dest_ip, rule_dest_ip_pattern)

while True:
    number_of_rules, number_of_messages = [int(element) for element in raw_input().split()]
    if number_of_rules == 0 and number_of_messages == 0:
        break
    else:
        permitted_message_count = 0
        permitted_messages = []
        rule_list = []
        for rule_index in range(number_of_rules):
            rule_definition = raw_input().split()
            rule_list.append(rule_definition)
        for message_index in range(number_of_messages):
            message_parts = raw_input().split()
            message_source_ip = message_parts[0]
            message_destination_ip = message_parts[1]
            for rule_offset in range(-1, -number_of_rules-1, -1):
                current_rule = rule_list[rule_offset]
                rule_type = current_rule[0]
                if rule_type == 'deny':
                    if rule_applies_to_message(message_source_ip, message_destination_ip, current_rule):
                        break
                else:
                    if rule_applies_to_message(message_source_ip, message_destination_ip, current_rule):
                        permitted_message_count += 1
                        permitted_messages.append([message_source_ip, message_destination_ip, message_parts[2]])
                        break
        print permitted_message_count
        for permitted_message in permitted_messages:
            print permitted_message[0], permitted_message[1], permitted_message[2]