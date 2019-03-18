from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('login.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('Page2.html')
    else:
        flash('wrong password!')
        return home()

#@app.route('/Page2')
#def Page2():
    #return render_template('Page2.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='127.0.0.2', port='8080', debug=True)
