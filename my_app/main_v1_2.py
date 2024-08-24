from typing import List


def process_data(data: str) ->str:
    return data
def concatenate_strings(strings: List[str]) -> str:
    return ''.join(strings)
def display_message(message: str) -> str:
    return message
def main() -> str:
    data = process_data("example")
    print(data)
    strings = ["hello", "world"]
    concatenated = concatenate_strings(strings)
    x = display_message(concatenated)
    return x

if __name__ == "__main__":
    main()