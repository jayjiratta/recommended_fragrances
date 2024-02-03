from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'asdfghjkl'
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'
# login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     user = User.query.filter_by(username=username).first()

    #     if user and check_password_hash(user.password, password):
    #         login_user(user)
    #         return redirect(url_for('blog'))
    #     else:
    #         flash('Invalid username or password', 'error')  
    #         return redirect(url_for('login'))
    # flash_messages = list(get_flashed_messages())
    # return render_template('login.html', flashed_messages=flash_messages)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # if request.method == 'POST':
    #     name = request.form.get('username')
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     if not username:
    #         flash('Username is required', 'error')
    #         return redirect(url_for('register'))

    #     user_exists = User.query.filter_by(username=username).first()
    #     if user_exists:
    #         return 'Username already exists'

    #     hashed_password = generate_password_hash(password)
    #     new_user = User(username=username, name=name, password=hashed_password)
    #     db.session.add(new_user)
    #     db.session.commit()

    #     return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/')
def home():    
    return render_template("home.html")

@app.route('/article')
def articles():
    return render_template('article.html')

@app.route('/brand')
def brands():
    return render_template('brand.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faqs')
def faq():
    return render_template('faq.html')

@app.route('/idoluse')
def idoluse():
    return render_template('idoluse.html')

@app.route('/perfume')
def perfumes():
    return render_template('perfume.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)