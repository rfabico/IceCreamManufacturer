import cx_Oracle as cx
from flask import Flask,render_template
import pandas as pd
import config
import queries

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('base.html')

@app.route('/query1', methods=['POST'])
def query1():
    # TODO: Put a query in here, provide result as HTML to result variable
    connection = connect()
    query = pd.read_sql(queries.query1, connection)
    html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)

@app.route('/query2',methods=['POST'])
def query2():
    connection = connect()
    query = pd.read_sql(queries.query2, connection)
    html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)

@app.route('/query3',methods=['POST'])
def query3():
    connection = connect()
    query = pd.read_sql(queries.query3, connection)
    html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)

@app.route('/query4',methods=['POST'])
def query4():
    connection = connect()
    query = pd.read_sql(queries.query4, connection)
    html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)


@app.route('/query5',methods=['POST'])
def query5():
    connection = connect()
    query = pd.read_sql(queries.query5, connection)
    html_result = query.to_html(classes=['table', 'table-striped'])
    connection.close()
    return render_template('base.html', result=html_result)

def connect():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)
    return connection


if __name__ == '__main__':
    main()

