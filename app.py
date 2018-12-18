from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/blog")
def about():
    return render_template('blog.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)