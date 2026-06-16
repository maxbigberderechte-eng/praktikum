mitarbeiter = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00),
]


def lohn_für_arbeiter(mitarbeiter):
    stunden = mitarbeiter[1]
    gehalt = mitarbeiter[2]
    if stunden < 40:
        return stunden * gehalt
    else:
        return (gehalt * 1.1 * (stunden - 40)) + 40 * gehalt


for mitarbeiter_eintrag in mitarbeiter:
    momentaner_lohn = lohn_für_arbeiter(mitarbeiter_eintrag)
    mitarbeiter_name = mitarbeiter_eintrag[0]
    stunden = mitarbeiter_eintrag[1]
    gehalt = mitarbeiter_eintrag[2]
    output = (f"Mitarbeiter: {mitarbeiter_name} / gearbeitet: {stunden}h / gehalt: {gehalt}€ / auszahlung diese Woche: {momentaner_lohn}€")

    if mitarbeiter_eintrag[1] < 40:
        print(output, "arbeitzeit eingehalten")
    else:
        print(output, "arbeitzeit nich eingehalten")
