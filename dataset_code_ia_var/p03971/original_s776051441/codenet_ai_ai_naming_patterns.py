import sys

def read_line():
    return sys.stdin.readline().strip()

def read_int():
    return int(read_line())

def read_int_list():
    return [int(element) for element in read_line().split()]

def process_admission():
    num_candidates, quota_domestic, quota_overseas = read_int_list()
    candidate_types = read_line()
    total_accepted = 0
    overseas_accepted = 0
    for candidate_type in candidate_types:
        if candidate_type == "a" and total_accepted < quota_domestic + quota_overseas:
            total_accepted += 1
            print("Yes")
        elif candidate_type == "b" and total_accepted < quota_domestic + quota_overseas and overseas_accepted < quota_overseas:
            overseas_accepted += 1
            total_accepted += 1
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    process_admission()