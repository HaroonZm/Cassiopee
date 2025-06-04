def calculer_operation_pile(operateur, pile_operandes):

    if len(pile_operandes) >= 2:

        deuxieme_operande = int(pile_operandes.pop())
        premier_operande = int(pile_operandes.pop())

        if operateur == '*' :
            resultat_operation = premier_operande * deuxieme_operande

        elif operateur == '+':
            resultat_operation = premier_operande + deuxieme_operande

        elif operateur == '-':
            resultat_operation = premier_operande - deuxieme_operande

        pile_operandes.append(resultat_operation)


expression_postfixee = list(input().split())

pile_calcul = []

for element in expression_postfixee:

    if element == '+' or element == '-' or element == '*':
        calculer_operation_pile(element, pile_calcul)
    else:
        pile_calcul.append(element)

print(pile_calcul[0])