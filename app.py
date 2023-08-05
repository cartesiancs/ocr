from typing import Union
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract
import uuid
import os

from fastapi.middleware.cors import CORSMiddleware


UPLOAD_DIR = "./images"
CORD_ORIGINS = ["*"]

app = FastAPI()
oem = 3
psm = 6


app.add_middleware(
    CORSMiddleware,
    allow_origins=CORD_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recognizetest/{item_id}")
def read_root(item_id: str):
    print(Image.open(item_id))

    g = pytesseract.image_to_string(Image.open(item_id), lang='kor+eng')
    print(g)

    return {"data": g}


@app.post("/recognize")
async def read_root(file: UploadFile):
    print(file.filename)
    
    content = await file.read()
    filename = f"{str(uuid.uuid4())}.jpg"


    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(content)

    print(pytesseract.get_languages(config=''))

    text = pytesseract.image_to_string(Image.open(os.path.join(UPLOAD_DIR, filename)), lang='kor+eng')

    return {"data": text}