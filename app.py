
import db
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/action_page', methods=['GET', 'POST'])
def action_page():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    #db에 데이터 저장
    db.insert_data(name, email, phone, message)
    return f"당신이 입력한 {name} {email} {phone} {message}"

@app.route('/msg')
def msg():
    contact_list = db.select_data()
    return render_template("action_page.html", data=contact_list)

if __name__ == '__main__':
    app.run(host='210.110.167.56')


