import os
from flask import Flask, json, Response, request,render_template, url_for, redirect

app = Flask(__name__)
app.config["APP_HOST"] = "0.0.0.0"
app.config["APP_PORT"] = 5000
# app.config["CLASS_JAR"] = "./parser/parser.jar"
# app.config["UPLOAD_FOLDER"] = "./uploads/"
# app.config["UNZIP_FOLDER"] = "./unzips/"
# app.config["OUTPUT_FOLDER"] = "./static/"


@app.route("/",methods=['GET'])
def index():
    return render_template("login.html")

@app.route("/",methods=['POST'])
def post_login():
    user_name = request.json["userName"]
    user_password = request.json["userPassword"]

    if user_name == "admin" and user_password == "admin":
        return Response(json.dumps({"redirect":url_for("dashboard")}), status=200)
    else:
        return Response(json.dumps({"error":"authentication fails"}), status=403)

@app.route("/dashboard",methods=['GET'])
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
