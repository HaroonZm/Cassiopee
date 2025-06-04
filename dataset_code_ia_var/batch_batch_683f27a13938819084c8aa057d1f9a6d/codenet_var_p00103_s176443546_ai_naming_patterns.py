num_innings = int(input())
for inning_idx in range(num_innings):
    out_count = 0
    base_runner_count = 0
    total_score = 0
    while out_count < 3:
        event_input = input()
        if event_input == 'HIT':
            if base_runner_count < 3:
                base_runner_count += 1
            else:
                total_score += 1
        elif event_input == 'HOMERUN':
            total_score += base_runner_count + 1
            base_runner_count = 0
        elif event_input == 'OUT':
            out_count += 1
    print(total_score)