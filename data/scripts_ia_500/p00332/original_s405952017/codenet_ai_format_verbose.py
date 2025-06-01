def convertir_annee_ere_japonaise_en_annee_occidentale(ere_code, annee_ere) :
    
    if ere_code == 1 :
        return annee_ere + 1867
    elif ere_code == 2 :
        return annee_ere + 1911
    elif ere_code == 3 :
        return annee_ere + 1925
    else :
        return annee_ere + 1988


def convertir_annee_occidentale_en_annee_ere_japonaise(annee_occidentale) :
    
    if annee_occidentale <= 1911 :
        return "M" + str(annee_occidentale - 1867)
    elif annee_occidentale <= 1925 :
        return "T" + str(annee_occidentale - 1911)
    elif annee_occidentale <= 1988 :
        return "S" + str(annee_occidentale - 1925)
    else :
        return "H" + str(annee_occidentale - 1988)


code_ere, annee = map(int, input().split())

if code_ere == 0 :
    print(convertir_annee_occidentale_en_annee_ere_japonaise(annee))
else :
    print(convertir_annee_ere_japonaise_en_annee_occidentale(code_ere, annee))