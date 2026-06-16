#1
Vorname_Nachname = input("Vorname und Nachname:")
Vorname_Nachname = Vorname_Nachname.split(", ")


while len(Vorname_Nachname) != 2:
    Vorname_Nachname = input(("bitte so eingeben( Vorname , Nachname):"))
    Vorname_Nachname = Vorname_Nachname.split(", ")

Vorname = Vorname_Nachname[0]
Nachname = Vorname_Nachname[1]

print(Vorname, Nachname)

#2

Liste = [1, 2, 3, 4, 5]

print(type(Liste))

klammer = []

for numer in Liste:
    klammer.append(str(numer))

print(type(Liste))

print(' | '.join(klammer))

#3

Zitate = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "A' bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]


for Zitate_text in Zitate:
    Zitate_text2 = Zitate_text[1 : -1]
    print(Zitate_text2)

    # Todo: nochmal mit strip
for zitate_text in Zitate:
    zitate_zeile = zitate_text.strip("'")
    print((zitate_zeile))
