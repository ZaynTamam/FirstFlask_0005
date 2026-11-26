from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        # Parsing parameter dari input bernama 'teks'
        data = request.form.get("teks")
        hasil = f"Input diterima: {data}"
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)