#A simple Flask app container
FROM kovarn/python-java
MAINTAINER khoale88 "lenguyenkhoa1988@gmail.com"


#Install dependencies
RUN apt-get update
RUN apt-get install graphviz plotutils imagemagick -y
RUN pip install flask flask-sqlalchemy pymysql
