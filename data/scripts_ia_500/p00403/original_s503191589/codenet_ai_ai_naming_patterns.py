nombre_de_operations = int(input())
liste_operations = list(map(int, input().split()))
pile_cavite = []

for index_operation in range(nombre_de_operations):
    operation_courante = liste_operations[index_operation]
    
    if operation_courante > 0:
        if operation_courante in pile_cavite:
            print(index_operation + 1)
            break
        else:
            pile_cavite.append(operation_courante)
    else:
        operation_inverse = -operation_courante
        if operation_inverse in pile_cavite:
            if pile_cavite[-1] == operation_inverse:
                pile_cavite.remove(operation_inverse)
            else:
                print(index_operation + 1)
                break
        else:
            print(index_operation + 1)
            break
    if index_operation + 1 == nombre_de_operations:
        print("OK")