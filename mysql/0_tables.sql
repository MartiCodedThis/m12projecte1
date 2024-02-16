CREATE TABLE statuses (
    id INTEGER PRIMARY KEY,
    name VARCHAR(64) UNIQUE,
    slug VARCHAR(64) UNIQUE
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) UNIQUE,
    email VARCHAR(64) UNIQUE,
    password VARCHAR(255),
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(16) NOT NULL DEFAULT 'wanner',
    email_token VARCHAR(255) DEFAULT NULL,
    verified INTEGER DEFAULT 0,
    token VARCHAR(32),
    token_expiration TEXT
);

CREATE TABLE blocked_users (
    user_id INTEGER NOT NULL,
    message TEXT,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    PRIMARY KEY(user_id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) UNIQUE,
    slug VARCHAR(64) UNIQUE
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    description TEXT,
    photo VARCHAR(255),
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
    reason TEXT,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(product_id) REFERENCES products(id),
    PRIMARY KEY(product_id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    product_id INTEGER,
    buyer_id INTEGER,
    offer DECIMAL(10, 2) DEFAULT 0,
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
