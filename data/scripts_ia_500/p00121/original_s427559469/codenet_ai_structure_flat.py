MOVE = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5], [1, 4, 6], [2, 5, 7], [3, 6]]
answers = {"01234567": 0}
q = [[0, "01234567"]]
while len(q) != 0:
    g, field = q.pop(0)
    a = field.find("0")
    tmp_field_list = list(field)
    for b in MOVE[a]:
        tmp_field_list[a], tmp_field_list[b] = tmp_field_list[b], tmp_field_list[a]
        tmp = "".join(tmp_field_list)
        tmp_field_list[a], tmp_field_list[b] = tmp_field_list[b], tmp_field_list[a]
        if tmp not in answers:
            answers[tmp] = g + 1
            q.append([g + 1, tmp])
while True:
    try:
        line = raw_input()
        line = line.replace(" ", "")
        print answers[line]
    except:
        break