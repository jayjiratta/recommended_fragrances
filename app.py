from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("home.html")

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/brands')
def brands():
    return render_template('brands.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/idoluse')
def idoluse():
    return render_template('idoluse.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/perfumes')
def perfumes():
    return render_template('perfumes.html')

@app.route('/register')
def regiter():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True)