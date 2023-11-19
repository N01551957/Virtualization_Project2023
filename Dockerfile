FROM python:3.8
WORKDIR /app
RUN apt-get update
RUN apt-get install default-libmysqlclient-dev
COPY . .
RUN pip install -r requirements.txt 
EXPOSE 5000
CMD [ "python","main.py"]
