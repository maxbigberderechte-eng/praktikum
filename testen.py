# Schreibe eine Funktion die (für eine gerade Anzahl von Eingaben) den Abstand(x-y) von je zwei Zahlen berechnet.
from os.path import split

wörter_liste = ["aaa", "bbb", "cc", "ddddddd", "t"]
zahlen_liste = [1, 2, 3, -1, -2, -3]
zahlen_liste_klein = [1, -2]

#zwei_zahlen= input("bitte zwei zahlen eingeben:")


eingabe = [1,2,3,4,5,6]

eingabe2 = [1,2,3,4,5,6,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]
nullen = [0,0]
# Abstand von Zeile darüber [-1,-1,-1]




def abstand(liste_von_zahlen):
    ergebnis_liste = []
    zahl1 = 0
    zahl2 = 0

    #print("einagbeänge", len(liste_von_zahlen))
    for i in range(0, len(liste_von_zahlen)-1,2):
        z1 = liste_von_zahlen[i]
        z2 = liste_von_zahlen[i+1]

        ergebnis = z1 - z2

        ergebnis_liste.append(ergebnis)
        print("i",i,"z1", z1,"z2",z2)

    #for zahl in eingabe:
        #zahl1 = zahl
        #print(zahl1)


    return ergebnis_liste

abstand_von_eingabe = abstand(eingabe)
print(abstand_von_eingabe)


