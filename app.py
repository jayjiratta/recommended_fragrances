from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/article')
def article():
    return render_template("article.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/idoluse')
def idoluse():
    return render_template("idoluse.html")

@app.route('/brand')
def brand():
    return render_template("brand.html")

@app.route('/perfume')
def perfume():
    return render_template("perfume.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
