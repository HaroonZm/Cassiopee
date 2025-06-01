#!/usr/bin/python3


nombre_premier, nombre_second = map(int, input().split())

valeur_difference = nombre_premier - nombre_second

if nombre_premier < nombre_second:
    
    valeur_difference = -valeur_difference

print(valeur_difference)