from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration (use your own email settings)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'simonhpalmer@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'hgjq xfse ssht palh'   # Your Gmail app password
app.config['MAIL_DEFAULT_SENDER'] = 'simonhpalmer@gmail.com'

# Initialize Flask-Mail
mail = Mail(app)

# List of subscriber emails
subscribers = [
    "hastingssp1234@gmail.com", "shpalmer@consultant.com", "V.Adjei-Darko1@uni.bsms.ac.uk","I.Close1@uni.bsms.ac.uk",
    "M.Heelam-Mcdonnell2@uni.bsms.ac.uk","L.Humphrys1@uni.bsms.ac.uk", "K.Anderson1@uni.bsms.ac.uk","I.Chamberlain@uni.bsms.ac.uk",
]

def send_notification():
    with app.app_context():
        subject = "New Update Available!"
        body = """
        Hello,

        I've just published a new update on the personal tutor updates website! Click the link below to read it:

        https://tutorupdates.onrender.com

        Please emal me to confirm seen. 

        Thank you

        Best regards,
        Simon Palmer
        """

        # Create the email message
        msg = Message(subject=subject, recipients=subscribers, body=body)

        # Send the email
        mail.send(msg)
        print("Notification emails sent successfully.")

if __name__ == "__main__":
    send_notification()
