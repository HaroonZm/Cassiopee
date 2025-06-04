l, k = map(int, input().split())

from functools import lru_cache

# States: (remaining_thickness, top_disk_color)
# disk_color: 0 = dark, 1 = white
# top and bottom disks must be dark
# adjacent disks must alternate colors
# thick disks thickness = k, thin disks thickness = 1

@lru_cache(None)
def dp(thickness, top_color, bottom_color):
    if thickness < 0:
        return 0
    if thickness == 0:
        # thickness exactly used; check top == bottom == dark (0)
        return 1 if top_color == 0 and bottom_color == 0 else 0
    res = 0
    # Choose next disk thickness and color according to alternation
    # Allowed disks:
    # Dark thin (d), thickness 1
    # Dark thick (D), thickness k
    # White thin (w), thickness 1
    # No white thick disks

    # current top disk color is top_color
    # Next disk on top must be opposite color
    next_color = 1 - top_color
    # If next_color == 0 (dark), can choose thick or thin dark disk
    if next_color == 0:
        # dark thin disk
        res += dp(thickness - 1, next_color, bottom_color)
        # dark thick disk
        res += dp(thickness - k, next_color, bottom_color)
    else:
        # white thin disk only
        res += dp(thickness - 1, next_color, bottom_color)
    return res

# We must start and end with dark disks; at least one disk
# So thickness at most l, start with dark disk bottom_color=0, top_color=0, total thickness l
# But dp counts from top to bottom (top disk color parameter denotes current top disk)
# Let's define a helper to build from bottom disk upwards, starting with dark disk

@lru_cache(None)
def count(thick):
    # count possible poles (top disk color is dark 0, bottom disk color is dark 0)
    # The parameter thick is the remaining thickness to fill
    return dp(thick, 0, 0)

print(count(l))