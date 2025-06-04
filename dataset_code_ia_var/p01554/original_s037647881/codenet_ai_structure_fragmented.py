def read_int():
    return int(input())

def read_inputs(n):
    return [input() for _ in range(n)]

def is_user_known(user, known_users):
    return user in known_users

def print_closed_by(user):
    print("Closed by " + user)

def print_opened_by(user):
    print("Opened by " + user)

def print_unknown(user):
    print("Unknown " + user)

def toggle_door(door_state):
    return not door_state

def handle_known_user(user, door_state):
    if door_state:
        print_closed_by(user)
        door_state = toggle_door(door_state)
    else:
        print_opened_by(user)
        door_state = toggle_door(door_state)
    return door_state

def handle_unknown_user(user):
    print_unknown(user)

def process_access(attempts, known_users):
    door_state = False
    for t in attempts:
        if is_user_known(t, known_users):
            door_state = handle_known_user(t, door_state)
        else:
            handle_unknown_user(t)

def main():
    N = read_int()
    known_users = read_inputs(N)
    M = read_int()
    attempts = [input() for _ in range(M)]
    process_access(attempts, known_users)

main()