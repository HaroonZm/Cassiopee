while True:
    input_count = input()
    if input_count == 0:
        break
    group_members_dict = {}
    first_group_name = None
    for entry_index in range(input_count):
        group_entry, members_entry = raw_input().split(":")
        if entry_index == 0:
            first_group_name = group_entry
        group_members_dict[group_entry] = set(members_entry[:-1].split(","))
        while True:
            updated = False
            for outer_group in group_members_dict:
                if outer_group == first_group_name:
                    continue
                for inner_group in group_members_dict:
                    if outer_group in group_members_dict[inner_group]:
                        group_members_dict[inner_group] |= group_members_dict[outer_group]
                        group_members_dict[inner_group].discard(outer_group)
                        updated = True
            if not updated:
                break
    print len(group_members_dict[first_group_name])