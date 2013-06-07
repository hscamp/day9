# imports
from flask import Flask, render_template, request
from flask_mail import Mail, Message
 
# run the app
app = Flask(__name__)

# config vars 
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME='sibrampup@gmail.com',
	MAIL_PASSWORD='SIBpassword'
)

# instantiate mail object
mail = Mail(app)

# route for domain
@app.route("/", methods=['GET', 'POST'])
# route function (get)
def hello():
	return render_template('index.html')

# route for menu
@app.route("/menu/", methods=['GET', 'POST'])
def menu():
	return render_template('menu.html')

# route for contact us
@app.route("/contact/", methods=['GET', 'POST'])
def contact():
	print "here I am"
	if request.method == 'POST':
		name = request.form['inputName']
		email = request.form['inputEmail']
		message = request.form['inputMessage']
		if name and email and message:
			msg = Message(
				'Someone sent me an email from my personal site!',
				sender = email,
				recipients= ['sibrampup@gmail.com'])
			msg.body = "Name: "+ name + "\n" + "Email: " + email + "\n\n" + message
			mail.send(msg)
		return render_template('contact.html')	
	else:
		return render_template('contact.html')

# route for 404
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# main (runs python file)
if __name__ == "__main__":
    app.run()

