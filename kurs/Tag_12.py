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
        ergebnis.append(f"{show["title"]} ({show["initial_release"]}) - {show["seasons"]} seasons")

    return ergebnis

for zeile in print_show_info(series):
     print(zeile)

