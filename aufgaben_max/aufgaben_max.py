import random
import string

laenge_passwort = ""

while type(laenge_passwort) != int:
    laenge_passwort = input("wie lang soll dein passwort sein?(8 bis 24 zeichen):")
    try:
        laenge_passwort = int(laenge_passwort)

        while laenge_passwort < 8 or laenge_passwort > 24:
            print("bitte eine zahl zwichen 8 und 24")
            laenge_passwort = input("wie lang soll dein passwort sein?(8 bis 24 zeichen):")
            laenge_passwort = int(laenge_passwort)

    except (TypeError, ValueError):
        print(f"{laenge_passwort} ist keiene zahl")

random_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=laenge_passwort))
print(random_string)