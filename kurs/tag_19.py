
user_noten = input("Bitte gib deine noten mit (,) ein:")
noten_str = user_noten.split(",")
noten_int = []

for note in noten_str:

    try:
        noten_int.append(int(note))
    except ValueError:
        print(type(user_noten))

print(noten_int)