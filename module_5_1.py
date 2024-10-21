class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        if floor > self.number_of_floors or floor < 1:
            return print('Такого этажа не существует')
        else:
            for stage in range(1, floor + 1):
                print(stage)


house_1 = House('Высокий дом', 35)
house_2 = House('Низкий дом', 5)
house_1.go_to(9)
house_2.go_to(0)
