FROM python:3-slim

COPY . .

WORKDIR ./apps

RUN pip install -r requirements.txt

CMD ["python","app.py"]
