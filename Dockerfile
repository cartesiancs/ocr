FROM python 
WORKDIR /usr/src/app 
COPY . . 
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8082"]
EXPOSE 8082