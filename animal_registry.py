class Animal:
    def __init__(self, name, birth_date, commands=None):
        self.name = name
        self.birth_date = birth_date
        self.commands = commands if commands is not None else []

    def learn_command(self, command):
        """Добавить новую команду для животного."""
        self.commands.append(command)

    def get_commands(self):
        """Получить список команд, которые выполняет животное."""
        return self.commands


class Pet(Animal):
    """Класс для домашних животных."""
    pass


class PackAnimal(Animal):
    """Класс для вьючных животных."""
    pass


class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise ValueError("Resource is closed!")
        self.count += 1

    def close(self):
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        if exc_type is not None:
            raise


def main_menu():
    """Главное меню программы."""
    print("Добро пожаловать в реестр домашних животных!")
    print("1. Завести новое животное")
    print("2. Определить животное в правильный класс")
    print("3. Посмотреть список команд животного")
    print("4. Обучить животное новым командам")
    print("5. Выход")


def add_animal():
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения животного (гггг-мм-дд): ")
    animal_type = input("Введите тип животного (домашнее/вьючное): ")
    if animal_type.lower() == "домашнее":
        return Pet(name, birth_date)
    elif animal_type.lower() == "вьючное":
        return PackAnimal(name, birth_date)
    else:
        print("Неизвестный тип животного.")
        return None


def animal_counter_demo(animals):
    with Counter() as counter:
        for _ in animals:
            counter.add()
        print(f"Количество животных: {counter.count}")


def main():
    animals = []
    while True:
        main_menu()
        choice = input("Выберите опцию: ")
        if choice == "1":
            animal = add_animal()
            if animal:
                animals.append(animal)
                print(f"{animal.name} успешно добавлено.")
        elif choice == "2":
            name = input("Введите имя животного для определения: ")
            for animal in animals:
                if animal.name == name:
                    print(f"{name} является {type(animal).__name__}.")
                    break
            else:
                print("Животное не найдено.")
        elif choice == "3":
            name = input("Введите имя животного для просмотра команд: ")
            for animal in animals:
                if animal.name == name:
                    print(f"{name} может выполнять: {animal.get_commands()}")
                    break
            else:
                print("Животное не найдено.")
        elif choice == "4":
            name = input("Введите имя животного для обучения: ")
            command = input("Введите новую команду: ")
            for animal in animals:
                if animal.name == name:
                    animal.learn_command(command)
                    print(f"{name} теперь может выполнять: {animal.get_commands()}")
                    break
            else:
                print("Животное не найдено.")
        elif choice == "5":
            animal_counter_demo(animals)
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
