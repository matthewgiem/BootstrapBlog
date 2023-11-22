from flask import Flask, render_template, request
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

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    header_title = "Post"
    return render_template("post.html", title=header_title, post=requested_post)

@app.route('/contact', methods=["POST", "GET"])
def contact():
    header_title = "Contact"
    if request.method == "POST":
        data = request.form
        print(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", title=header_title, msg_sent=True)
    return render_template("contact.html", title=header_title, msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)