from pathlib import Path

from scripts.filter_words import filter_words


def get_words(path=None):
    path = path or Path() / "data" / "english_words.txt"
    path = Path(path)
    file_io = path.read_text()
    return sorted(set(file_io.split()))


def save_words(words, path=None):
    path = path or Path() / "data" / "english_words_filtered.txt"
    path = Path(path)
    path.write_text("\n".join(sorted(words)))
    return


def main():
    words = get_words()
    filtered_words = filter_words(words, short_threshold=4, total_threshold=7)
    save_words(filtered_words)


if __name__ == "__main__":
    main()
