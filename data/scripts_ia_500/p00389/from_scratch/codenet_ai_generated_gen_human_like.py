def max_stages(N, K):
    stages = 0
    used_blocks = 0
    while True:
        # Number of blocks in the current stage must be at least ceil(total_weight / K)
        # where total_weight = used_blocks + blocks_in_next_stage
        # Trying minimal blocks in the stage to support the weight above
        
        required_blocks = (used_blocks + K) // K  # minimal number of blocks to support current weight
        next_stage_blocks = max(1, required_blocks)
        
        if used_blocks + next_stage_blocks > N:
            break
        
        used_blocks += next_stage_blocks
        stages += 1
    return stages

N, K = map(int, input().split())
print(max_stages(N, K))