import string


def film_katalog():

    Filmtitel= input("Filmtitel:")
    Regisseurs = input("Regisseurs:")
    Erscheinungsjahr = input("Erscheinungsjahr:")
    Budget = input("Budget:"  )

    #Budget = input("Budget:")


    filme = ["Filmtitel:", Filmtitel, "Regisseurs:", Regisseurs, "Erscheinungsjahr:", Erscheinungsjahr,"Budget:", Budget]

    filme.append("neuer_name")
    filme.insert(1,"test")


    print(filme)
    print(type(filme))
    print(f"{filme[1]} wort ({filme[5]})")
    del filme[1]


film_katalog()

#[] {}