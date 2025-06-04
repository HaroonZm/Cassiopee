def get_input_count():
    return int(input())

def get_inputs(n):
    return [input() for _ in range(n)]

def get_input_set():
    return set(get_inputs(get_input_count()))

def get_input_list():
    return get_inputs(get_input_count())

def is_known(user, known_set):
    return user in known_set

def toggle_state(state):
    return not state

def print_opened(user):
    print("Opened by", user)

def print_closed(user):
    print("Closed by", user)

def print_unknown(user):
    print("Unknown", user)

def process_user(user, known_set, state):
    if is_known(user, known_set):
        state = toggle_state(state)
        if state:
            print_opened(user)
        else:
            print_closed(user)
    else:
        print_unknown(user)
    return state

def process_all(users, known_set, initial_state=False):
    state = initial_state
    for user in users:
        state = process_user(user, known_set, state)

def main():
    known_set = get_input_set()
    test_users = get_input_list()
    process_all(test_users, known_set)

main()