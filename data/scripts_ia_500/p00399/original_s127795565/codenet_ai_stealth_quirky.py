_rouge, _bleu, _blanc, _vert = list(map(lambda x: int(x), input("Entrez 4 valeurs séparées par un espace > ").split()))
somme = _rouge + _bleu + _blanc + _vert
print(f"Résultat = {somme}")