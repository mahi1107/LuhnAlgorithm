from flask import Flask, render_template, request
from luhn import luhn_check

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        number = request.form.get("number", "").strip()
        if not number.isdigit():
            result = "❌ Please enter only digits"
        else:
            result = "✅ Valid Number" if luhn_check(number) else "❌ Invalid Number"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
