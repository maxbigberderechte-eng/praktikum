from operator import index

wörter_liste = ["aaa", "bbb", "cc", "ddddddd", "t"]
zahlen_liste = [1, 2, 3, -1, -2, -3]
liste_liste = [[1, 2], [2, 1]]


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


# grade = [zahl for zahl in zahlen_liste if zahl % 2==0]
def gerade_zahlen(zahlen_liste):
    ergebnis = []
    for zahl in zahlen_liste:
        if zahl % 2 == 0:
            ergebnis.append(zahl)
    return ergebnis


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
    max_wort = ""
    for wort in liste:
        if len(wort) >= len(max_wort):
            max_wort = wort

    return max_wort


print(längste_elment(wörter_liste))


# Schreibe eine Funktion die aus einer Liste von Zahlen die Summe berechnet.

def summe(zahlen_liste):
    return sum(zahlen_liste)


print(summe(zahlen_liste))


# Schreibe eine Funktion die (für eine gerade Anzahl von Eingaben) den Abstand(x-y) von je zwei Zahlen berechnet.

def abstand(liste_von_zahlen):
    ergebnis_liste = []
    zahl1 = 0
    zahl2 = 0

    # print("einagbeänge", len(liste_von_zahlen))
    for i in range(0, len(liste_von_zahlen) - 1, 2):
        z1 = liste_von_zahlen[i]
        z2 = liste_von_zahlen[i + 1]

        ergebnis = z1 - z2

        ergebnis_liste.append(ergebnis)
        # print("i", i, "z1", z1, "z2", z2)

    # for zahl in eingabe:
    # zahl1 = zahl
    # print(zahl1)

    return ergebnis_liste


abstand_von_eingabe = abstand(zahlen_liste)
print(abstand_von_eingabe)


# Schreibe eine Funktion die aus einer Liste von Listen eine "flache" Liste macht. [[1],[2]] soll zu [1,2] werden)


def enpakte_list(liste_liste):
    ergebnis = []

    for liste in liste_liste:
        ergebnis = ergebnis + liste
    return ergebnis


print(enpakte_list(liste_liste))

# Schreibe eine Funktion die eine Liste von Zahlen sortiert.

def sortierte_zahlen(zahlen_liste):
    ergebnis = []
    while zahlen_liste:
        ergebnis.append(min(zahlen_liste))
        zahlen_liste.remove(min(zahlen_liste))
    return ergebnis

def sortierte_zahlen2(zahlen_liste):
    tausch_fand_statt = True

    while tausch_fand_statt:
        tausch_fand_statt = False

        for i in range(0, len(zahlen_liste) - 1):
            z1 = zahlen_liste[i]
            z2 = zahlen_liste[i + 1]

            if z1 > z2:
                tausch_fand_statt = True
                zahlen_liste[i] = zahlen_liste[i + 1]
                zahlen_liste[i + 1] = z1

    return zahlen_liste

print(sortierte_zahlen(zahlen_liste))
print(sortierte_zahlen2(zahlen_liste))
