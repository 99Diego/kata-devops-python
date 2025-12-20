import argparse

from app.dictionary_kata import Dictionary
from app.shopping_kata import get_total
from app.words_kata import nth_char


def run_dictionary(word: str):
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    print(d.look(word))


def run_shopping(items: list[str]):
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    total = get_total(costs, items, 0.09)
    print(total)


def run_words(words: list[str]):
    print(nth_char(words))


def main():
    parser = argparse.ArgumentParser(description="Python DevOps Kata CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    dict_parser = subparsers.add_parser("dictionary")
    dict_parser.add_argument("word")

    shop_parser = subparsers.add_parser("shopping")
    shop_parser.add_argument("items", nargs="+")

    words_parser = subparsers.add_parser("words")
    words_parser.add_argument("words", nargs="+")

    args = parser.parse_args()

    if args.command == "dictionary":
        run_dictionary(args.word)
    elif args.command == "shopping":
        run_shopping(args.items)
    elif args.command == "words":
        run_words(args.words)


if __name__ == "__main__":
    main()
