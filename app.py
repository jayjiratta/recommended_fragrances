from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("home.html")

@app.route('/articles')
def about():
    return render_template('articles.html')

@app.route('/brands')
def about():
    return render_template('brands.html')

@app.route('/contact')
def about():
    return render_template('contact.html')

@app.route('/faq')
def about():
    return render_template('faq.html')

@app.route('/idoluse')
def about():
    return render_template('idoluse.html')

@app.route('/login')
def about():
    return render_template('login.html')

@app.route('/perfumes')
def about():
    return render_template('perfumes.html')

@app.route('/regiter')
def about():
    return render_template('regiter.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True)