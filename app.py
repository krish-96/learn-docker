from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    return render_template('logout.html')


if __name__ == '__main__':
    # app.run()
    app.run(host='127.0.0.1', port='5555')
