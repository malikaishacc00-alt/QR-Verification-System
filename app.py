from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def verification():
    return render_template("verify.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)