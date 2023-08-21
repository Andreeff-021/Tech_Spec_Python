class NegativeSideValue(Exception):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        if self.side_a < 0:
            result = f'Нельзя создать прямоугольник, т.к сторона "А" равна {self.side_a}'
        else:
            result = f'Нельзя создать прямоугольник, т.к сторона "B" равна {self.side_b}'
        return result
