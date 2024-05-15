class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

# Пример использования базового класса
# animal = Animal("Generic Animal", 5)  # Будет ошибка, так как метод make_sound не реализован
# animal.make_sound()


### 2. Реализация наследования:


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} chirps.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} roars.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} hisses.")

# Примеры использования подклассов
bird = Bird("Parrot", 2, "Medium")
mammal = Mammal("Lion", 5, "Golden")
reptile = Reptile("Snake", 3, "Smooth")

bird.make_sound()
mammal.make_sound()
reptile.make_sound()


### 3. Демонстрация полиморфизма:


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования функции полиморфизма
animals = [bird, mammal, reptile]
animal_sound(animals)


### 4. Создание класса Zoo, использующего композицию:


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Added {staff_member.name} to the zoo staff.")

# Пример использования класса Zoo
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)


### 5. Создание классов для сотрудников:


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")

# Примеры использования классов для сотрудников
zookeeper = ZooKeeper("John")
veterinarian = Veterinarian("Emily")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

zookeeper.feed_animal(bird)
veterinarian.heal_animal(mammal)