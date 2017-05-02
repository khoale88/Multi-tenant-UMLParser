import os
from flask import Flask, json, Response, request,render_template, url_for, redirect

app = Flask(__name__)
app.config["APP_HOST"] = "localhost"
app.config["APP_PORT"] = 5000
# app.config["CLASS_JAR"] = "./parser/parser.jar"
# app.config["UPLOAD_FOLDER"] = "./uploads/"
# app.config["UNZIP_FOLDER"] = "./unzips/"
# app.config["OUTPUT_FOLDER"] = "./static/"


@app.route("/",methods=['GET'])
def index():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
