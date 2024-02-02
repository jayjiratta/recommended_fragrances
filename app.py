from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/Home')
def home():    
    return render_template("home.html")

@app.route('/Articles')
def articles():
    return render_template('article.html')

@app.route('/Brands')
def brands():
    return render_template('brand.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/FAQs')
def faq():
    return render_template('faq.html')

@app.route('/idoluse')
def idoluse():
    return render_template('idoluse.html')

@app.route('/LOGIN')
def login():
    return render_template('login.html')

@app.route('/Perfumes')
def perfumes():
    return render_template('perfume.html')

@app.route('/REGISTER')
def register():
    return render_template('register.html')

@app.route('/About')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True)