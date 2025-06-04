# Lecture des entrées
a, b = map(int, input().split())  # nouveau créneau à réserver
N = int(input())  # nombre de réservations existantes

reservations = []
for _ in range(N):
    s, f = map(int, input().split())
    reservations.append((s, f))

# Fonction pour vérifier si deux intervalles se chevauchent
# On considère que deux intervals [a, b) et [s, f) se chevauchent si
# ils ont une intersection stricte.
# Notons que la coïncidence d'extrémités n'est pas un chevauchement.
def est_chevauchement(a, b, s, f):
    # Pas de chevauchement si intervalle 1 fini avant début intervalle 2
    # ou intervalle 2 fini avant début intervalle 1
    if b <= s or f <= a:
        return False
    return True

# Vérification de chevauchement avec chaque réservation existante
for (s_i, f_i) in reservations:
    if est_chevauchement(a, b, s_i, f_i):
        print(1)
        break
else:
    # Si aucune réservation ne chevauche
    print(0)