from flask import Flask, render_template, send_file
import json
import qrcode
import io

app = Flask(__name__)


def load_documents():
    with open("documents.json") as file:
        return json.load(file)


@app.route("/")
def verification():
    documents = load_documents()
    document_id = "DOC-2026-0001"
    document = documents[document_id]

    return render_template(
        "verify.html",
        document=document,
        document_id=document_id
    )


@app.route("/verify/<document_id>")
def verify_document(document_id):
    documents = load_documents()

    if document_id not in documents:
        return render_template("invalid.html"), 404

    document = documents[document_id]

    return render_template(
        "verify.html",
        document=document,
        document_id=document_id
    )


@app.route("/qr/<document_id>")
def generate_qr(document_id):
    url = f"https://qr-verification-system-5er6.onrender.com/verify/{document_id}"

    qr = qrcode.make(url)

    img = io.BytesIO()
    qr.save(img, format="PNG")
    img.seek(0)

    return send_file(img, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
