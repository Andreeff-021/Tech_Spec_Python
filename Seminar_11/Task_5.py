# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

from Seminar_10.Task_2 import Rectangle


class RectanglePro(Rectangle):
    """
    Addition, subtraction of rectangle perimeters. Comparing rectangle areas
    """
    def __add__(self, other):
        """Adding perimeters"""
        sum_of_perims = self.get_perim() + other.get_perim()
        side_a = self.side_a + other.side_a
        side_b = sum_of_perims / 2 - side_a
        return Rectangle(side_a, side_b)

    def __sub__(self, other):
        """Subtracting perimeters"""
        if self.get_perim() < other.get_perim():
            self, other = other, self
        diff = self.get_perim() - other.get_perim()
        side_a = abs(self.side_a - other.side_a)
        side_b = diff / 2 - side_a
        return RectanglePro(side_a, side_b)

    def __eq__(self, other):
        """Comparison for equality"""
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """Comparison on inequality"""
        return self.get_square() > other.get_square()

    def __le__(self, other):
        """Comparison on inequality or inequality"""
        return self.get_square() <= other.get_square()


if __name__ == '__main__':
    rect_1 = RectanglePro(2, 3)
    rect_2 = RectanglePro(5)
    print(rect_1.get_perim())
    print(rect_2.get_perim())

    rect_sum = rect_1 + rect_2
    print(rect_sum.get_perim())
    print(rect_sum.side_a, rect_sum.side_b)
    rect_dif = rect_1 - rect_2
    print(rect_dif.get_perim())
    print(rect_dif.side_a, rect_dif.side_b)