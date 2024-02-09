from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Card
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '0293ff43f19034'
app.config['MAIL_PASSWORD'] = 'f2d89bdf1413e8'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Card
from flask_login import LoginManager, login_user, login_required, logout_user, current_user



app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.init_app(app)

db.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('blog')) #direct after login
        else:
            flash('Invalid username or password', 'error')  
            return redirect(url_for('login'))
    flash_messages = list(get_flashed_messages())
    return render_template('login.html', flashed_messages=flash_messages)

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

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('blog')) #direct after login
        else:
            flash('Invalid username or password', 'error')  
            return redirect(url_for('login'))
    flash_messages = list(get_flashed_messages())
    return render_template('login.html', flashed_messages=flash_messages)

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

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
