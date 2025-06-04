import sys

read_line_from_stdin = sys.stdin.readline

def main():
    number_of_monsters, required_damage = map(int, read_line_from_stdin().split())
    
    monster_slash_damages = [0] * number_of_monsters
    monster_throw_damages = [0] * number_of_monsters
    
    for monster_index in range(number_of_monsters):
        slash_damage, throw_damage = map(int, read_line_from_stdin().split())
        monster_slash_damages[monster_index] = slash_damage
        monster_throw_damages[monster_index] = throw_damage

    monster_slash_damages.sort()
    monster_throw_damages.sort()

    accumulated_damage_from_throws = 0
    minimum_attacks_needed = 0

    for reverse_index in reversed(range(number_of_monsters)):
        if monster_throw_damages[reverse_index] < monster_slash_damages[-1]:
            break
        accumulated_damage_from_throws += monster_throw_damages[reverse_index]
        minimum_attacks_needed += 1
        if accumulated_damage_from_throws >= required_damage:
            break

    if accumulated_damage_from_throws < required_damage:
        remaining_damage = required_damage - accumulated_damage_from_throws
        max_slash_damage = monster_slash_damages[-1]
        full_slash_attacks, leftover_damage = divmod(remaining_damage, max_slash_damage)
        minimum_attacks_needed += full_slash_attacks
        if leftover_damage > 0:
            minimum_attacks_needed += 1

    print(minimum_attacks_needed)

if __name__ == "__main__":
    main()