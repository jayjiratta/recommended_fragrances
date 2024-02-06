from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0293ff43f19034'
app.config['MAIL_PASSWORD'] = 'f2d89bdf1413e8'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


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
    return render_template('contact.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject=subject, sender=email, recipients=['support@scentspectrum.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    mail.send(msg)
    return render_template('send_email.html')

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
