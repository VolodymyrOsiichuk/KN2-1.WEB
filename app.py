from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

app = Flask(__name__)

# Налаштування бази даних SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'qweasd'

db = SQLAlchemy(app)

# Модель для таблиці users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return f"<User {self.username}>"

# Створення бази даних, якщо вона ще не існує
if not os.path.exists('myDataBase.db'):
    with app.app_context():
        db.create_all()
        print("Базу Данних успішно створено!")

# Маршрути
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
        if request.method == 'POST':
            user = User(
                username=request.form['username'], 
                email=request.form['email'],
                password=request.form['password'], 
                phone = request.form['phone'])

            db.session.add(user)
            db.session.commit()
            flash('Реєстрація успішна!')
        return render_template('signup_page.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin_page():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.password == request.form['password']:
            flash('Вхід успішно здійнено!')
            return redirect(url_for('index'))
        else:
            flash('Вхід не здійнено. Перевірте емейл та пароль!')
    return render_template('signin_page.html')

if __name__ == '__main__':
    app.run(debug=True)
