from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/',methods=['GET', 'POST']) # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		form_username = request.form['username']
		form_password = request.form['password']

		if form_username == username+form_password == password:

			return render_template('home.html')

		else:

			return render_template('login.html')





@app.route('/home')  # '/' for the default page
def home():
  return render_template('home.html',fl=facebook_friends)


@app.route('/friend_exists/<string:friend>',methods=['GET','POST'])
def friend_exists(friend):
	if(friend in facebook_friends):
		return
		render_template('friend_exists.html',friend=friend,b="they are!")
	else:
		return
		render_template('friend_exists.html',friend=friend,b="they are not")
























if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)



