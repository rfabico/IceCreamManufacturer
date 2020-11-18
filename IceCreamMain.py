import cx_Oracle as cx
from flask import Flask, render_template
import pandas as pd
import config

app = Flask(__name__)


@app.route('/')
def main():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)
    sql = "SELECT * FROM product"
    cursor = cx.Cursor(connection)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    return render_template('base.html')


if __name__ == '__main__':
    main()

