def get_text_words_number(text: str) -> int:
    return len(text.split())

# "Esto es una frase que voy a splitear por letras"
def chars_count(text: str) -> dict[str, int]:
    data: dict[str, int] = {}
    char_list = list(text.lower())

    for char in char_list:
        if char in data.keys():
            data[char] = data[char] + 1
        else:
            data[char] = 1


    return data

def get_sort_key(dict):
    return dict["num"]

def get_sorted_data(data: dict[str, int]) -> list[dict[str, str | int]]:
    unprocessed_data: list[dict[str, str | int]] = []

    for key in data:
        if key.isalpha():
            unprocessed_data.append({"char": key, "num": data[key]})

    unprocessed_data.sort(reverse=True, key=get_sort_key)

    processed_data = unprocessed_data

    return processed_data
