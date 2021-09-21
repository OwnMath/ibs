class Animal:
    def voice(self):
        pass


class Cow(Animal):
    def voice(self):
        print('Moo-oo-o')


class Chicken(Animal):
    def voice(self):
        print('Pip-pip!')


class Cat(Animal):
    def voice(self):
        print('Meow')


Marta = Cow()
Berta = Chicken()
Snow = Cat()

Marta.voice()
Berta.voice()
Snow.voice()
