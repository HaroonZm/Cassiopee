#Time limit exceedsになるので二分探索法を使う
from bisect import bisect_left

while True:
    n, q = map(int, input().split())
    if n == 0:
        break

    era = {} # {西暦: ('元号', 年)}
    years = [] 
    
    for _ in range(n):
        gengou, wa_year, we_year = input().split()
        wa_year = int(wa_year)
        we_year = int(we_year)
        era[we_year] = (gengou, wa_year)
        years.append(we_year)
    
    years_final = sorted(years) 

    for _ in range(q):
        year1 = int(input())
        temp = bisect_left(years_final, year1)
        
        if temp >= len(years_final):
            print('Unknown')
            continue
            
        year2 = years_final[temp]
        gengou, span = era[year2]
        result = year1 - year2 + span

        if result <= 0:
            print('Unknown')
        else:
            print(gengou, result)