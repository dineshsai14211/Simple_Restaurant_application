FROM python:3-slim

RUN mkdir Restaurant

WORKDIR /Restaurant

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/Restaurant"

CMD [ "python", "./apps/app.py" ]



