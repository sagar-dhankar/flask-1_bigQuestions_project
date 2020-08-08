# flask-1_bigQuestions_project

_______________________________________________________
|		COMMAND PROMPT
|
|	1.) mkdir foldername
|	2.) cls	#clear the screen
|	3.) dir # shows the folders and files in present folder
|
|________________________________________________________
|
|		PYTHON 
|	INITIAL STEPS TO INSTALL AND CONFIGURE
|
|	python --version
|	pip help #checks if pip is installed, generally it installed in latest py2, py3
|	py -m pip install --upgrade pip #to upgrade version of pip if it is installed already
|	py -m pip install --user virtualenv #install virtual machine setup in KB
|	py -m venv env
|	env\Scripts\activate #activate virtual
|	pip install flask #in KB
|________________________________________________
|
| env\Scripts\activate	#to activate the virtual machine
|	#folder is one up to (env folder)
| 
| cd foldername	#in which your filename.py reside
|
| python filename.py	#to start the local server
| Option1: set flask_app=filename.py
|	
|	
| Option2: set flask_debug=1
|_________________________________________________
|	flask run
|	#starts the server at provided address
|	ctrl + c #to stop server
|__________________________________________________
After that the below code will work ;)

D:\sagar\codes\python_code\pythonP\flask_projects>env\Scripts\activate

(env) D:\sagar\codes\python_code\pythonP\flask_projects>cd myflaskfolder

(env) D:\sagar\codes\python_code\pythonP\flask_projects\myflaskfolder>python bigQuestions.py
 * Serving Flask app "bigQuestions" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 208-290-692
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
