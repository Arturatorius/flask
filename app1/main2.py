from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/login2", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings2.html", vardas=vardas)
    else:
        return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True)