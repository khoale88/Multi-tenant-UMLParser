#A simple Flask app container
FROM khoale88/281-personal
MAINTAINER khoale88 "lenguyenkhoa1988@gmail.com"

#Place app in container
COPY . /app
WORKDIR /app

#ENV JAVA_HOME /usr/lib/jvm/jdk1.8.0_111
ENV UMLGRAPH_HOME /app/lib

CMD python main.py