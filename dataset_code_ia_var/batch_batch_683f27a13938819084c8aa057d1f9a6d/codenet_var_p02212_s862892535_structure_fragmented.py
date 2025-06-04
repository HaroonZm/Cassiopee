def read_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_int_list(str_list):
    return [int(x) for x in str_list]

def get_nums():
    s = read_input()
    str_list = split_input(s)
    num_list = convert_to_int_list(str_list)
    return num_list

def sort_nums(nums):
    nums.sort()
    return nums

def get_initial_team_scores():
    return 0, 0

def add_to_team(score, value):
    return score + value

def assign_teams(nums):
    team_a, team_b = get_initial_team_scores()
    team_a = add_to_team(team_a, nums[0])
    team_a = add_to_team(team_a, nums[3])
    team_b = add_to_team(team_b, nums[1])
    team_b = add_to_team(team_b, nums[2])
    return team_a, team_b

def calculate_difference(a, b):
    return abs(a - b)

def display_result(result):
    print(result)

def main():
    nums = get_nums()
    nums = sort_nums(nums)
    team_a, team_b = assign_teams(nums)
    diff = calculate_difference(team_a, team_b)
    display_result(diff)

main()