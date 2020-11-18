import cx_Oracle as cx
import flask as fl
import pandas as pd
import config

def main():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)
    sql = "SELECT * FROM product"
    cursor = cx.Cursor(connection)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)


if __name__ == '__main__':
    main()

