from flask import Flask, render_template, request
import requests
import smtplib
from password import EMAIL, PASSWORD

posts = requests.get("https://api.npoint.io/7437a304f2ccfab65014").json()
USER_EMAIL = EMAIL
USER_PASSWORD = PASSWORD

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
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", title=header_title, msg_sent=True)
    return render_template("contact.html", title=header_title, msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Name {name} \nEmail {email} \nPhone number {phone} \nmessage {message}"
    message = 'Subject: {}\n{}'.format("Some One Wants to Contact You", email_message)

    print(email_message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USER_EMAIL, USER_PASSWORD)
        connection.sendmail(to_addrs='matty.matt.matt@hotmail.com', msg=message, from_addr=USER_EMAIL)


if __name__ == "__main__":
    app.run(debug=True)