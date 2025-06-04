def read_integer():
    return int(input())

def read_users(n):
    return [read_single_user() for _ in range(n)]

def read_single_user():
    return input()

def read_attempt():
    return input()

def is_user_known(user, users_list):
    return user in users_list

def open_action(user):
    print("Opened by", user)

def close_action(user):
    print("Closed by", user)

def unknown_action(user):
    print("Unknown", user)

def toggle_lock_state(state):
    return not state

def process_attempt(user, users_list, locked):
    if is_user_known(user, users_list):
        if locked:
            open_action(user)
            return toggle_lock_state(locked)
        else:
            close_action(user)
            return toggle_lock_state(locked)
    else:
        unknown_action(user)
        return locked

def process_all_attempts(m, users_list):
    locked = True
    for _ in range(m):
        user = read_attempt()
        locked = process_attempt(user, users_list, locked)

def main():
    n = read_integer()
    users_list = read_users(n)
    m = read_integer()
    process_all_attempts(m, users_list)

main()