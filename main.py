class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "жре")

    def sleep(self):
        print(self.name, "спить")


class Mammals(Animal):
    def __init__(self, name, age, fur):
        super().__init__(name, age)
        self.fur = fur
        self.warm_blooded = True

    def run(self):
        print(self.name, "бігає")

    def give_birth(self):
        print(self.name, "ражаэ дитинчат")


class Cat(Mammals):
    def __init__(self, name, age, fur):
        super().__init__(name, age, fur)

    def meow(self):
        print(self.name, "нявкає")

    def climb(self):
        print(self.name, "лазить по дереву")


class Dog(Mammals):
    def __init__(self, name, age, fur):
        super().__init__(name, age, fur)

    def bark(self):
        print(self.name, "гавкае")

    def wag_tail(self):
        print(self.name, "махає хвостом")


class Fish(Animal):
    def __init__(self, name, age, water):
        super().__init__(name, age)
        self.water = water
        self.fins = True

    def swim(self):
        print(self.name, "плаває")

    def dive(self):
        print(self.name, "пірнає")


cat = Cat("Мурзик", 3, "сіре")
dog = Dog("Бобік", 5, "коротке")
fish = Fish("Немо", 2, "солона")

cat.eat()
cat.meow()

dog.run()
dog.bark()

fish.swim()
fish.dive()