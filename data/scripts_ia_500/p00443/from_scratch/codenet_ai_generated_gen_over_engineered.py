from __future__ import annotations
from typing import Optional, Dict, List, Tuple, Union
from fractions import Fraction
import sys

class Weight:
    """
    Абстракция для веса, с поддержкой рациональных чисел для точного вычисления.
    """
    def __init__(self, value: Fraction):
        self.value = value

    @staticmethod
    def from_int(value: int) -> Weight:
        return Weight(Fraction(value))

    def __mul__(self, other: Fraction) -> Weight:
        return Weight(self.value * other)

    def __truediv__(self, other: Fraction) -> Weight:
        return Weight(self.value / other)

    def __add__(self, other: Weight) -> Weight:
        return Weight(self.value + other.value)

    def __lt__(self, other: Weight) -> bool:
        return self.value < other.value

    def __le__(self, other: Weight) -> bool:
        return self.value <= other.value

    def __int__(self) -> int:
        # Возвращает округленное вверх целочисленное значение веса
        return int(self.value.numerator // self.value.denominator + (1 if self.value.numerator % self.value.denominator != 0 else 0))

    def __repr__(self) -> str:
        return f"Weight({float(self.value)})"

class Node:
    """
    Абстрактный класс для узла в структуре мобиля.
    """
    def weight(self) -> Weight:
        """
        Получить минимальный вес узла с учётом баланса.
        """
        raise NotImplementedError()

class WeightNode(Node):
    """
    Узел, представляющий груз.
    """
    def __init__(self):
        # Вес груза минимален 1.
        self._weight = Weight.from_int(1)

    def weight(self) -> Weight:
        return self._weight

    def __repr__(self) -> str:
        return f"WeightNode(weight={self._weight})"

class RodNode(Node):
    """
    Узел, представляющий палку.
    Поддерживает структуру с красным (r) и синим (b) концом,
    длины от точки подвеса до концов задаются дробью p:q.
    """
    def __init__(self, p: int, q: int):
        self.p = Fraction(p)
        self.q = Fraction(q)
        self.red: Optional[Node] = None
        self.blue: Optional[Node] = None

        # Кеш для веса, чтобы избежать повторных вычислений
        self._cached_weight: Optional[Weight] = None

    def weight(self) -> Weight:
        if self._cached_weight is not None:
            return self._cached_weight

        # Балансировка места
        # вес * расстояние справа = вес * расстояние слева

        if self.red is None or self.blue is None:
            raise RuntimeError("Rod with missing end nodes")

        w_red = self.red.weight()
        w_blue = self.blue.weight()

        # Используя уравнение баланса:
        # w_red * p = w_blue * q

        # Чтобы минимизировать вес палки:
        # ищем целочисленные веса грузов, удовлетворяющие уравнению.
        # Но так как веса могут быть агрегированные значения, используем масштабирование.

        # Для сбалансированной палки вес = w_red + w_blue
        # Подгоняем веса по минимальному общему знаменателю:

        # Домножаем веса и длины, соответствующим образом.

        # Пусть X - общий множитель

        # Вес грузов уже минимальны, результаты с ро́дами
        # Предполагаем, что w_red и w_blue уже минимальны и сбалансированы.

        # Балансируем веса:
        # w_red * p = w_blue * q =>
        # w_red / q = w_blue / p

        # Чтобы найти общий вес:
        # weight = w_red + w_blue
        # Но нужно привести к общему масштабу, домножая веса на длины и затем уменьшить к целому.

        # Для корректной минимизации необходимо масштабировать веса с учётом п и q

        # Способ: привести веса к уравнению балансировки с использованием НОК

        # Реализуем упрощение с рациональными числами:

        # число = w_red * p
        # число должно равняться w_blue * q
        # чтобы минимизировать сумму w_red + w_blue, надо найти пропорциональные множители

        # Наибольший общий делитель для балансирования:
        gcd_val = (w_red.value * self.p).denominator * (w_blue.value * self.q).denominator

        # Используем дроби напрямую:
        lhs = w_red.value * self.p
        rhs = w_blue.value * self.q
        lcm_denominator = (lhs.denominator * rhs.denominator) // Fraction(lhs.denominator).denominator

        # Определим множители чтобы привести равенство к общему виду:
        # Но учитывая целочисленность весов (выходное значение) и то что минимизация веса это сложная задача,
        # а задача из IOI предполагает, что можно минимизировать с помощью масштабирования:

        # Вес палки - объединение масштабированных весов с учетом p и q:

        # Используем следующий подход:
        # вес палки = w_red * q + w_blue * p (стандартизируем веса к общем масштабе)

        # Для вычисления минимального веса палки используем лемму:

        weight_value = w_red.value * self.q + w_blue.value * self.p

        # создаём объект веса:
        self._cached_weight = Weight(weight_value)

        return self._cached_weight

    def set_red(self, node: Node):
        self.red = node
        self._cached_weight = None

    def set_blue(self, node: Node):
        self.blue = node
        self._cached_weight = None

    def __repr__(self) -> str:
        return f"RodNode(p={self.p}, q={self.q}, red={self.red}, blue={self.blue})"

class MobileFactory:
    """
    Фабрика для построения мобиля из входных данных.
    """
    def __init__(self):
        self.rods: Dict[int, RodNode] = {}
        self.weights: Dict[int, WeightNode] = {}
        self.n_rods = 0

    def build(self, n: int, data: List[Tuple[int, int, int, int]]) -> RodNode:
        self.n_rods = n
        self.rods.clear()
        self.weights.clear()

        # Создаём объекты палок
        for i in range(1, n + 1):
            p, q, r, b = data[i - 1]
            rod = RodNode(p, q)
            self.rods[i] = rod

        # Рекурсивное построение головы мобиль
        # Чтобы найти корневой элемент - палку, которая не висит на другом
        # Принимаем, что существует ровно одна палка, которая висит на несоединённой верёвке.

        # Построим зависимости
        hanging = [False] * (n + 1)
        for i in range(1, n + 1):
            p, q, r, b = data[i - 1]
            if r != 0:
                hanging[r] = True
            if b != 0:
                hanging[b] = True

        # Найти корень:
        root_rod_index = 0
        for i in range(1, n + 1):
            if not hanging[i]:
                root_rod_index = i
                break

        # Рекурсивное формирование дерева
        def build_node(i: int) -> Node:
            # i - номер палки
            p, q, r, b = data[i - 1]

            rod = self.rods[i]

            # Строим красный конец
            if r == 0:
                rod.set_red(WeightNode())
            else:
                rod.set_red(build_node(r))

            # Строим синий конец
            if b == 0:
                rod.set_blue(WeightNode())
            else:
                rod.set_blue(build_node(b))

            return rod

        root = build_node(root_rod_index)
        return root

def solve_dataset(n: int, data: List[Tuple[int, int, int, int]]) -> int:
    factory = MobileFactory()
    root = factory.build(n, data)
    w = root.weight()
    # Округляем вес вверх согласно условию целочисленного веса
    result = int(w)
    return result

def main():
    input_data = sys.stdin.read().strip().split()
    index = 0
    while True:
        if index >= len(input_data):
            break
        n = int(input_data[index])
        index += 1
        if n == 0:
            break
        data = []
        for _ in range(n):
            p = int(input_data[index]); index += 1
            q = int(input_data[index]); index += 1
            r = int(input_data[index]); index += 1
            b = int(input_data[index]); index += 1
            data.append((p, q, r, b))
        result = solve_dataset(n, data)
        print(result)

if __name__ == "__main__":
    main()