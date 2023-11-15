from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/7437a304f2ccfab65014").json()

app = Flask(__name__)


@app.route('/')
def home():
    header_title = "Home"
    return render_template("index.html", title=header_title, all_posts=posts)

@app.route('/about')
def about():
    header_title = "About"
    return render_template("about.html", title=header_title)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    post=None
    for blog in posts:
        if blog["id"] == blog_id:
            post = blog
    header_title = "Post"
    return render_template("post.html", title=header_title, post=post)

@app.route('/contact')
def contact():
    header_title = "Contact"
    return render_template("contact.html", title=header_title)

if __name__ == "__main__":
    app.run(debug=True)