def FarmCount():
    print("There are ", Animal.count, " animals")


class Animal:
    count = 0

    def voice(self):
        pass


class Cow(Animal):
    def __init__(self):
        Animal.count += 1

    def voice(self):
        print('Moo-oo-o')


class Chicken(Animal):
    def __init__(self):
        Animal.count += 1

    def voice(self):
        print('Pip-pip!')


class Cat(Animal):
    def __init__(self):
        Animal.count += 1

    def voice(self):
        print('Meow')


Marta = Cow()
Berta = Chicken(); Bart = Chicken()
Snow = Cat(); Yely = Cat();

Marta.voice()
Berta.voice()
Snow.voice()

FarmCount()