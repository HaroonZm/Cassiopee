times = set()
vals1 = map(int, raw_input().split())
count1 = vals1[0]

for i in xrange(count1):
    # transforme heures et minutes en total de minutes
    total_min = vals1[2*i+1]*60 + vals1[2*i+2]
    times.add(total_min)

vals2 = map(int, raw_input().split())
count2 = vals2[0]

for i in xrange(count2):
    total_min = vals2[2*i+1]*60 + vals2[2*i+2]
    times.add(total_min)

times_list = list(times)
times_list.sort()  # tri pour l'affichage

# affichage format hh:mm, remplissage des minutes avec zéro si besoin
print " ".join(":".join([str(t/60), str(t%60).zfill(2)]) for t in times_list)