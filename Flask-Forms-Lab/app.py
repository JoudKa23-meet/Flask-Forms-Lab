from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "Joud"
password = "123456"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		name = request.form['username']
		password1 = request.form['password']
		if name==username and password==password1:
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friend_exists(name):
	exist=False
	if name=="Loai" or name=="Yonathan" or name=="Adan" or name=="George" or name=="Fouad" or name=="Celina":
		exist=True
	return render_template('friend_exists.html', name=name, facebook_friends=facebook_friends, exist=exist)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)