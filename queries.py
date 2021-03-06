query1 = 'SELECT customers.company_name, orders.order_date, orders.total_price, orders.required_date, orders.shipped_date ' \
         'FROM orders INNER JOIN customers ON customers.customer_id = orders.customer_id ' \
         'WHERE shipped_date BETWEEN (sysdate - 90) AND sysdate'
query2 = 'SELECT flavour_name, ingredient_name FROM flavours ' \
         'INNER JOIN flavour_ings ON flavour_ings.flavour_id = flavours.flavour_id ' \
         'INNER JOIN ingredients ON ingredients.ingredient_id = flavour_ings.ingredient_id '
query3 = """SELECT supplier_city, COUNT(supplier_id) AS "NUMBER OF SUPPLIERS" """ \
         """FROM suppliers """ \
         """WHERE supplier_city <> 'Toronto' """ \
         """GROUP BY supplier_city"""
query4 = "SELECT flavour_name FROM flavours " \
         "WHERE flavour_id = (SELECT flavour_id FROM flavour_ings " \
         "WHERE ingredient_id = (SELECT ingredient_id FROM ingredients WHERE ingredient_name = 'Sugar')) " \
         "ORDER BY flavour_name ASC"
query5 = "SELECT orders.order_id, customers.customer_first_name , customers.customer_last_name, orders.total_price, orders.order_date " \
         "FROM orders LEFT JOIN customers ON orders.customer_id = customers.customer_id " \
         "WHERE orders.order_date < to_date('8/10/2020','dd/mm/yyyy') AND orders.total_price > 700"
queryList = [query1, query2, query3, query4, query5]