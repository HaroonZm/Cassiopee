import sys
sys.setrecursionlimit(10000000)
MOD_CONST = 10 ** 9 + 7
INF_CONST = 10 ** 15

class UnionFindStruct:
    def __init__(self, node_count):
        self.node_count = node_count
        self.parent_list = [-1] * node_count

    def find_root(self, node_idx):
        if self.parent_list[node_idx] < 0:
            return node_idx
        else:
            self.parent_list[node_idx] = self.find_root(self.parent_list[node_idx])
            return self.parent_list[node_idx]

    def merge_groups(self, node_x, node_y):
        root_x = self.find_root(node_x)
        root_y = self.find_root(node_y)
        if root_x == root_y:
            return
        if self.parent_list[root_x] > self.parent_list[root_y]:
            root_x, root_y = root_y, root_x
        self.parent_list[root_x] += self.parent_list[root_y]
        self.parent_list[root_y] = root_x

    def in_same_group(self, node_x, node_y):
        return self.find_root(node_x) == self.find_root(node_y)

    def group_members(self, node_idx):
        root = self.find_root(node_idx)
        return [i for i in range(self.node_count) if self.find_root(i) == root]

    def group_size(self, node_idx):
        return -self.parent_list[self.find_root(node_idx)]

    def root_list(self):
        return [i for i, v in enumerate(self.parent_list) if v < 0]

    def group_count(self):
        return len(self.root_list())

    def group_member_dict(self):
        return {root: self.group_members(root) for root in self.root_list()}

def process_query_group(group_constraint_count, god_count, evil_count):
    total_char_count = god_count + evil_count
    uf_struct = UnionFindStruct(total_char_count * 2)
    is_valid = True
    for _ in range(group_constraint_count):
        input_line = input().split()
        idx_a = int(input_line[0]) - 1
        idx_b = int(input_line[1]) - 1
        relation = input_line[2]
        if relation == 'yes':
            if idx_a == idx_b:
                continue
            if uf_struct.in_same_group(idx_a, idx_b + total_char_count) or uf_struct.in_same_group(idx_a + total_char_count, idx_b):
                is_valid = False
                break
            uf_struct.merge_groups(idx_a, idx_b)
            uf_struct.merge_groups(idx_a + total_char_count, idx_b + total_char_count)
        else:
            if idx_a == idx_b:
                is_valid = False
                break
            if uf_struct.in_same_group(idx_a, idx_b) or uf_struct.in_same_group(idx_a + total_char_count, idx_b + total_char_count):
                is_valid = False
                break
            uf_struct.merge_groups(idx_a, idx_b + total_char_count)
            uf_struct.merge_groups(idx_a + total_char_count, idx_b)
    if not is_valid:
        print('no')
        return
    for idx in range(total_char_count):
        if uf_struct.in_same_group(idx, idx + total_char_count):
            print('no')
            return

    root_list = uf_struct.root_list()
    group_members_dict = uf_struct.group_member_dict()
    group_cand_list = []
    group_char_count_list = []
    char_selected_flag = [0] * total_char_count

    for root in root_list:
        god_cnt = 0
        evil_cnt = 0
        is_group_valid = True
        for member_idx in group_members_dict[root]:
            if member_idx < total_char_count:
                if char_selected_flag[member_idx] == 1:
                    is_group_valid = False
                    break
                god_cnt += 1
                char_selected_flag[member_idx] = 1
            else:
                if char_selected_flag[member_idx - total_char_count] == 1:
                    is_group_valid = False
                    break
                evil_cnt += 1
                char_selected_flag[member_idx - total_char_count] = 1
        if is_group_valid:
            group_cand_list.append(root)
            group_char_count_list.append((god_cnt, evil_cnt))

    dp_table = [[0] * (god_count + 1) for _ in range(len(group_cand_list) + 1)]
    if group_char_count_list[0][0] <= god_count:
        dp_table[1][group_char_count_list[0][0]] = 1
    if group_char_count_list[0][1] <= god_count:
        dp_table[1][group_char_count_list[0][1]] += 1
    for group_idx, (group_god_cnt, group_evil_cnt) in enumerate(group_char_count_list[1:], 1):
        for god_idx in range(god_count + 1):
            if god_idx - group_evil_cnt >= 0:
                dp_table[group_idx + 1][god_idx] += dp_table[group_idx][god_idx - group_evil_cnt]
            if god_idx - group_god_cnt >= 0:
                dp_table[group_idx + 1][god_idx] += dp_table[group_idx][god_idx - group_god_cnt]
    if dp_table[-1][god_count] == 1:
        result_list = []
        curr_god_count = god_count
        for rev_group_idx in range(len(group_cand_list) - 1, 0, -1):
            if 0 <= curr_god_count - group_char_count_list[rev_group_idx][0] <= god_count and dp_table[rev_group_idx][curr_god_count - group_char_count_list[rev_group_idx][0]] == 1:
                for mem_idx in group_members_dict[group_cand_list[rev_group_idx]]:
                    if mem_idx < total_char_count:
                        result_list.append(mem_idx + 1)
                curr_god_count -= group_char_count_list[rev_group_idx][0]
            elif 0 <= curr_god_count - group_char_count_list[rev_group_idx][1] <= god_count and dp_table[rev_group_idx][curr_god_count - group_char_count_list[rev_group_idx][1]] == 1:
                for mem_idx in group_members_dict[group_cand_list[rev_group_idx]]:
                    if mem_idx >= total_char_count:
                        result_list.append(mem_idx - total_char_count + 1)
                curr_god_count -= group_char_count_list[rev_group_idx][1]
        if curr_god_count > 0:
            if curr_god_count == group_char_count_list[0][0]:
                for mem_idx in group_members_dict[group_cand_list[0]]:
                    if mem_idx < total_char_count:
                        result_list.append(mem_idx + 1)
            elif curr_god_count == group_char_count_list[0][1]:
                for mem_idx in group_members_dict[group_cand_list[0]]:
                    if mem_idx >= total_char_count:
                        result_list.append(mem_idx - total_char_count + 1)
        result_list.sort()
        if result_list:
            print('\n'.join(map(str, result_list)))
        print('end')
    else:
        print('no')

def main_entry():
    while True:
        input_line = list(map(int, input().split()))
        query_n_val, group_god_cnt, group_evil_cnt = input_line
        if query_n_val == 0 and group_god_cnt == 0 and group_evil_cnt == 0:
            return
        process_query_group(query_n_val, group_god_cnt, group_evil_cnt)

if __name__ == '__main__':
    main_entry()