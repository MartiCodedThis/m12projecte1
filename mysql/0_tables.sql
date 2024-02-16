CREATE TABLE statuses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    slug TEXT
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    role TEXT NOT NULL DEFAULT 'wanner',
    email_token TEXT DEFAULT NULL,
    verified INTEGER DEFAULT 0,
    token TEXT,
    token_expiration TEXT
);

CREATE TABLE blocked_users (
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    PRIMARY KEY(user_id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT UNIQUE,
    slug TEXT UNIQUE
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title TEXT,
    description TEXT,
    photo TEXT,
    price DECIMAL(10, 2),
    category_id INTEGER,
    seller_id INTEGER,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status_id INTEGER,
    FOREIGN KEY(category_id) REFERENCES categories(id),
    FOREIGN KEY(seller_id) REFERENCES users(id)
);

CREATE TABLE banned_products (
    product_id INTEGER NOT NULL,
    reason TEXT NOT NULL,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(product_id) REFERENCES products(id),
    PRIMARY KEY(product_id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    product_id INTEGER,
    buyer_id INTEGER,
    offer NUMERIC DEFAULT 0,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uc_product_buyer UNIQUE (product_id, buyer_id),
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(buyer_id) REFERENCES users(id)
);

CREATE TABLE confirmed_orders (
    order_id INTEGER,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    PRIMARY KEY(order_id)
);
