def read_input():
    return input()

def parse_N_Q(line):
    N, Q = [int(x) for x in line.split()]
    return N, Q

def exit_condition(N, Q):
    return N == 0 and Q == 0

def create_date_list(size=100):
    return [0] * size

def parse_member_dates(line):
    return [int(x) for x in line.split()]

def update_date_counts(Date, member_dates):
    days_count = member_dates[0]
    for idx in range(1, days_count + 1):
        Date[member_dates[idx] - 1] += 1

def process_members(N, Date):
    for _ in range(N):
        member_line = read_input()
        member_dates = parse_member_dates(member_line)
        update_date_counts(Date, member_dates)

def find_best_meeting_day(Date, Q):
    meeting_day = 0
    member_num = 0
    for i in range(100):
        if Date[i] >= Q and Date[i] > member_num:
            meeting_day = i + 1
            member_num = Date[i]
    return meeting_day

def process_case():
    input_line = read_input()
    N, Q = parse_N_Q(input_line)
    if exit_condition(N, Q):
        exit()
    Date = create_date_list()
    process_members(N, Date)
    best_day = find_best_meeting_day(Date, Q)
    print(best_day)

def main_loop():
    while True:
        process_case()

main_loop()