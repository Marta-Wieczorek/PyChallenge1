name = input("Write your name: ")

age = int(input("How old are you? "))

if (17 < age < 31):
    print("Welcome on Your holiday, {0}".format(name))
else:
    print("We are sorry, {0}, but AYou can't enter".format(name))