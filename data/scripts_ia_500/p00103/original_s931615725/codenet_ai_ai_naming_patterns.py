event_list = []
total_innings = int(input())

RUNNER_NONE   = 0b000
RUNNER_FIRST  = 0b001
RUNNER_SECOND = 0b010
RUNNER_THIRD  = 0b100

current_runner_state = RUNNER_NONE
current_inning_index = 0
current_score = 0
current_out_count = 0
score_per_inning = []

while current_inning_index < total_innings:
    event_input = input()
    if event_input == "HIT":
        if (current_runner_state & RUNNER_THIRD) == RUNNER_THIRD:
            current_score += 1
            current_runner_state &= ~RUNNER_THIRD
        current_runner_state = current_runner_state << 1
        current_runner_state |= RUNNER_FIRST
    elif event_input == "OUT":
        current_out_count += 1
    elif event_input == "HOMERUN":
        if (current_runner_state & RUNNER_THIRD) == RUNNER_THIRD:
            current_score += 1
        if (current_runner_state & RUNNER_SECOND) == RUNNER_SECOND:
            current_score += 1
        if (current_runner_state & RUNNER_FIRST) == RUNNER_FIRST:
            current_score += 1
        current_score += 1
        current_runner_state = RUNNER_NONE
    
    if current_out_count == 3:
        score_per_inning.append(current_score)
        current_inning_index += 1
        current_out_count = 0
        current_score = 0
        current_runner_state = RUNNER_NONE

for inning_index in range(total_innings):
    print(score_per_inning[inning_index])