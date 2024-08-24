FROM python:3.8-slim-buster

WORKDIR /app
# WORKDIR /python-docker

RUN pip3 install --upgrade pip
RUN pip3 install python-dotenv
RUN pip3 install flask_sqlalchemy
RUN pip3 install flask-bcrypt
RUN pip3 install psutil
COPY . .

CMD [ "python3", "run.py"]