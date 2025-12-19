from app.dictionary_kata import Dictionary
from app.shopping_kata import get_total
from app.words_kata import nth_char


def main():
    # Dictionary kata
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    print(d.look("Apple"))
    print(d.look("Banana"))

    # Shopping kata
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    print(get_total(costs, ["socks", "shoes"], 0.09))

    # Words kata
    print(nth_char(["yoda", "best", "has"]))


if __name__ == "__main__":
    main()

