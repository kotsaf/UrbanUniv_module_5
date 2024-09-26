class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'Такого этажа не существует')
            return
        for i in range(1, new_floor):
            i += 1
            print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to(0)


# 2
# 3
# 4
# 5
# Такого этажа не существует
# Такого этажа не существует