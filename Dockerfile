FROM python:3.8-slim

ARG name=simple-restaurant-application

RUN mkdir name && cd name

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

WORKDIR /apps

CMD ["python3","./app.py"]