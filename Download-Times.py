
print(""" ____                      _                 _   _____ _                     
|  _ \  _____      ___ __ | | ___   __ _  __| | |_   _(_)_ __ ___   ___  ___ 
| | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |   | | | | '_ ` _ \ / _ \/ __|
| |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |   | | | | | | | | |  __/\__ \ 
|____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|   |_| |_|_| |_| |_|\___||___/\n""")

mode = 0
mode = int((input("1 - Calcul de temps de téléchargements\n2 - Calcul de données téléchargeable dans un temps donné\nQuelle mode voulez-vous choisir ? (1 ou 2) \n")))



def mode_1():

    unite = str(input("\nQuelle unité choisisez-vous ? (Mo ou Go) "))
    taille = float(input("Quelle est la taille de votre téléchargements ? "))
    vitesse = float(input("Quelle est votre vitesse de téléchargement ? (en Mbits/s) "))

    if unite == "Mo" or unite == "mo":
        result_sec = round(taille / (vitesse / 8))
        result_mn = round(taille / (vitesse / 8) / 60, 1)
        result_h = round(taille / (vitesse / 8) / 3600, 2)

    elif unite == "Go" or unite == "go":
        result_sec = round(taille * 1000 / (vitesse / 8))
        result_mn = round(taille * 1000 / (vitesse / 8) / 60, 1)
        result_h = round(taille * 1000 / (vitesse / 8) / 3600, 2)

    else:
        print("Choisisez un unité valable.")
        input()
        exit()

    print("\nVotre Téléchargement prendra :")

    def seconde(iterable):
        jour = int(iterable / 86400)

        heure = int((iterable - (jour * 86400)) / 3600)

        minute = int((iterable - (86400 * jour) - (3600 * heure)) / 60)

        seconde = int(iterable - (86400 * jour) - (3600 * heure) - (60 * minute))

        time = (jour, heure, minute, seconde)

        return time



    resultat = (seconde(result_sec))

    if (resultat[0]) < 1:
        print("%s heures, %s minutes, et %s secondes." % (resultat[1], resultat[2], resultat[3]))

    else:
        print("%s jours, %s heure(s), %s minute(s), et %s seconde(s)." % (resultat[0], resultat[1], resultat[2], resultat[3]))

    cut = str(input("\nVoulez-vous découper ce temps en plage horaire ? "))

    if cut == "y" or cut == "yes" or cut == "oui":
        temps_h = float(input("En combien d'heure(s) voulez-vous découper votre temps de téléchargement ? "))
        temps_s = temps_h * 3600
        plage = int(result_sec / temps_s)
        plus_plage = ((result_sec / temps_s) - plage) * temps_s
        plus_plage_hm = (seconde(plus_plage))

    elif cut == "n" or cut == "non" or cut == "no":
        input()
        exit()

    else:
        print("Veuillez répondre correctement.")
        input()
        exit()


    print("\nVous pourrez télécharger votre fichier en", str(plage), "plage(s) horaire(s), plus", (plus_plage_hm[0]), "heure(s),", (plus_plage_hm[1]), "minute(s) et", (plus_plage_hm[2]), "seconde(s).")


    input()



def mode_2():

    temps_h = int(input("\nCombien d'heure durera votre téléchargement ? "))
    temps_mn = int(input("Combien de minute ? (en plus des heures) "))
    vitesse = float(input("Quelle est votre vitesse de téléchargement ? (en Mbits/s) "))

    temps_sec = (temps_h * 3600) + (temps_mn * 60)
    result_mo = temps_sec * (vitesse / 8)

    def taille(taille_mo):
        Go = int((taille_mo / 1000))

        Mo = int(taille_mo - (Go * 1000))

        result = (Go, Mo)

        return result

    resultat = (taille(result_mo))

    print("\nVous pourrez télécharger :")
    print("%s Go et %s Mo." % (resultat[0], resultat[1]))
    input()



if mode == 1:
    mode_1()

elif mode == 2:
    mode_2()

else:
    print("Choisissez un mode valable.")
    input(9)
    exit()
