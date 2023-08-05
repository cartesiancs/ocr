from typing import Union
from fastapi import FastAPI
from PIL import Image
import pytesseract

app = FastAPI()


@app.get("/rcg/{item_id}")
def read_root(item_id: str):
    print(pytesseract.get_languages(config=''))

    g = pytesseract.image_to_string(Image.open(item_id), lang='kor+eng')
    print(g)

    return {"data": g}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}