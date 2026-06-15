x = 1
y = 2
w = 4
list_of_numbers = [x, y, w]


def do():
    print("do")


# For-Each
for number_el in list_of_numbers:
    higher_num = number_el + 10
    print(number_el, higher_num, "x")



# for-Schleife
number = int(input("Number"))
for i in range(number):
    print(i + i)
    do()
    print("x")
print("y")


# While-Schleife
while input():
    do()


# Boolean/Cast, bzw "Truthiness"
nicht_leer = bool("hallo")
print(nicht_leer)
leer = bool("")
print(leer)
