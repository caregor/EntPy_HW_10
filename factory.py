"""
    ---Task 1---
Доработаем задачи 5-6. Создайте класс-фабрику.
    * Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    * Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""
from task6 import Bird, Fish, Mammal


class Factory:

    def create_animal(self,animal_type, **kwargs):
        if animal_type == "Bird":
            return Bird(**kwargs)
        elif animal_type == "Fish":
            return Fish(**kwargs)
        elif animal_type == "Mammal":
            return Mammal(**kwargs)
        else:
            raise ValueError("Invalid animal type")