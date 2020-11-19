import cx_Oracle as cx
from flask import Flask,render_template
import pandas as pd
import config
import queries

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('base.html')


@app.route('/query1')
def query1():
    # TODO: Put a query in here, provide result as HTML to result variable
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
    except pd.DatabaseError as e:
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result)

@app.route('/query2')
def query2():
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
    except pd.DatabaseError as e:
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result)

@app.route('/query3')
def query3():
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
    except pd.DatabaseError as e:
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result)

@app.route('/query4')
def query4():
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
    except pd.DatabaseError as e:
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result)


@app.route('/query5')
def query5():
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
    except pd.DatabaseError as e:
        html_result = '<h4>Query Error</h4>'
    return render_template('base.html', result=html_result)

@app.route('/populate')
def populate_tables():
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
    return render_template('base.html', result=html_result)

@app.route('/create')
def create_tables():
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
    return render_template('base.html', result=html_result)

@app.route('/drop')
def tables_dropped():
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
    return render_template('base.html', result=html_result)

@app.route('/test')
def test_connection():
    html_result = '<h4>Connection successful</h4>'
    try:
        connection = connect()
    except cx.Error as e:
        errorObj, = e.args
        print('error code: ', errorObj.code)
        print('error message: ', errorObj.message)
        html_result = '<h4>Error dropping</h4>'
    connection.close()
    return render_template('base.html', result=html_result)

def connect():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)
    return connection


if __name__ == '__main__':
    main()

