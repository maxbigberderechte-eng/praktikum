
nummer_liste = range(1, 15)

list

for nummer in nummer_liste:
    mod_3 = nummer % 3
    print("num:",mod_3)
    var_1 = bool(mod_3)
    var_2 = mod_3 == 0
    print(var_1,var_2)

    if nummer % 3 == 0 and nummer % 5 == 0:
        print("Fizz Buzz")
    elif nummer % 3 :
        print("Fizz")
    elif nummer % 5 == 0:
        print("Buzz")
    else:
        print(nummer)





print(bool(30 % 18))