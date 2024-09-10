from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Home Page
@app.route('/')
def home():
    return render_template('home.html')
# Blog Page (Old index.html)
@app.route('/blog')
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
        
        # Here you could send the data to an email, save it in a database, etc.
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        # Redirect to a thank-you page or back to the contact form
        return redirect(url_for('thank_you'))

    return render_template('contact.html')

# Thank You Page (after form submission)
@app.route('/thank-you')
def thank_you():
    return "Thank you for contacting us!"

if __name__ == '__main__':
    app.run()
