# bigQuestions.py

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db_locale = 'users.db'


@app.route('/')
@app.route('/home')
def homepage():
	user_data=queryQuestions()
	print(user_data)
	return render_template('home.html', user_data=user_data)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/addQuestion',methods=['GET', 'POST'])
def addQuestion():
	if request.method=="GET":
		return render_template('addQuestion.html')
	else:
		user_details=(request.form['title'], request.form['details'], request.form['name'])
		insertquestion(user_details)
		return render_template('successfullyAdded.html')


def insertquestion(user_details):
	connie = sqlite3.connect(db_locale)
	c=connie.cursor()
	sql_execute_string = 'INSERT INTO questions (title, details, name) VALUES (?,?,?)';
	c.execute(sql_execute_string, user_details)
	connie.commit()
	connie.close()
	print(user_details)

def queryQuestions():
	connie= sqlite3.connect(db_locale)
	c=connie.cursor()
	c.execute("""
		SELECT * FROM questions
	""")
	userdata = c.fetchall()
	return userdata


# now we just only have to=> set Flask_debug=1
#							 python filename.py
#-----server starts for this file-----
if __name__ == '__main__':
	app.run(debug=True)


# we will pass this data in html
# push Dummy Data in home.html, @app.route('/home'), as ->.. return render_template('home.html', questions=questions)
# questions=[

# {
# 	'title':'what is benits of quora?',
# 	'name':'mr. x',
# 	'comments':'please provide authentic resource :)'
# },
# {
# 	'title':'there are benefits as the count of stars in the sky',
# 	'name':'mr. y',
# 	'comments':'type in google and post the question with a little smile on face :)',
# }

# ]
