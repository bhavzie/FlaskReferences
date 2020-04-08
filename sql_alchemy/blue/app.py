from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thissecret'
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

@app.route('/login')
def index():
        return render_template('login.html')

@app.route('/login1', methods=['GET', 'POST'])
def index1():
        username = request.form['username']
        user = User.query.filter_by(username=username).first()

        if not user :
                return '<h1> User not found </h1>'
        else:
                login_user(user)
                return '<h1> logged in </h1>'


@login_required
@app.route('/logout')
def logout():
        logout_user()
        return 'eklk'

@login_required
@app.route('/home')
def home():
        return current_user.username

if __name__ == "__main__":
        app.run(debug=True)