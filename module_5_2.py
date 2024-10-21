class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, floor):
        if floor > self.number_of_floors or floor < 1:
            return print('Такого этажа не существует')
        else:
            for stage in range(1, floor + 1):
                print(stage)


house_1 = House('Высокий дом', 35)
house_2 = House('Низкий дом', 5)

# __str__
print(house_1)
print(house_2)

# __len__
print(len(house_1))
print(len(house_2))
