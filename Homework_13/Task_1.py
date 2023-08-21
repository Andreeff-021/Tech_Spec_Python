from Homework_13.my_exeptions import NegativeSideValue


class Rectangle:
    def __init__(self, side_a: int, side_b: int = None):
        self.side_a = side_a
        self.side_b = side_b
        if side_b is None:
            self.side_b = side_a

    def get_perim(self):
        return (self.side_a + self.side_b) * 2

    def get_square(self):
        return self.side_a * self.side_b


class RectanglePro(Rectangle):
    def __add__(self, other):
        sum_of_perims = self.get_perim() + other.get_perim()
        side_a = self.side_a + other.side_a
        side_b = sum_of_perims / 2 - side_a
        return Rectangle(side_a, side_b)

    def __sub__(self, other):
        if self.get_perim() < other.get_perim():
            self, other = other, self
        diff = self.get_perim() - other.get_perim()
        side_a = self.side_a - other.side_a
        side_b = diff / 2 - side_a
        if side_a < 0 or side_b < 0:
            raise NegativeSideValue(side_a, side_b)
        return RectanglePro(side_a, side_b)


if __name__ == '__main__':
    rect_1 = RectanglePro(12, 3)
    rect_2 = RectanglePro(5)

    rect_dif = rect_1 - rect_2
    print(rect_dif.side_a, rect_dif.side_b)