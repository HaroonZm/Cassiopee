left_isono, right_isono = map(int, input().split())
left_nakajima, right_nakajima = map(int, input().split())
TURN_ISONO = True
TURN_NAKAJIMA = False

def recursive_search(liso, risco, lnaka, rnaka, current_turn):
    if liso is None and risco is None:
        return False
    if lnaka is None and rnaka is None:
        return True

    if current_turn == TURN_ISONO:
        result = False
        if liso and lnaka:
            new_lnaka = lnaka + liso if lnaka + liso < 5 else None
            result = result or recursive_search(liso, risco, new_lnaka, rnaka, not current_turn)
        if liso and rnaka:
            new_rnaka = rnaka + liso if rnaka + liso < 5 else None
            result = result or recursive_search(liso, risco, lnaka, new_rnaka, not current_turn)
        if risco and lnaka:
            new_lnaka = lnaka + risco if lnaka + risco < 5 else None
            result = result or recursive_search(liso, risco, new_lnaka, rnaka, not current_turn)
        if risco and rnaka:
            new_rnaka = rnaka + risco if rnaka + risco < 5 else None
            result = result or recursive_search(liso, risco, lnaka, new_rnaka, not current_turn)

    if current_turn == TURN_NAKAJIMA:
        result = True
        if liso and lnaka:
            new_liso = liso + lnaka if liso + lnaka < 5 else None
            result = result and recursive_search(new_liso, risco, lnaka, rnaka, not current_turn)
        if liso and rnaka:
            new_liso = liso + rnaka if liso + rnaka < 5 else None
            result = result and recursive_search(new_liso, risco, lnaka, rnaka, not current_turn)
        if risco and lnaka:
            new_risco = risco + lnaka if risco + lnaka < 5 else None
            result = result and recursive_search(liso, new_risco, lnaka, rnaka, not current_turn)
        if risco and rnaka:
            new_risco = risco + rnaka if risco + rnaka < 5 else None
            result = result and recursive_search(liso, new_risco, lnaka, rnaka, not current_turn)

    return result

if recursive_search(left_isono, right_isono, left_nakajima, right_nakajima, TURN_ISONO):
    print("ISONO")
else:
    print("NAKAJIMA")