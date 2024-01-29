from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():    
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('articles.html')

@app.route('/about')
def about():
    return render_template('brands.html')

@app.route('/about')
def about():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('faq.html')

@app.route('/about')
def about():
    return render_template('idoluse.html')

@app.route('/about')
def about():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('perfumes.html')

@app.route('/about')
def about():
    return render_template('regiter.html')

if __name__ =="__main__":
    app.run(debug=True)