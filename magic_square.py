from math import sqrt


class MagicSquare:
    def __init__(self, _contents: list):
        self.contents = _contents
        self.size = int(sqrt(len(_contents)))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"A magic square of size {self.size} containing {self.contents}."

    def solved(self) -> bool:
        line_value = sum(self.contents[: self.size])
        return self.check_horizontals(line_value) \
            and self.check_verticals(line_value) \
            and self.check_diagonals(line_value)

    def check_horizontals(self, target: int) -> bool:
        for i in range(self.size):
            if sum(self.contents[i * self.size: i * self.size + self.size]) != target:
                return False

        return True

    def check_verticals(self, target: int) -> bool:
        for i in range(self.size):
            if sum(self.contents[i:: self.size]) != target:
                return False
        return True

    def check_diagonals(self, target: int) -> bool:
        return (
                sum([self.contents[(i * self.size) + i] for i in range(self.size)])
                == target
                and sum([self.contents[(i * self.size) + i] for i in range(self.size)])
                == target
        )


if __name__ == "__main__":
    example_contents = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9],
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16],
        [13, 3, 6, 12, 2, 16, 9, 7, 11, 5, 4, 14, 8, 10, 15, 1]
    ]
    for contents in example_contents:
        square = MagicSquare(contents)
        print(square)
        print(square.solved())
        print("--------------------")
