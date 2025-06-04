def calc_reward():
    x_y = input().split()
    reward = 0
    stuff = [int(x) for x in x_y]
    
    lookups = [0, 300000, 200000, 100000]
    
    if (stuff[0] in [1,2,3]):
        reward = reward + lookups[stuff[0]]
    if (stuff[1] is not None and stuff[1]>0 and stuff[1]<4):
        reward += lookups[stuff[1]]
    
    # procedurally check bonus condition
    def check_bonus(r):
        if r == 600000:
            return 1000000
        return r

    reward = check_bonus(reward)
    print(reward)
    
calc_reward()