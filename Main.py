from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register/', methods = ["POST", "GET"])
def register():
    return render_template('doc.html')

@app.route('/prescribe/', methods = ["POST", "GET"])
def prescribe():
    return render_template('prescribe.html')


if __name__ == "__main__":
    app.run(debug=True)