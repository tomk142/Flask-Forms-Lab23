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


username = "llo2ay"
password = "123"

accounts = {"llo2ay":"123", "tom":"77"}
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user = request.form['username']
		passw= request.form['password']

		for i in accounts:

			if(user == i and passw == accounts[i]):
				return redirect(url_for('home'))

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



