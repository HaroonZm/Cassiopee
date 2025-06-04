def read_integer():
    return int(input())

def read_inputs(n):
    return [input() for _ in range(n)]

def is_user_known(user, known_users):
    return user in known_users

def print_opened_by(user):
    print('Opened by ' + user)

def print_closed_by(user):
    print('Closed by ' + user)

def print_unknown(user):
    print('Unknown ' + user)

def handle_known_user(user, opened_state):
    if opened_state:
        print_closed_by(user)
        opened_state = False
    else:
        print_opened_by(user)
        opened_state = True
    return opened_state

def handle_unknown_user(user):
    print_unknown(user)

def process_action(user, known_users, opened_state):
    if is_user_known(user, known_users):
        opened_state = handle_known_user(user, opened_state)
    else:
        handle_unknown_user(user)
    return opened_state

def process_all_actions(actions, known_users):
    opened = False
    for action in actions:
        opened = process_action(action, known_users, opened)
        
def main():
    N = read_integer()
    U = read_inputs(N)
    M = read_integer()
    T = read_inputs(M)
    process_all_actions(T, U)

main()