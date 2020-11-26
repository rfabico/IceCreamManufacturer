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