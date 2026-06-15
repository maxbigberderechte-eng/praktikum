numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers.append(5)

print(numbers is new_numbers)
print(numbers == new_numbers)
print(numbers, new_numbers)

input_number = input("schreibe eine nummer:")

try:
    input_number = int(input_number)
    print(type(input_number))
    if int(input_number) == 0:
        print("Die Zahl ist: 0")
    elif int(input_number) < 0:
        print("Die Zahl ist: negativ")
    elif int(input_number) > 0:
        print("Die Zahl ist: positiv")
    # else:
    # print("{input_number}:ist keine Zahl")

except ValueError as e:
    # ...
    print("bitte Zahl eingeben")
    pass

h_w = int(input("Wie viele Stunden hast du diese Woche gearbeitet:"))
h_wage = int(input("Was ist dein Stundenlohn:"))

ergebnis = round(h_wage * 1.1 * (h_w - 40))

if h_w > 40:
    print(f"Dier steht {ergebnis} "
          f"Euro zu")
else:
    print(f"Dier stehen {h_wage}Euro zu")
