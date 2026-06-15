from operator import index


wörter_liste = ["aaa", "bbb", "cc", "ddddddd", "t"]
zahlen_liste = [1, 2, 3, -1, -2, -3]

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
