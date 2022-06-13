import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/create', methods=['POST'])
def create_emp():
    try:
        _json = request.json
        _first_name = _json['first_name']
        _email_id = _json['email_id']
        _last_name = _json['last_name']
        if _first_name and _email_id and _last_name and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            sqlQuery = "INSERT INTO user(first_name, email_id, last_name) VALUES(%s, %s, %s)"
            bindData = (_first_name, _email_id, _last_name)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Customer added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/read')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        empRows = cursor.fetchall()
        conn.commit()
        cursor.close()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/single_user')
def emp_details():
    try:
        id = request.args.get('id')
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE id =%s", id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _id = _json['id']
        _first_name = _json['first_name']
        _email_id = _json['email_id']
        _last_name = _json['last_name']
        if _first_name and _email_id and _last_name and _id and request.method == 'PUT':
            sqlQuery = "UPDATE user SET first_name=%s, email_id=%s, last_name=%s WHERE id=%s"
            bindData = (_first_name, _email_id, _last_name, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Customer updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete', methods=['DELETE'])
def delete_emp():
    try:
        id = request.args.get('id')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE id =%s", (id,))
        conn.commit()
        respone = jsonify('Customer deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.debug = True
    app.run()
