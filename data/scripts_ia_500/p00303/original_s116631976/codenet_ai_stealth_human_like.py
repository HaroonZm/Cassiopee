locked_users = {}
watched_devices = {}

n = int(input())
for _ in range(n):
    user, command, device = input().split()
    # storing locked devices per user
    if command == "lock":
        if user not in locked_users:
            locked_users[user] = set([device])
        else:
            locked_users[user].add(device)
    else:
        # for watched devices, store users watching them
        if device not in watched_devices:
            watched_devices[device] = set([user])
        else:
            watched_devices[device].add(user)

found_cycle = False
for starting_user in locked_users:
    current_users = [starting_user]
    while True:
        connected_devices = set()
        for usr in current_users:
            if usr in locked_users:
                connected_devices |= locked_users[usr]
        connected_devices = list(connected_devices)

        next_users = set()
        for dev in connected_devices:
            if dev in watched_devices:
                next_users |= watched_devices[dev]
        next_users = list(next_users)

        if starting_user in next_users:
            print(1)  # cycle detected, user came back to themselves
            found_cycle = True
            break
        elif not next_users:
            break
        current_users = next_users

    if found_cycle:
        break
else:
    print(0)  # no cycles found after trying all users