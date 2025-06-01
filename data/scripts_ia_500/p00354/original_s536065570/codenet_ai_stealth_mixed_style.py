jours = ["thu","fri","sat","sun","mon","tue","wed"]
def get_day(index):
    if index < 0:
        return None
    return jours[index % len(jours)]
i = int(input())
print(get_day(i))