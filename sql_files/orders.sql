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