longueur_cote_a, longueur_cote_b = map(int, raw_input().split())
aire_rectangle = longueur_cote_a * longueur_cote_b
perimetre_rectangle = 2 * (longueur_cote_a + longueur_cote_b)
print aire_rectangle, perimetre_rectangle