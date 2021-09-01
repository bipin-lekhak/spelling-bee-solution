from pathlib import Path

from src.words import Words


def get_inputs_dummy(path=None):
    path = path or Path() / "dummy_input" / "dummy_input.txt"
    path = Path(path)

    file_io = path.read_text()
    grid, compulsory_char = file_io.split()
    grid = set(grid)

    validate_input(grid, compulsory_char)

    return grid, compulsory_char


def get_data(path=None):
    path = path or Path() / "data" / "english_words_filtered.txt"
    path = Path(path)

    file_io = path.read_text()
    all_words = file_io.split()
    return sorted(set(all_words))


def validate_input(grid, compulsory_char):
    assert len(grid) == 6
    assert len(compulsory_char) == 1
    assert all(len(x) == 1 for x in grid)


def save_output(word_list, grid=None, char=None, path=None):
    path = (
        path
        or Path() / "outputs" / f"outputs_{''.join(sorted(grid))}{char}.txt"
    )
    path = Path(path)

    path.write_text(
        "\n".join(x.string + "," + str(x.score) for x in word_list)
    )


def main():
    grid, char = get_inputs_dummy()
    all_words_read = get_data()
    all_words = {Words(x) for x in all_words_read}
    all_words = {x for x in all_words if x.unique_len <= 7}
    solution_words = {x for x in all_words if x.is_solution(grid, char)}
    solution_sorted = sorted(
        solution_words, key=lambda x: x.score, reverse=True
    )
    save_output(solution_sorted, grid, char)


if __name__ == "__main__":
    main()
