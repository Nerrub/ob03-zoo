class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("Чирик")
    def eat(self):
        print("Ем червяков")

class Mammal(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)
    def make_sound(self):
        print("Мууу")
    def eat(self):
        print("Ем траву")

class Reptile(Animal):
    def __init__(self,name,age):
        super().__init__(name, age)
    def make_sound(self):
        print("Шшшш")
    def eat(self):
       print("Ем яйца птиц")

bird = Bird("Ворон","3")
mammal = Mammal("Корова","10")
reptile = Reptile("Гадюка","2")

bird.make_sound()
mammal.eat()
reptile.make_sound()
class Zoo:
    def __init__(self):
        self.animals = []
        self.employee = []

    def add_animal(self, Animal):
        self.animals.append(Animal)
        print(f"{Animal} добавлен в зоопарк")
    def add_employee(self,employee):
        self.employee.append(employee)
        print(f"{employee} добавлен в штат сотрудников")

zoo = Zoo()
zoo.add_animal(bird)

class Employee:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession
class Zookeeper(Employee):
    def __init__(self,name):
        super().__init__(name, "Смотритель зоопарка")
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal}")
class Veterinar(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal}")

zookeeper = Zookeeper("Даша")
veterinar = Veterinar("Дима")
zoo.add_employee(veterinar)
zoo.add_employee(zookeeper)
veterinar.heal_animal(bird)
