from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask (__name__)
app.secret_key = 'secrete key'


#MYSQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'maestro'
app.config['MYSQL_DB'] = 'User_sys'

mysql = MySQL(app)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.connect("SELECT username, password FROM user WHERE username = %s,"(username))
        user = cur.fetchone()
        cur.close()

        if user and password == user[1]:
            session['username'] = user[0]
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error= 'invalid username or password')
        
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, port=5050)
