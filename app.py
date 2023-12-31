from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return "this is a test route"


if __name__ == '__main__':
    app.run(debug=True)
    print("the app is running")