K = int(input())
I_poses = [input() for _ in range(K)]
N_poses = [input() for _ in range(K)]

I_power = 0
N_power = 0
winner = None
round_won = 0

for i in range(K):
    I_pose = I_poses[i]
    N_pose = N_poses[i]

    # Determine if each is attacking this round and their attack powers
    I_attacking = (I_pose == "kougekida")
    N_attacking = (N_pose == "kougekida")

    # Check victory conditions only if winner not decided yet
    if winner is None:
        # Case both attack
        if I_attacking and N_attacking:
            # Both power 0 => no win
            if I_power == 0 and N_power == 0:
                pass
            # One power 0 one power > 0 => higher power wins
            elif I_power == 0 and N_power > 0:
                winner = "Nakajima-kun"
                round_won = i+1
            elif N_power == 0 and I_power > 0:
                winner = "Isono-kun"
                round_won = i+1
            else:
                # both 1 or more, compare
                if I_power > N_power:
                    winner = "Isono-kun"
                    round_won = i+1
                elif N_power > I_power:
                    winner = "Nakajima-kun"
                    round_won = i+1
                else:
                    # same power => no win
                    pass

        # One attacks, one not attack
        elif I_attacking and not N_attacking:
            # I_power == 0 => I punish by N win?
            if I_power == 0:
                # I attack at 0 power => illegal, N win
                winner = "Nakajima-kun"
                round_won = i+1
            else:
                # I_attack >=1
                # Check opponent pose:
                if N_pose == "tameru":
                    # N is charging, attacked => I win
                    winner = "Isono-kun"
                    round_won = i+1
                elif N_pose == "mamoru":
                    # Defense pose, if attacker power == 5 => attacker win, else no win
                    if I_power == 5:
                        winner = "Isono-kun"
                        round_won = i+1

        elif N_attacking and not I_attacking:
            # N_power == 0 => illegal, I win
            if N_power == 0:
                winner = "Isono-kun"
                round_won = i+1
            else:
                # N_attack >=1
                if I_pose == "tameru":
                    # I is charging, attacked => N win
                    winner = "Nakajima-kun"
                    round_won = i+1
                elif I_pose == "mamoru":
                    # defense pose, attacker power==5 attacker win else no win
                    if N_power == 5:
                        winner = "Nakajima-kun"
                        round_won = i+1

    # After checking victory, update powers according to poses

    # Handle Isono power changes
    if I_pose == "tameru":
        if I_power <5:
            I_power +=1
        # else power capped at 5
    elif I_pose == "kougekida":
        # power reset to zero only if power >=1 and attacked
        if I_power >=1:
            I_power =0
    # mamoru does not change power

    # Handle Nakajima power changes
    if N_pose == "tameru":
        if N_power <5:
            N_power +=1
    elif N_pose == "kougekida":
        if N_power >=1:
            N_power =0
    # mamoru no change

# Output
if winner is None:
    print("Hikiwake-kun")
else:
    print(winner)