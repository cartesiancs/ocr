from typing import Union
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract
import uuid
import os
import matplotlib.pyplot as plt
import imutils
from imutils.perspective import four_point_transform
from imutils.contours import sort_contours
import cv2
import re
import requests
import numpy as np

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


    savedFilename = os.path.join(UPLOAD_DIR, filename)
    receipt = cv2.imread(savedFilename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(receipt, cv2.COLOR_BGR2GRAY)    
    rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 20))
    
    gray = cv2.GaussianBlur(gray, (11, 11), 0)
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
    
    text = pytesseract.image_to_string(blackhat, lang='kor+eng')

    return {"data": text}