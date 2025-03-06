import re

def split_into_groups(file_content, group_size=40):
    """
    Splits the content of a Java file into groups of 'group_size' lines.
    Returns a list of code groups (each group is a string).
    """
    lines = file_content.splitlines()
    groups = []
    for i in range(0, len(lines), group_size):
        group = "\n".join(lines[i:i+group_size])
        groups.append(group)
    return groups
