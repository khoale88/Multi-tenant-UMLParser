#A simple Flask app container
FROM khoale88/281-personal
MAINTAINER khoale88 "lenguyenkhoa1988@gmail.com"

#Place app in container
COPY . /app
WORKDIR /app

RUN pip install mysql-connector-python-rf

CMD python main.py