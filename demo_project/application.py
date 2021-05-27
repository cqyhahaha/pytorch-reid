from flask import Flask, render_template, request, jsonify
import mysql.connector
import json

application = Flask(__name__, static_url_path='/static')
#app = Flask(__name__)



@application.route('/')
def index():
	return render_template('index.html')

def db_connection():
    mydb = mysql.connector.connect( host = '192.168.1.100',
    user = 'cqy',
    port = '3306',
    database = 'edgedemo',
    passwd = '123456',
    autocommit = True)
    return mydb


@application.route('/query',methods=['POST','GET'])
def query():
	mydb = db_connection()
	cur = mydb.cursor()
	print("Opened database successfully")

	if request.method == "POST":

		PersonID = request.form['PersonID']
		print(PersonID)
		print(type(PersonID))
		info = "select * from REID where person == '{}'".format(PersonID)
		cur.execute(info)
		data = cur.fetchall()
		print(type(data))

		results = ""
		for item in data:
			results += "<tr><td>"+ str(item[0])+"</td>"+"<td>"+ str(item[1])+"</td>"+"<td>"+str(item[2])+"</td>"+"</tr>"

		return results

if __name__ == '__main__':
	application.run(port=5000, debug = True)