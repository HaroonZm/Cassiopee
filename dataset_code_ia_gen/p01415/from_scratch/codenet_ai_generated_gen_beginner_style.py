N,K,T,U,V,L = map(int, input().split())
D = [int(input()) for _ in range(N)]

time = 0.0
pos = 0
carrots = 0
speed = U
boost_end = 0.0

for i in range(N):
    dist = D[i] - pos
    # If boost is active, check if it lasts until reaching this carrot
    remaining_boost = max(0.0, boost_end - time)
    # Calculate distance can be covered at boosted speed in remaining boost time
    boosted_dist = remaining_boost * V
    if dist <= boosted_dist:
        # All distance to carrot covered at boosted speed
        time += dist / V
        pos = D[i]
    else:
        # Use boost for distance, then normal speed for the rest
        time += remaining_boost
        dist -= boosted_dist
        time += dist / U
        pos = D[i]
    # Decide whether to eat carrot or keep it
    # Simple approach: if we can still eat carrots to get boost, eat
    # We can hold up to K carrots; if holding less than K, keep it
    # But always eat if no boost active
    if boost_end <= time:
        # No boost active, eat carrot
        boost_end = time + T
        speed = V
    else:
        # Have boost active
        if carrots < K:
            carrots += 1 # keep carrot
        else:
            # must eat to get new boost
            boost_end = time + T
    # For simplicity, we do not use stored carrots in this beginner approach

# After last carrot, go to goal
dist = L - pos
remaining_boost = max(0.0, boost_end - time)
boosted_dist = remaining_boost * V
if dist <= boosted_dist:
    time += dist / V
else:
    time += remaining_boost
    dist -= boosted_dist
    time += dist / U

print(time)