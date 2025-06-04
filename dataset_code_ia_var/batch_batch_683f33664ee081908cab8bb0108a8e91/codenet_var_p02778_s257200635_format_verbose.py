import re

chaine_entree_utilisateur = input()

expression_reguliere_minuscules = '[a-z]'

chaine_modifiee = re.sub(
    expression_reguliere_minuscules,
    'x',
    chaine_entree_utilisateur
)

print(chaine_modifiee)