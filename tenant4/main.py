from flask import Flask, json, Response, request,render_template, url_for, redirect
import save_and_parse as sap

app = Flask(__name__)
app.config["APP_HOST"] = "0.0.0.0"
app.config["APP_PORT"] = 5000
app.config["PARSER"] = "./parser/umlgraph"
app.config["SAVE_FOLDER"] = "./textcodes/"
app.config["OUTPUT_FOLDER"] = "./static/"


@app.route('/textUpload', methods=['POST'])
def upload_text():
    body = request.json["textCode"]
    sap.process(app.config["PARSER"],
                app.config["SAVE_FOLDER"],
                body,app.config["OUTPUT_FOLDER"])

    res_json = {}
    res_json["link"] = url_for("static", filename="output.png")

    return Response(response=json.dumps(res_json), status=200)

@app.route("/tenant4",methods=['GET'])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host=app.config["APP_HOST"], port=app.config["APP_PORT"])
