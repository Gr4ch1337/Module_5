class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def go_to(self, floor):
        if floor > self.number_of_floors or floor < 1:
            return print('Такого этажа не существует')
        else:
            for stage in range(1, floor + 1):
                print(stage)


house_1 = House('Высокий дом', 35)
house_2 = House('Низкий дом', 5)

print(house_1)
print(house_2)

print(house_1 == house_2)  # __eq__

house_1 = house_1 + 78  # __add__
print(house_1)
print(house_1 == house_2)

house_1 += 10  # __iadd__
print(house_1)

house_2 = 10 + house_2  # __radd__
print(house_2)

print(house_1 > house_2)  # __gt__
print(house_1 >= house_2)  # __ge__
print(house_1 < house_2)  # __lt__
print(house_1 <= house_2)  # __le__
print(house_1 != house_2)  # __ne__
