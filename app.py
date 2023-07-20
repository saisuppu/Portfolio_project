from flask import Flask,url_for,render_template
app = Flask(__name__)


@app.route('/')
def home():
    x = 12
    return render_template("home.html", x=x)


@app.route('/about')
def link():
    return render_template("link.html")


if __name__ == "__main__":
    app.run(debug=True)
