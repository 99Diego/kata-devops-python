from fastapi import FastAPI
from app.dictionary_kata import Dictionary
from app.shopping_kata import get_total
from app.words_kata import nth_char

app = FastAPI(title="DevOps Kata Service")


@app.get("/dictionary/{word}")
def dictionary(word: str):
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    return {"result": d.look(word)}


@app.post("/shopping")
def shopping(items: list[str]):
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    total = get_total(costs, items, 0.09)
    return {"total": total}


@app.post("/words")
def words(words: list[str]):
    return {"result": nth_char(words)}

