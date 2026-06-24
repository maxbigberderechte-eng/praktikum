import random

zuföllige_zahl = random.randrange(101)
gespielte_versuche = 1
eingaben_korrekt = False
versuche_text = "Versucheingeben zwichen 3 - 10 oder (endlos) für endlose versuche:"
versuche = input(versuche_text)

def spiel(zuföllige_nummer):
    user_nummer = input("bitte ihre zahl eingeben:")
    eingaben_korrekt = False

    while not eingaben_korrekt:
        try:
            user_nummer = int(user_nummer)
            eingaben_korrekt = True
        except ValueError:
            print(f"{user_nummer} ist keine gültige eingabe")
            user_nummer = input("bitte ihre zahl eingeben:")

    try:
        user_nummer = int(user_nummer)
    except ValueError:
        exit()

    if zuföllige_nummer - user_nummer == 0:
        print("RICHTIG!")
        return False

    elif zuföllige_nummer - user_nummer <= 5 and zuföllige_nummer - user_nummer >= -5:
        print("Fast!")

        if zuföllige_nummer - user_nummer < 0:
            print("Die Geheimzahl ist kleiner")
        else:
            print("Die Geheimzahl ist grösser")
        return True

    elif zuföllige_nummer - user_nummer <= 15 and zuföllige_nummer - user_nummer >= -15:
        print("Nicht schlecht!")

        if zuföllige_nummer - user_nummer < 0:
            print("Die Geheimzahl ist kleiner")
        else:
            print("Die Geheimzahl ist grösser")
        return True

    elif zuföllige_nummer - user_nummer < 0:
        print("Die Geheimzahl ist kleiner")
        return True
    else:
        print("Die Geheimzahl ist grösser")
        return True


while not eingaben_korrekt:
    if versuche == "endlos":
        eingaben_korrekt = True
    else:
        try:
            versuche = int(versuche)
            if versuche <3 or versuche >10:
                raise ValueError
            eingaben_korrekt = True
        except ValueError:
            versuche = input(f"{versuche} ist keine gültige eingabe \n{versuche_text}")


if versuche == "endlos":
    while spiel(zuföllige_zahl):
        gespielte_versuche += 1
        print(gespielte_versuche)
    print(f"du hast {gespielte_versuche} versuche gebraucht")
    exit()

for i in range(0, versuche):
    print(f"Noch {versuche - i} versuche")
    if spiel(zuföllige_zahl) == False:
        print(f"mit {i +1} versuchen")
        exit()
print(f"Du hast verloren, die Zahl war {zuföllige_zahl}")
