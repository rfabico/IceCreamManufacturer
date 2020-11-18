import cx_Oracle as cx
from flask import Flask, render_template
import pandas as pd
import config

app = Flask(__name__)


@app.route('/')
def main():
    dsn_tns = cx.makedsn(config.ip, config.port, config.sid)
    connection = cx.connect(config.user_name, config.password,dsn_tns)
    query1 = 'SELECT customers.company_name, orders.order_date, orders.total_price, orders.required_date, orders.shipped_date ' \
             'FROM orders INNER JOIN customers ON customers.customer_id = orders.customer_id ' \
             'WHERE shipped_date BETWEEN (sysdate - 90) AND sysdate'
    query2 = 'SELECT flavour_name, ingredient_name FROM flavours ' \
             'INNER JOIN flavour_ings ON flavour_ings.flavour_id = flavours.flavour_id' \
             'INNER JOIN ingredients ON ingredients.ingredient_id = flavour_ings.ingredient_id'
    query3 = "SELECT supplier_city, COUNT(supplier_id) AS 'NUMBER OF SUPPLIERS' " \
             "FROM suppliers " \
             "WHERE supplier_city <> 'Toronto'" \
             "GROUP BY supplier_city"
    query4 = "SELECT flavour_name FROM flavours " \
             "WHERE flavour_id = (SELECT flavour_id FROM flavour_ings " \
             "WHERE ingredient_id = (SELECT ingredient_id FROM ingredients WHERE ingredient_name = 'Sugar')) " \
             "ORDER BY flavour_name ASC;"
    query5 = "SELECT orders.order_id, customers.customer_first_name , customers.customer_last_name, orders.total_price, orders.order_date " \
             "FROM orders LEFT JOIN customers ON orders.customer_id = customers.customer_id " \
             "WHERE orders.order_date < to_date('8/10/2020','dd/mm/yyyy') AND orders.total_price > 700;"
    queryList = [query1, query2, query3, query4, query5]
    # for i in queryList:
    #     data = pd.read_sql(i,connection)
    #     print(data)
    connection.close()

    return render_template('base.html')


@app.route('/query1', methods=['POST'])
def query1():
    # TODO: Put a query in here, display a table as the result

    return render_template('base.html')


if __name__ == '__main__':
    main()

