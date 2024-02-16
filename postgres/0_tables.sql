CREATE TABLE statuses (
    id SERIAL PRIMARY KEY,
    name TEXT,
    slug TEXT
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    slug TEXT UNIQUE
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    role TEXT NOT NULL DEFAULT 'wanner',
    email_token TEXT DEFAULT NULL,
    verified INTEGER DEFAULT 0,
    token TEXT,
    token_expiration TEXT
);

CREATE TABLE blocked_users (
    user_id INTEGER PRIMARY KEY,
    message TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    title TEXT,
    description TEXT,
    photo TEXT,
    price DECIMAL(10, 2),
    category_id INTEGER,
    seller_id INTEGER,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    status_id INTEGER,
    FOREIGN KEY (seller_id) REFERENCES users (id),
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
CREATE TABLE banned_products (
    product_id INTEGER PRIMARY KEY,
    reason TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id)
);
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    product_id INTEGER,
    buyer_id INTEGER,
    offer NUMERIC DEFAULT 0,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (buyer_id) REFERENCES users (id),
    CONSTRAINT uc_product_buyer UNIQUE (product_id, buyer_id)
);

CREATE TABLE confirmed_orders (
    order_id INTEGER PRIMARY KEY,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (id)
);