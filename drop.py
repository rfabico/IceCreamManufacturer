ord_prod = "DROP TABLE order_products CASCADE CONSTRAINTS;"
orders = "DROP TABLE orders CASCADE CONSTRAINTS;"
favourites = "DROP TABLE favourites CASCADE CONSTRAINTS;"
flavouring = "DROP TABLE flavour_ings CASCADE CONSTRAINTS;"
products = "DROP TABLE products CASCADE CONSTRAINTS;"
customers = "DROP TABLE customers CASCADE CONSTRAINTS;"
status = "DROP TABLE statuses CASCADE CONSTRAINTS;"
brands = "DROP TABLE brands CASCADE CONSTRAINTS;"
suppliers = "DROP TABLE suppliers CASCADE CONSTRAINTS;"
ingredients = "DROP TABLE ingredients CASCADE CONSTRAINTS;"
flavours = "DROP TABLE flavours CASCADE CONSTRAINTS;"
sizes = "DROP TABLE sizes;"
ord_prod_pk = "DROP SEQUENCE op_id;"
order_pk = "DROP SEQUENCE order_id;"
favourites_pk = "DROP SEQUENCE favourite_id;"
flavouring_pk = "DROP SEQUENCE fl_ig_pk;"
products_pk = "DROP SEQUENCE prod_pk;"
customers_pk = "DROP SEQUENCE c_id;"
status_pk = "DROP SEQUENCE status_pk;"
brands_pk = "DROP SEQUENCE brand_pk;"
supplier_pk = "DROP SEQUENCE supplier_pk;"
ingredients_pk = "DROP SEQUENCE pk_value;"
flavour_pk = "DROP SEQUENCE flavour_pk;"
size_pk ="DROP SEQUENCE size_pk;"

drop_tables = [flavours, ingredients, brands, suppliers, customers, status, sizes, products, flavouring, favourites,
               orders, ord_prod]
pk_list = [flavour_pk, ingredients_pk, brands_pk, supplier_pk, customers_pk, status_pk, size_pk, products_pk,
           flavouring_pk, favourites_pk, order_pk, ord_prod_pk]
