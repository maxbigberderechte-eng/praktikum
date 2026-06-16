zeile = f"{10}  .\n+ weiter wörter"

mittelteil = "."

ergebnis = mittelteil.join(["a", "b", "c", " a "])
ergebnis = mittelteil.join(["\n"])
mit_comma = ", ".join(["spam", "spam", "spam"])
mit_comma = ", ".join(["spam"])
# print(mit_comma)
# exit()

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
        zeile_roh = (
            f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons"
        )
        zeile = f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons".join(
            ["1\n2"]
        )
        zeile_andersrum = "\n".join(
            f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons"
        )
        print("-")
        print(zeile)
        print(show, "zr", zeile_roh, "z", zeile, "za", zeile_andersrum)

        ergebnis.append(zeile)
    return ergebnis


ergebnis = print_show_info(series)
print(ergebnis)
for zeile in print_show_info(series):
    print(zeile)
# #emptz = "".join(["\n","\n","\n","\n","\n","\n","\n","\n","\n","\n",])
# #print(emptz)
# print(ergbenis)
#
# #for zeile in print_show_info(series):
#     #print(zeile)
# exit()
# for zeile in ergbenis:
#     print(zeile)