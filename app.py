from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def verification():
    with open("documents.json") as file:
        documents = json.load(file)

    document = documents["DOC-2026-0001"]

    return render_template(
        "verify.html",
        document=document
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
