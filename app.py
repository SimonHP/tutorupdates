from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

#configure flak-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Your SMTP server
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'simonhpalmer@gmail.com'
app.config['MAIL_PASSWORD'] = 'hgjq xfse ssht palh'
app.config['MAIL_DEFAULT_SENDER'] = 'simonhpalmer@gmail.com'

mail = Mail(app)

# Blog Page (Old index.html)
@app.route('/')
def blog():
    return render_template('index.html') 



# About Page
@app.route('/about')
def about():
    return render_template('about.html')




# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # compose email
        msg = Message('New Contact Form Submission',
                      recipients=['hastingssp1234@gmail.com','simon.palmer10@nhs.net'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        # Redirect to a thank-you page or back to the contact form
        return redirect(url_for('thank_you'))

    return render_template('contact.html')

# Thank You Page (after form submission)
@app.route('/thank-you')
def thank_you():
    return "Thank you for contacting us!"

if __name__ == '__main__':
    app.run(debug=True)
