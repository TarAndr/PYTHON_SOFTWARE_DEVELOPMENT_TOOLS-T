class TransportVehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def calculate_max_speed(self):
        raise NotImplementedError("Метод должен быть переопределен в производном классе")

    def calculate_capacity(self):
        raise NotImplementedError("Метод должен быть переопределен в производном классе")


class Car(TransportVehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def calculate_max_speed(self):
        # Предположим, что для автомобиля максимальная скорость зависит от количества дверей
        return 200 + self.num_doors * 10

    def calculate_capacity(self):
        # Предположим, что вместимость автомобиля зависит от количества дверей
        return 4 + self.num_doors


class Airplane(TransportVehicle):
    def __init__(self, brand, model, wingspan):
        super().__init__(brand, model)
        self.wingspan = wingspan

    def calculate_max_speed(self):
        # Предположим, что для самолета максимальная скорость зависит от размаха крыльев
        return 800 + self.wingspan * 20

    def calculate_capacity(self):
        # Предположим, что вместимость самолета зависит от размаха крыльев
        return 100 + self.wingspan // 2


# Пример использования классов
car_instance = Car("Toyota", "Camry", 4)
print(f"Автомобиль {car_instance.brand} {car_instance.model}:")
print(f"Максимальная скорость: {car_instance.calculate_max_speed()} км/ч")
print(f"Вместимость: {car_instance.calculate_capacity()} человек\n")

airplane_instance = Airplane("Boeing", "747", 60)
print(f"Самолет {airplane_instance.brand} {airplane_instance.model}:")
print(f"Максимальная скорость: {airplane_instance.calculate_max_speed()} км/ч")
print(f"Вместимость: {airplane_instance.calculate_capacity()} человек")
