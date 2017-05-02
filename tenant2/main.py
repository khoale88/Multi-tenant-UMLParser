import os
from flask import Flask, json, Response, request,render_template, url_for, redirect
import unzip_and_parse as uap

app = Flask(__name__)

app.config["APP_HOST"] = "0.0.0.0"
app.config["APP_PORT"] = 5000
app.config["CLASS_JAR"] = "./parser/parser.jar"
app.config["UPLOAD_FOLDER"] = "./uploads/"
app.config["OUTPUT_FOLDER"] = "./static/"


@app.route('/upload', methods=['POST'])
def upload_zip():
    zipfile = request.files['zipFile']
    filename = zipfile.filename

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    zipfile.save(save_path)

    outputlink = uap.process(jar_path=app.config["CLASS_JAR"],
                             save_path=app.config["UPLOAD_FOLDER"],
                             zip_name=filename,
                             output_path=app.config["OUTPUT_FOLDER"])

    body = {}
    body["link"] = url_for("static", filename="output.png")

    return Response(response=json.dumps(body), status=200)


@app.route("/",methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host=app.config["APP_HOST"], port=app.config["APP_PORT"])
