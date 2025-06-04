import re

while True:

    number_of_rules, number_of_packets = map(int, input().split())

    if (number_of_rules | number_of_packets) == 0:
        break

    list_of_packet_filtering_rules = []
    list_of_detected_packets = []

    for rule_index in range(number_of_rules):

        rule_type, source_pattern, destination_pattern = input().split()

        is_protect_rule = (rule_type[0] == 'p')
        combined_pattern = (source_pattern + destination_pattern).replace("?", r"\d")
        compiled_regex_pattern = re.compile(combined_pattern)

        list_of_packet_filtering_rules.append((is_protect_rule, compiled_regex_pattern))

    for packet_index in range(number_of_packets):

        packet_source, packet_destination, packet_message = input().split()

        concatenated_packet_address = packet_source + packet_destination

        for is_protect_rule, compiled_regex_pattern in reversed(list_of_packet_filtering_rules):

            if re.match(compiled_regex_pattern, concatenated_packet_address):

                if is_protect_rule:
                    list_of_detected_packets.append((packet_source, packet_destination, packet_message))

                break

    print(len(list_of_detected_packets))

    for detected_packet in list_of_detected_packets:
        print(*detected_packet)