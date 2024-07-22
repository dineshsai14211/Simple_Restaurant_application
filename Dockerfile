#Base image
FROM python:3.8-slim

#Created the name argument and assigned "simple-restaurant-application" value
ARG name=simple-restaurant-application

#It creates the directory with name=simple-restaurant-application && change the directory to "simple-restaurant-application"
RUN mkdir name && cd name

#Copy all content into the present directory
COPY . .

#installing packages
RUN pip install -r requirements.txt

#Exposing the port
EXPOSE 5000

#Present directory
WORKDIR /apps

#Running the application
CMD ["python3","./app.py"]
