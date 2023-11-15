from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    header_title = "Home"
    return render_template("index.html", title=header_title)

@app.route('/about')
def about():
    header_title = "About"
    return render_template("about.html", title=header_title)

@app.route('/post')
def post():
    header_title = "Post"
    return render_template("post.html", title=header_title)

@app.route('/contact')
def contact():
    header_title = "Contact"
    return render_template("contact.html", title=header_title)

if __name__ == "__main__":
    app.run(debug=True)