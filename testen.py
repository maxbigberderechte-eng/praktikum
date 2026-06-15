# Schreibe eine Funktion die (für eine gerade Anzahl von Eingaben) den Abstand(x-y) von je zwei Zahlen berechnet.
from os.path import split

wörter_liste = ["aaa", "bbb", "cc", "ddddddd", "t"]
zahlen_liste = [1, 2, 3, -1, -2, -3]
zahlen_liste_klein = [1, -2]

#zwei_zahlen= input("bitte zwei zahlen eingeben:")


eingabe = [1,2,3,4,5,6]
# Abstand von Zeile darüber [-1,-1,-1]




def abstand(zwei_zahlen):
    print("eingaeb",zwei_zahlen)
    ergebnis = []
    #zwei_zahlen_liste = int(zwei_zahlen.split(","))
    #return (zwei_zahlen_liste[0] - zwei_zahlen_liste[1])
    print("ergebnis", ergebnis)
    return ergebnis

abstand_von_eingabe = abstand(eingabe)

print(abstand_von_eingabe)


