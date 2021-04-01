FROM python:3.6-alpine

EXPOSE 1986

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . .

CMD [ "python", "main.py"]
