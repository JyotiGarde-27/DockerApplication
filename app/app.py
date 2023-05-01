from flask import Flask, request
import requests
import os
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify

app = Flask(__name__)


mysql = MySQL()


mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'


# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'first'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT']=int('3306')
mysql.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        response = requests.get('http://database-service:5001/vaccination-details', params={'reg_no': reg_no})
        return response.text
    return '''
        <form method="post">
            <label for="reg_no">Enter Registration Number:</label>
            <input type="text" id="reg_no" name="reg_no">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/read from database')
def read():
    conn = mysql.connect()


    cursor = conn.cursor(pymysql.cursors.DictCursor)


    cursor.execute("SELECT * FROM employees1")
    row = cursor.fetchone()
    result = []
    while row is not None:
      row = cursor.fetchone()
      result.append(row)


      return ','.join(str(result)[1:-1])
    #   for column in row:
    #       result.append(column)
     
      
    cursor.close()
    conn.close()
    
    # return ','.join(','.join(map(str, l)) for l in result)
    return ",".join(result)


@app.route('/all users')
def users():
    conn = mysql.connect()


    cursor = conn.cursor(pymysql.cursors.DictCursor)


    cursor.execute("SELECT * FROM employees1")


    rows = cursor.fetchall()


    resp = jsonify(rows)
    resp.status_code = 200
    cursor.close()
    conn.close()


    return resp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
