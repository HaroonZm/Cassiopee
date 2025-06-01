import datetime

jour = int(input())
date_util = datetime.date(2017, 9, jour)
index_jour = date_util.weekday()

jours_semaine = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

print(jours_semaine[index_jour])