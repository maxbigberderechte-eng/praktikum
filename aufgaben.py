from operator import index

wörter_liste = ["aaa", "bbb", "cc", "ddddddd", "t"]
zahlen_liste = [1, 2, 3, -1, -2, -3]

# Schreibe eine Funktion die das Mininum einer Liste von Integern findet.

def minimum(zahlen_liste):
    return min(zahlen_liste)


print(minimum(zahlen_liste))


# Schreibe eine Funktion die aus einer Liste nur die ersten n Einträge zurückgibt.

def erster_eintrag(Liste, anzahl):
    return Liste[0: anzahl]


print(erster_eintrag(wörter_liste, 1))


# Schreibe eine Funktion die das Maximum einer Liste von Integern findet.
def maximum(zahlen_liste):
    return max(zahlen_liste)


print(maximum(zahlen_liste))


# Schreibe eine Funktion die den Index des kleinsten Elements findet.

def kleinstes_elment(liste):
    return index(min(liste))


# for i in range(len(lite)):
# element[i]
# len "hh")

print(kleinstes_elment(zahlen_liste))


# Schreibe eine Funktion die aus einer Liste von Integern nur die geraden Integer findet.

def gerade_zahlen(zahlen_liste):
    ergebnis = []
    for zahl in zahlen_liste:
        if zahl % 2 == 0:
            ergebnis.append(zahl)
    return  ergebnis

print(gerade_zahlen(zahlen_liste))

# Schreibe eine Funktion die aus einer Liste von Wörtern das längste findet.


def längste_elment(liste):
    ergebnis = []

    for wort in liste:
        wort_länge = len(wort)
        ergebnis.append(wort_länge)

    for wort in liste:
        wort_länge = len(wort)
        if wort_länge == max(ergebnis):
            return wort


def längste_elment(liste):
    max_wort =""
    for wort in liste:
        if len(wort) >=len(max_wort):
            max_wort =wort

    return max_wort



print(längste_elment(wörter_liste))

# Schreibe eine Funktion die aus einer Liste von Zahlen die Summe berechnet.

def summe(zahlen_liste):
    return sum(zahlen_liste)

print(summe(zahlen_liste))

# Schreibe eine Funktion die (für eine gerade Anzahl von Eingaben) den Abstand(x-y) von je zwei Zahlen berechnet.



