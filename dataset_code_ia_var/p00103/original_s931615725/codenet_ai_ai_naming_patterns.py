event_log = []
inning_total = int(input())

RUNNER_NONE = 0b000
RUNNER_FIRST = 0b001
RUNNER_SECOND = 0b010
RUNNER_THIRD = 0b100

runner_state = RUNNER_NONE
inning_index = 0
inning_score = 0
out_counter = 0
inning_scores = []

while inning_index < inning_total:
    play_action = input()
    if play_action == "HIT":
        if (runner_state & RUNNER_THIRD) == RUNNER_THIRD:
            inning_score += 1
            runner_state &= ~RUNNER_THIRD
        runner_state = runner_state << 1
        runner_state |= RUNNER_FIRST
    elif play_action == "OUT":
        out_counter += 1
    elif play_action == "HOMERUN":
        if (runner_state & RUNNER_THIRD) == RUNNER_THIRD:
            inning_score += 1
        if (runner_state & RUNNER_SECOND) == RUNNER_SECOND:
            inning_score += 1
        if (runner_state & RUNNER_FIRST) == RUNNER_FIRST:
            inning_score += 1
        inning_score += 1
        runner_state = RUNNER_NONE

    if out_counter == 3:
        inning_scores.append(inning_score)
        inning_index += 1
        out_counter = 0
        inning_score = 0
        runner_state = RUNNER_NONE

for inning_output_index in range(inning_total):
    print(inning_scores[inning_output_index])