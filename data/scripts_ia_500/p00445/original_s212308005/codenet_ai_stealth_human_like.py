while True:
    try:
        s = input()  # je prends l'entrée sous forme de string
        count_JOI = 0
        count_IOI = 0
        # je parcours la chaîne en m'arrêtant avant les 2 derniers chars
        for i in range(len(s) - 2):
            if s[i] == "J" and s[i+1] == "O" and s[i+2] == "I":
                count_JOI += 1
            elif s[i] == "I" and s[i+1] == "O" and s[i+2] == "I":
                count_IOI += 1
        print(count_JOI)
        print(count_IOI)
    except EOFError:
        # fin du fichier ou entrée terminée => on stoppe
        break
    except:
        # on ignore les autres erreurs, pas super propre mais bon...
        break