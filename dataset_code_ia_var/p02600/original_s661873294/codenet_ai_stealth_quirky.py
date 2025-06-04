get_score = lambda v: (8 if 400<=v<=599 else
                       7 if 600<=v<=799 else
                       6 if 800<=v<=999 else
                       5 if 1000<=v<=1199 else
                       4 if 1200<=v<=1399 else
                       3 if 1400<=v<=1599 else
                       2 if 1600<=v<=1799 else 1)

try:
    __import__('builtins').exec('y=int(input())')
except Exception as e:
    raise SystemExit('Valeur d’entrée invalide:',e)
finally:
    print(get_score(locals().get('y',0)))