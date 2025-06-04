import sys

def get_criteria():
    return [
        (35.50,  71.0, 'AAA'),
        (37.50,  77.0, 'AA'),
        (40.0,   83.0, 'A'),
        (43.0,   89.0, 'B'),
        (50.0,  105.0, 'C'),
        (55.0,  116.0, 'D'),
        (70.0,  148.0, 'E')
    ]

def get_input_lines():
    return sys.stdin

def parse_line(line):
    return [float(x) for x in line.strip().split()]

def get_r500(parsed):
    return parsed[0]

def get_r1000(parsed):
    return parsed[1]

def check_criteria(r500, r1000, c500, c1000):
    return r500 < c500 and r1000 < c1000

def get_rank_from_criteria(r500, r1000, criteria):
    for item in criteria:
        c500 = get_c500(item)
        c1000 = get_c1000(item)
        rank = get_rank_label(item)
        if check_criteria(r500, r1000, c500, c1000):
            return rank
    return None

def get_c500(criterion):
    return criterion[0]

def get_c1000(criterion):
    return criterion[1]

def get_rank_label(criterion):
    return criterion[2]

def handle_no_rank():
    return 'NA'

def evaluate_rank(r500, r1000):
    criteria = get_criteria()
    rank = get_rank_from_criteria(r500, r1000, criteria)
    if rank is None:
        rank = handle_no_rank()
    return rank

def process_line(line):
    parsed = parse_line(line)
    r500 = get_r500(parsed)
    r1000 = get_r1000(parsed)
    return evaluate_rank(r500, r1000)

def output_result(result):
    print(result)

def main(args):
    lines = get_input_lines()
    for line in lines:
        result = process_line(line)
        output_result(result)

if __name__ == '__main__':
    main(sys.argv[1:])