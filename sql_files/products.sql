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