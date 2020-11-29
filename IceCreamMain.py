import cx_Oracle as cx
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import config
import queries

app = Flask(__name__)

tables = ['flavours', 'ingredients', 'brands', 'suppliers', 'customers', 'statuses', 'sizes', 'products', 'flavour_ing',
          'favourites', 'orders', 'order_prod']

class Person:
  def __init__(self, name, passw):
    self.name = name
    self.password = passw

admin = Person("admin", "adminIC5")
user = Person("user", "userIC2")
app_user = Person(None, None)

@app.route('/')
def main():
    global app_user
    return render_template('base.html', app_user=app_user)

@app.route('/login', methods=['POST'])
def login():
    global app_user
    error = None
    if request.form['username'] == 'admin' and request.form['password'] == admin.password:
        app_user = admin
    if request.form['username'] == 'user' and request.form['password'] == user.password:
        app_user = user
    else:
        error = 'Invalid Credentials. Please try again.'
    return render_template('base.html', error=error, app_user=app_user)

@app.route('/query1')
def query1():
    global app_user
    try:
        connection = connect()
        query = pd.read_sql(queries.query1, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
        connection.close()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Query Error</h4>'
    except Exception as e:
        print(e)
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result, app_user=app_user)

@app.route('/query2')
def query2():
    global app_user
    try:
        connection = connect()
        query = pd.read_sql(queries.query2, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
        connection.close()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Query Error</h4>'
    except Exception as e:
        print(e)
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result, app_user=app_user)

@app.route('/query3')
def query3():
    global app_user
    try:
        connection = connect()
        query = pd.read_sql(queries.query3, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
        connection.close()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Query Error</h4>'
    except Exception as e:
        print(e)
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result, app_user=app_user)

@app.route('/query4')
def query4():
    global app_user
    try:
        connection = connect()
        query = pd.read_sql(queries.query4, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
        connection.close()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Query Error</h4>'
    except Exception as e:
        print(e)
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result, app_user=app_user)


@app.route('/query5')
def query5():
    global app_user
    try:
        connection = connect()
        query = pd.read_sql(queries.query5, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
        connection.close()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Query Error</h4>'
    except Exception as e:
        print(e)
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result, app_user=app_user)

@app.route('/populate')
def populate_tables():
    global app_user
    fo = open('populate_tables.sql', 'r')
    allsql = fo.read()
    fo.close()
    sql_commands = allsql.split(';')
    sql_commands = [command.strip() for command in sql_commands]
    sql_commands = [command.replace('\n',' ') for command in sql_commands]
    sql_commands = sql_commands[:-1]
    connection = connect()
    html_result = '<h4>Tables populated</h4>'
    with connection.cursor() as cursor:
        for command in sql_commands:
            try:
                cursor.execute(command)
                connection.commit()
            except cx.Error as e:
                errorObj, = e.args
                print('error code: ', errorObj.code)
                print('error message: ', errorObj.message)
                html_result = '<h4>Error populating</h4>'

    connection.close()
    return render_template('base.html', result=html_result, app_user=app_user)
  
def populate(table):
    path = 'sql_files/'
    fo = open(path + table, 'r')
    allsql = fo.read()
    fo.close()
    sql_commands = allsql.split(';')
    sql_commands = [command.strip() for command in sql_commands]
    sql_commands = [command.replace('\n',' ') for command in sql_commands]
    sql_commands = sql_commands[:-1]
    connection = connect()
    with connection.cursor() as cursor:
        for command in sql_commands:
            try:
                cursor.execute(command)
                connection.commit()
            except cx.Error as e:
                errorObj, = e.args
                print('error code: ', errorObj.code)
                print('error message: ', errorObj.message)
                html_result = '<h4>Error populating</h4>'
    if html_result is None:
        query = pd.read_sql('SELECT * FROM ' + table, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)

@app.route('/create')
def create_tables():
    global app_user
    fo = open('create_tables.sql', 'r')
    allsql = fo.read()
    fo.close()
    sql_commands = allsql.split(';')
    sql_commands = [command.strip() for command in sql_commands]
    sql_commands = [command.replace('\n',' ') for command in sql_commands]
    sql_commands = sql_commands[:-1]
    connection = connect()
    html_result = '<h4>Tables created</h4>'
    with connection.cursor() as cursor:
        for command in sql_commands:
            try:
                cursor.execute(command)
            except cx.Error as e:
                errorObj, = e.args
                print('error code: ', errorObj.code)
                print('error message: ', errorObj.message)
                html_result = '<h4>Error creating</h4>'

    connection.close()
    return render_template('base.html', result=html_result, app_user=app_user)

def create(table):
    index = tables.index(table)
    to_create = create.create_tables[index]
    pk = create.pk_list[index]
    connection = connect()
    with connection.cursor() as cursor:
        try:
            cursor.execute(pk)
            connection.commit()
            cursor.execute(to_create)
            connection.commit()
        except cx.Error as e:
            errorObj, = e.args
            print('error code: ', errorObj.code)
            print('error message: ', errorObj.message)
            html_result = '<h4>Error creating</h4>'
    if html_result is None:
        query = pd.read_sql('SELECT * FROM ' + table, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)
  
@app.route('/drop')
def tables_dropped():
    global app_user
    fo = open('drop_tables.sql', 'r')
    allsql = fo.read()
    fo.close()
    sql_commands = allsql.split(';')
    sql_commands = [command.strip() for command in sql_commands]
    sql_commands = sql_commands[:-1]
    connection = connect()
    html_result = '<h4>Tables dropped</h4>'
    with connection.cursor() as cursor:
        for command in sql_commands:
            try:
                cursor.execute(command)
            except cx.Error as e:
                errorObj, = e.args
                print('error code: ', errorObj.code)
                print('error message: ', errorObj.message)
                html_result = '<h4>Error dropping</h4>'

    connection.close()
    return render_template('base.html', result=html_result, app_user=app_user)

def drop(table):
    index = tables.index(table)
    to_drop = drop.drop_tables[index]
    pk = create.pk_list[index]
    connection = connect()
    with connection.cursor() as cursor:
        try:
            cursor.execute(pk)
            connection.commit()
            cursor.execute(to_drop)
            connection.commit()
        except cx.Error as e:
            errorObj, = e.args
            print('error code: ', errorObj.code)
            print('error message: ', errorObj.message)
            html_result = '<h4>Error dropping</h4>'
    if html_result is None:
        query = pd.read_sql('SELECT * FROM ' + table, connection)
        html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)
  
@app.route('/test')
def test_connection():
    global app_user
    html_result = '<h4>Connection successful</h4>'
    try:
        connection = connect()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Error dropping</h4>'
    connection.close()
    return render_template('base.html', result=html_result, app_user=app_user)

def connect():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)
    return connection


if __name__ == '__main__':
    main()

