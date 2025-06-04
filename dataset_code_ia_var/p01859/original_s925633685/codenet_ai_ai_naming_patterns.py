def game_state_update(p1l, p1r, p2l, p2r, turn):
    if turn == 0:
        current_result = 1
        if p1l < 5:
            if p2l < 5:
                current_result = min(current_result, game_state_update(p1l, p1r, p1l + p2l, p2r, 1 - turn))
            if p2r < 5:
                current_result = min(current_result, game_state_update(p1l, p1r, p2l, p1l + p2r, 1 - turn))
        if p1r < 5:
            if p2l < 5:
                current_result = min(current_result, game_state_update(p1l, p1r, p1r + p2l, p2r, 1 - turn))
            if p2r < 5:
                current_result = min(current_result, game_state_update(p1l, p1r, p2l, p1r + p2r, 1 - turn))
    else:
        current_result = 0
        if p2l < 5:
            if p1l < 5:
                current_result = max(current_result, game_state_update(p1l + p2l, p1r, p2l, p2r, 1 - turn))
            if p1r < 5:
                current_result = max(current_result, game_state_update(p1l, p1r + p2l, p2l, p2r, 1 - turn))
        if p2r < 5:
            if p1l < 5:
                current_result = max(current_result, game_state_update(p1l + p2r, p1r, p2l, p2r, 1 - turn))
            if p1r < 5:
                current_result = max(current_result, game_state_update(p1l, p1r + p2r, p2l, p2r, 1 - turn))
    return current_result

player1_left, player1_right = map(int, raw_input().split())
player2_left, player2_right = map(int, raw_input().split())

print "ISONO" if game_state_update(player1_left, player1_right, player2_left, player2_right, 0) == 0 else "NAKAJIMA"