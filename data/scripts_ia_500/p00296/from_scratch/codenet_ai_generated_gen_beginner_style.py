N, M, Q = map(int, input().split())
a_list = list(map(int, input().split()))
q_list = list(map(int, input().split()))

students = list(range(N))
current_index = 0  # 最初はゼッケン0の生徒がバトンを持つ（index 0）

for a in a_list:
    # aが偶数なら時計回り（正方向）、奇数なら反時計回り（負方向）
    if a % 2 == 0:
        # 時計回りにa回移動して脱落者を決定
        remove_index = (current_index + a) % len(students)
    else:
        # 反時計回りにa回移動して脱落者を決定
        remove_index = (current_index - a) % len(students)

    # 脱落させる生徒
    eliminated = students.pop(remove_index)

    # 脱落した生徒は時計回りで隣の生徒にバトンを渡す
    # 現在の円で時計回りはremove_indexの位置が次の生徒
    if len(students) == 0:
        break
    current_index = remove_index % len(students)

for q in q_list:
    if q in students:
        print(1)
    else:
        print(0)