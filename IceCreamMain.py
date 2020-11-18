import cx_Oracle as cx
from flask import Flask, render_template
import pandas as pd
import config

app = Flask(__name__)


@app.route('/')
def main():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)

    connection.close()

    return render_template('base.html')

@app.route('/query1', methods=['POST'])
def query1():
    # TODO: Put a query in here, provide result as HTML to result variable
    query = pd.readsql(queries.query1)
    html_result = query.to_html()
    return render_template('base.html', result=html_result)

@app.route('/query2',methods=['POST'])
def query2():
    query = pd.readsql(queries.query2)
    html_result = query.to_html()
    return render_template('base.html', result=html_result)

@app.route('/query3',methods=['POST'])
def query3():
    query = pd.readsql(queries.query3)
    html_result = query.to_html()
    return render_template('base.html', result=html_result)

@app.route('/query4',methods=['POST'])
def query4():
    query = pd.readsql(queries.query4)
    html_result = query.to_html()
    return render_template('base.html', result=html_result)


@app.route('/query5',methods=['POST'])
def query5():
    query = pd.readsql(queries.query5)
    html_result = query.to_html()
    return render_template('base.html', result=html_result)


if __name__ == '__main__':
    main()

