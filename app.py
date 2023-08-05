from typing import Union
from fastapi import FastAPI
from PIL import Image
import pytesseract

app = FastAPI()
oem = 3
psm = 6


@app.get("/recognizetest/{item_id}")
def read_root(item_id: str):
    print(pytesseract.get_languages(config=''))

    g = pytesseract.image_to_string(Image.open(item_id), lang='kor+eng')
    print(g)

    return {"data": g}


@app.get("/recognize/{item_id}")
def read_root(item_id: str):
    print(pytesseract.get_languages(config=''))

    g = pytesseract.image_to_string(Image.open(item_id), lang='kor+eng')
    print(g)

    return {"data": g}