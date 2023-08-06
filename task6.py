# ------------------------------------------- 5 -----------------------------
"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""

# ------------------------------------------- 6 -----------------------------
"""
Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс
Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        return 'Обычный'
