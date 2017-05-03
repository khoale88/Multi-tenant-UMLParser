import os
from flask import Flask, json, Response, request,render_template, url_for, redirect
import unzip_and_parse as uap
import model

app = Flask(__name__)
app.config["APP_HOST"] = "0.0.0.0"
app.config["APP_PORT"] = 5005
app.config["CLASS_JAR"] = "./parser/parser.jar"
app.config["UPLOAD_FOLDER"] = "./uploads/"
app.config["OUTPUT_FOLDER"] = "./static/"
app.config["DB_USER"] = "admin"
app.config["DB_PASSWORD"] = "cmpe281#2017"
app.config["DB_HOST"] = "cmpe281.cotowvf3a27g.us-west-2.rds.amazonaws.com"
app.config["DB_PORT"] = 3306
app.config["DB_DATABASE"] = "cmpe281"
app.config["TENANT_ID"] = "Tenant4"

@app.route('/upload', methods=['POST'])
def upload_zip():
    zipfile = request.files['zipFile']
    filename = zipfile.filename

    #filename = "output.zip"
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    zipfile.save(save_path)

    outputlink = uap.process(jar_path=app.config["CLASS_JAR"],
                             save_path=app.config["UPLOAD_FOLDER"],
                             zip_name=filename,
                             output_path=app.config["OUTPUT_FOLDER"])

    body = {}
    body["link"] = url_for("static", filename="output.png")

    return Response(response=json.dumps(body), status=200)

@app.route("/tenant_data",methods=['POST'])
def tenant_update():
    tenant_data = request.json["tenant_data"]
    model.update_tenant_data(app.config, tenant_data)
    return Response(status=200)

@app.route("/tenant_data",methods=['GET'])
def tenant_read():
    tenant_data = model.get_tenant_data(app.config)
    return Response(json.dumps({"tenant_data":tenant_data}), status=200)


@app.route("/tenant1",methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host=app.config["APP_HOST"], port=app.config["APP_PORT"])
