from stats import get_text_words_number, chars_count, get_sorted_data
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def print_processed_data(data: list[dict[str, str | int]]):
    for entry in data:
        print(f"{entry['char']}: {entry['num']}")

def print_report(file_path: str):
    book_text = get_book_text(file_path)
    data = chars_count(book_text)
    processed_data = get_sorted_data(data)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_text_words_number(book_text)} total words")
    print("--------- Character Count -------")
    print_processed_data(processed_data)
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])

main()
