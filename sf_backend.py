from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

admin_email = 'skillfactory@example.com'
admin_password = 'admin123'
users_list = []
auth_status = False

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
    if request.method == 'GET':
        return render_template('log_in.html')
    else:
        user_login = request.form["login"]
        user_pass = request.form["password"]

        for user in users_list:
            if user.login == user_login and user.password == user_pass:
                auth_status = True
            else:
                auth_status = False
        return render_template('cars.html', auth_status_for_page=auth_status)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/cars')
def cars():
    return render_template('cars.html')

@app.route('/contacts')
def contacts():
	return render_template('contacts.html')

@app.route("/greeting")
def greeting():
    return "<h1>Привет, " + admin_email + "! </h1>"

@app.route('/in_stock')
def in_stock():
	return render_template('in_stock.html')

@app.route('/sign_in', methods = ['POST', 'GET'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
        user_login = request.form['login']
        user_pass = request.form['password']
        new_user = User(login=user_login, password=user_pass)
        users_list.append(new_user)
        return render_template('index.html')

app.run(debug=True)

