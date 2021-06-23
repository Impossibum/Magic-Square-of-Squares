from magic_square import MagicSquare
from itertools import permutations


def square_list(generated_list: list) -> list:
    return [x * x for x in generated_list]


def generate_and_evaluate(size: int) -> MagicSquare:
    max_int = size * size
    max_squared = max_int * max_int
    square_count = 0
    while True:
        contents = square_list(list(range(1, max_int + 1)))
        mutations = permutations(contents, size * size)
        for _contents in mutations:
            if max_squared in _contents:
                square_count += 1
                square = MagicSquare(contents)
                if square.solved():
                    return square

        print(
            f"squares {contents} tested so far resulting in {square_count} magic squares generated."
        )
        max_int += 1
        max_squared = max_int * max_int


if __name__ == "__main__":
    print("Exercise in futility initiated!")
    square_of_squares = generate_and_evaluate(3)
    print(f"Squared magic square found! {square_of_squares}")
