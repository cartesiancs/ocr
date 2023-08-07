FROM python 
WORKDIR /usr/src/app 
COPY . . 
RUN apt update
RUN apt-get -y install libgl1-mesa-glx
RUN apt-get install libglib2.0-0
RUN apt install -y tesseract-ocr
RUN apt-get install tesseract-ocr-kor
RUN apt install -y libtesseract-dev
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10083"]
EXPOSE 10083