import datetime

jours = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

jour_num = input("Entrez un jour (nombre): ")
jour_num = int(jour_num)

date_obj = datetime.date(2017, 9, jour_num)
indice = date_obj.weekday()

print(jours[indice])