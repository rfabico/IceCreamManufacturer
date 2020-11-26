CREATE TABLE flavours (
    flavour_id INTEGER PRIMARY KEY,
    flavour_name VARCHAR2(30) NOT NULL,
    flavour_description VARCHAR2(255)
);
CREATE SEQUENCE flavour_pk START WITH 1;
CREATE TABLE ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    ingredient_quantity VARCHAR2(30) NOT NULL,
    ingredient_name VARCHAR2(30) NOT NULL
);
CREATE SEQUENCE pk_value START WITH 1;
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name VARCHAR2(30) NOT NULL,
    supplier_email VARCHAR2(50),
    rep_first_name VARCHAR2(30) NOT NULL,
    rep_last_name VARCHAR2(30) NOT NULL,
    rep_phone_no VARCHAR2(30) NOT NULL,
    supplier_address VARCHAR2(100) NOT NULL,
    supplier_city VARCHAR2(30) NOT NULL
);
CREATE SEQUENCE supplier_pk START WITH 1;
CREATE TABLE brands (
    brand_id INTEGER PRIMARY KEY,
    brand_name VARCHAR2(30) NOT NULL,
    brand_email VARCHAR2(50),
    rep_first_name VARCHAR2(30) NOT NULL,
    rep_last_name VARCHAR2(30) NOT NULL,
    rep_phone_no VARCHAR2(30) NOT NULL
);
CREATE SEQUENCE brand_pk START WITH 1;
CREATE TABLE statuses (
    status_id INTEGER PRIMARY KEY,
    status_name VARCHAR2(30) NOT NULL
);
CREATE SEQUENCE status_pk START WITH 1;
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    company_name VARCHAR2(30) NOT NULL,
    customer_last_name VARCHAR2(30) NOT NULL,
    customer_first_name VARCHAR2(30) NOT NULL,
    customer_phone VARCHAR2(30) NOT NULL,
    customer_email VARCHAR2(50),
    customer_address VARCHAR(100) NOT NULL,
    customer_city VARCHAR2(30) NOT NULL
);
CREATE SEQUENCE size_pk START WITH 1;
CREATE TABLE sizes (
    size_id INTEGER PRIMARY KEY,
    size_name VARCHAR2(30) NOT NULL
);
CREATE SEQUENCE c_id START WITH 1;
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    flavour_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 0 NOT NULL,
    price_each DECIMAL NOT NULL,
    purchase_amount DECIMAL NOT NULL,
    product_name VARCHAR2(30) NOT NULL,
    FOREIGN KEY (flavour_id) REFERENCES flavours(flavour_id),
    FOREIGN KEY (size_id) REFERENCES sizes(size_id)
);
CREATE SEQUENCE prod_pk START WITH 1;
CREATE TABLE flavour_ings (
    flavour_ing_id INTEGER PRIMARY KEY,
    flavour_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    FOREIGN KEY (flavour_id) REFERENCES flavours(flavour_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);
CREATE SEQUENCE fl_ig_pk START WITH 1;
CREATE TABLE favourites (
    favourite_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    frequency VARCHAR2(30),
    total_amount INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
CREATE SEQUENCE favourite_id START WITH 1;
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    total_price DECIMAL NOT NULL,
    required_date DATE NOT NULL,
    shipped_date DATE,
    shipping_address VARCHAR2(100) NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (status_id) REFERENCES statuses(status_id)
);
CREATE SEQUENCE order_id START WITH 1;
CREATE TABLE order_products (
    order_prod_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
CREATE SEQUENCE op_id START WITH 1;