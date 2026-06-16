
wörter_liste = ["aaa", "bbb", "cc", "ddddddd", "t"]
zahlen_liste = [1, 2, 3, -1, -2, -3]
zahlen_liste_klein = [1, -2]
eingabe = [1, 2, 3, 4, 5, 6]
eingabe2 = [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
nullen = [0, 0]
liste_liste = [[1, 2],[2, 1]]


def add(zahl1, zahl2):
    return zahl1 + zahl2

def subtract(zahl1, zahl2):
    return zahl1 - zahl2

def divide(zahl1, zahl2):
    if zahl2 == 0:
        return 0
    else:
        return zahl1 / zahl2

def multiply(zahl1, zahl2):
    return zahl1 * zahl2

print(divide(6, 0))

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]


def print_show_info(shows):
    ergebnis = []
    for show in shows:
        ergebnis.append(f"{show["title"]} ({show["initial_release"]}) - {show["seasons"]} seasons".join(["\n"]))



    return ergebnis

ergbenis = print_show_info(series)
#emptz = "".join(["\n","\n","\n","\n","\n","\n","\n","\n","\n","\n",])
#print(emptz)
print(ergbenis)

#for zeile in print_show_info(series):
    #print(zeile)
exit()
for zeile in ergbenis:
    print(zeile)



