INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=2 AND products.product_id=4;
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=3 AND products.product_id=2;
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=3 AND products.product_id=3;
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=5 AND products.product_id=2;
