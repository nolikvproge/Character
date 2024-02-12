class Character:
    def __init__(self, name, strength, dexterity, intelligence, speed):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.speed = speed

    def dodge(self):
        if self.dexterity + self.speed > 15:
            print(f"{self.name}  успешно увернулся!")
        else:
            print(f"{self.name}  не смог увернуться(.")

    def print_characteristics(self):
        print("Characteristics:")
        print(f"Name: {self.name}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Speed: {self.speed}")

# Создание объекта персонажа с именем
my_character = Character("Алукард", 10, 8, 12, 10)

# Вызов метода уклонения
my_character.dodge()

# Вывод характеристик персонажа
my_character.print_characteristics()
