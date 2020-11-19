INSERT INTO flavours VALUES (flavour_pk.NEXTVAL, 'Vanilla', 'Plain Stuff');
INSERT INTO flavours VALUES (flavour_pk.NEXTVAL, 'Chocolate', 'Chocolatey Stuff');
INSERT INTO flavours VALUES (flavour_pk.NEXTVAL, 'Mango', 'May contain mango.');
INSERT INTO flavours VALUES (flavour_pk.NEXTVAL, 'Banana', 'But why?');
INSERT INTO flavours VALUES (flavour_pk.NEXTVAL, 'Rainbow', 'Why have one flavour when you can have all of them?');
INSERT INTO ingredients VALUES (pk_value.NEXTVAL, '600L', 'Cream');
INSERT INTO ingredients VALUES (pk_value.NEXTVAL, '600L', 'Milk');
INSERT INTO ingredients VALUES (pk_value.NEXTVAL, '2000kg', 'Sugar');
INSERT INTO ingredients VALUES (pk_value.NEXTVAL, '600L', 'Vanilla');
INSERT INTO ingredients VALUES (pk_value.NEXTVAL, '600L', 'Condensed Milk');
INSERT INTO brands VALUES (brand_pk.NEXTVAL, 'Chapman''s', 'contact@chapmans.ca', 'Bob', 'Smith', '123-456-7890');
INSERT INTO brands VALUES (brand_pk.NEXTVAL, 'Haagen-Dazs', 'icecream@haagen.de', 'Jon', 'Doe', '555-555-5555');
INSERT INTO brands VALUES (brand_pk.NEXTVAL, 'Ben and Jerry''s', 'email@benjerry.com', 'Ben', 'Benington', '555-123-4567');
INSERT INTO brands VALUES (brand_pk.NEXTVAL, 'No Name', 'boring@nonname.com', 'Laura', 'Laurington', '416-123-4567');
INSERT INTO brands VALUES (brand_pk.NEXTVAL, 'We Ran Out of Names', 'icecream@dunno.com', 'Jill', 'Jillington', '555-444-3333');
INSERT INTO statuses
VALUES (status_pk.NEXTVAL, 'Cancelled');
INSERT INTO statuses
VALUES (status_pk.NEXTVAL, 'In Progress');
INSERT INTO statuses
VALUES (status_pk.NEXTVAL, 'On Hold');
INSERT INTO statuses
VALUES (status_pk.NEXTVAL, 'Shipped');
INSERT INTO statuses
VALUES (status_pk.NEXTVAL, 'Completed');
INSERT INTO customers VALUES(c_id.NEXTVAL,'IScream','George','Curious','416-123-4567','george@gmail.com','1 Something st', 'Toronto');
INSERT INTO customers VALUES(c_id.NEXTVAL,'Ice Age','Pina','Nico', '911', 'notthepolice@gmail.com','55 police ave', 'Toronto');
INSERT INTO customers VALUES(c_id.NEXTVAL,'White Ice Markets', 'Jablonski', 'Karl','312-555-5555', 'karl@gmail.com','6th avenue', 'New York');
INSERT INTO customers VALUES(c_id.NEXTVAL,'BELOW 32 DEGREES', 'Park','Matthew','416-214-4576', 'matthew@gmail.com','29 icey rd', 'Toronto');
INSERT INTO customers VALUES(c_id.NEXTVAL,'Hint of Cloud', 'Delvey','Anna', '647-378-2478','anna@gmail.com', '705 Niagara rd','Niagara Falls');
INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, supplier_city, supplier_address, rep_first_name, rep_last_name, rep_phone_no)
VALUES (supplier_pk.NEXTVAL, 'Kawartha Dairy Ltd', 'kawartha@gmail.com', 'Bobcaygeon', '89 Prince St W', 'Alice', 'Fernandez', '416-123-4567');
INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, supplier_city, supplier_address, rep_first_name, rep_last_name, rep_phone_no)
VALUES (supplier_pk.NEXTVAL, 'St Clair Ice Cream Ltd', 'stclair@gmail.com', 'Toronto', '2861 Danforth Ave', 'Peter', 'Parker', '416-652-9845');
INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, supplier_city, supplier_address, rep_first_name, rep_last_name, rep_phone_no)
VALUES (supplier_pk.NEXTVAL, 'Gelato Fresco', 'gelatofresco@gmail.com', 'Toronto', '60 Tycos Dr', 'Mark', 'Ruffalo', '416-354-9844');
INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, supplier_city, supplier_address, rep_first_name, rep_last_name, rep_phone_no)
VALUES (supplier_pk.NEXTVAL, 'Chapman Ice Cream', 'chapman@gmail.com', 'Markdale', '160 Main St., W.', 'Chris', 'Evans', '416-625-7984');
INSERT INTO suppliers(supplier_id, supplier_name, supplier_email, supplier_city, supplier_address, rep_first_name, rep_last_name, rep_phone_no)
VALUES (supplier_pk.NEXTVAL, 'Metropolitan Ice Cream Inc.', 'metropolitan@gmail.com', 'North York', '10 Benton Rd', 'Jeremy', 'Renner', '647-111-2222');
INSERT INTO sizes
VALUES (3, 'large');
INSERT INTO sizes
VALUES (2, 'medium');
INSERT INTO sizes
VALUES (1, 'small');
INSERT INTO products
SELECT prod_pk.NEXTVAL, flavour_id, size_id, 12, 12.45, (12 * 12.45), 'Plain Jane'
FROM flavours, sizes
WHERE flavour_name = 'Vanilla' AND size_name = 'medium';
INSERT INTO products
SELECT prod_pk.NEXTVAL, flavour_id, size_id, 75, 20, 0, 'Rainbow Explosion'
FROM flavours, sizes
WHERE flavour_name = 'Rainbow' AND size_name = 'medium';
INSERT INTO products
SELECT prod_pk.NEXTVAL, flavour_id, size_id, 50, 15.25, (50 * 15.25), 'Mango Madness'
FROM flavours, sizes
WHERE flavour_name = 'Mango' AND size_name = 'large';
INSERT INTO products
SELECT prod_pk.NEXTVAL, flavour_id, size_id, 100, 13.25, (100 * 13.25), 'Chocolate?'
FROM flavours, sizes
WHERE flavour_name = 'Chocolate' AND size_name = 'small';
INSERT INTO products
SELECT prod_pk.NEXTVAL, flavour_id, size_id, 20, 20.25, (20 * 20.25), 'Banana Bonanza'
FROM flavours, sizes
WHERE flavour_name = 'Banana' AND size_name = 'large';
INSERT INTO orders
SELECT order_id.NEXTVAL, customer_id, to_date('8/10/2020','dd/mm/yyyy'), 3500, 
to_date('9/10/2020','dd/mm/yyyy'), to_date('8/10/2020','dd/mm/yyyy'), '1 Something st',
(SELECT status_id FROM statuses WHERE status_name = 'Shipped')
FROM customers
WHERE company_name = 'IScream';
INSERT INTO orders
SELECT order_id.NEXTVAL, customer_id, to_date('8/10/2020','dd/mm/yyyy'), 500, 
to_date('15/10/2020','dd/mm/yyyy'), NULL, '1 Something st',
(SELECT status_id FROM statuses WHERE status_name = 'In Progress')
FROM customers
WHERE company_name = 'IScream';
INSERT INTO orders
SELECT order_id.NEXTVAL, customer_id, to_date('7/10/2020','dd/mm/yyyy'), 1200,
to_date('11/10/2020','dd/mm/yyyy'), NULL, '6th avenue',
(SELECT status_id FROM statuses WHERE status_name = 'Shipped')
FROM customers
WHERE company_name = 'White Ice Markets';
INSERT INTO orders
SELECT order_id.NEXTVAL, customer_id, to_date('2/10/2020','dd/mm/yyyy'), 650,
to_date('7/10/2020','dd/mm/yyyy'), to_date('7/10/2020','dd/mm/yyyy'), '55 police ave',
(SELECT status_id FROM statuses WHERE status_name = 'Completed')
FROM customers
WHERE company_name = 'Ice Age';
INSERT INTO orders
SELECT order_id.NEXTVAL, customer_id, to_date('6/10/2020', 'dd/mm/yyyy'), 800,
to_date('8/10/2020','dd/mm/yyyy'), to_date('8/10/2020','dd/mm/yyyy'), '55 police ave',
(SELECT status_id FROM statuses WHERE status_name = 'Shipped')
FROM customers
WHERE company_name = 'Ice Age';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id 
FROM ingredients, flavours
where flavours.flavour_name = 'Vanilla' AND ingredients.ingredient_name = 'Vanilla';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id 
FROM ingredients, flavours
where flavours.flavour_name = 'Rainbow' AND ingredients.ingredient_name = 'Cream';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id 
FROM ingredients, flavours
where flavours.flavour_name = 'Mango' AND ingredients.ingredient_name = 'Milk';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id 
FROM ingredients, flavours
where flavours.flavour_name = 'Chocolate' AND ingredients.ingredient_name = 'Sugar';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id 
FROM ingredients, flavours
where flavours.flavour_name = 'Banana' AND ingredients.ingredient_name = 'Condensed Milk';
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=2 AND products.product_id=4;
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=3 AND products.product_id=2;
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=3 AND products.product_id=3;
INSERT INTO order_products SELECT op_id.NEXTVAL, orders.order_id,products.product_id FROM orders, products WHERE orders.order_id=5 AND products.product_id=2;
INSERT INTO favourites 
SELECT favourite_id.NEXTVAL, products.product_id, 'Weekly', 100 
FROM products 
WHERE products.flavour_id=(
    SELECT flavour_id FROM flavours
    WHERE flavour_name='Vanilla'
);
INSERT INTO favourites 
SELECT favourite_id.NEXTVAL, products.product_id, 'Monthly',50
FROM products 
WHERE products.flavour_id=(
    SELECT flavour_id FROM flavours
    WHERE flavour_name='Banana'
);
INSERT INTO favourites 
SELECT favourite_id.NEXTVAL, products.product_id, 'Weekly', 50
FROM products
WHERE products.flavour_id=(
    SELECT flavour_id FROM flavours
    WHERE flavour_name='Chocolate'
);
INSERT INTO favourites 
SELECT favourite_id.NEXTVAL, products.product_id, 'Weekly', 50
FROM products
WHERE products.flavour_id=(
    SELECT flavour_id FROM flavours
    WHERE flavour_name='Mango'
);
INSERT INTO favourites 
SELECT favourite_id.NEXTVAL, products.product_id, 'Monthly', 100
FROM products
WHERE products.flavour_id=(
    SELECT flavour_id FROM flavours
    WHERE flavour_name='Chocolate'
);