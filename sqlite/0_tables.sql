CREATE TABLE "statuses" (
	"id"	INTEGER,
	"name"	TEXT,
	"slug"	TEXT,
	PRIMARY KEY("id")
)

CREATE TABLE "users" (
	"id"	INTEGER,
	"name"	TEXT UNIQUE,
	"email"	TEXT UNIQUE,
	"password"	TEXT,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"updated"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"role"	TEXT NOT NULL DEFAULT 'wanner',
	"email_token"	TEXT DEFAULT NULL,
	"verified"	INTEGER DEFAULT 0,
	"token"	TEXT,
	"token_expiration"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
CREATE TABLE "blocked_users" (
	"user_id"	INTEGER NOT NULL,
	"message"	STRING NOT NULL,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("user_id")
)

CREATE TABLE categories (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE,
	slug TEXT UNIQUE
)
CREATE TABLE "products" (
	"id"	INTEGER,
	"title"	TEXT,
	"description"	TEXT,
	"photo"	TEXT,
	"price"	DECIMAL(10, 2),
	"category_id"	INTEGER,
	"seller_id"	INTEGER,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"updated"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	"status_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("seller_id") REFERENCES "users"("id"),
	FOREIGN KEY("category_id") REFERENCES "categories"("id")
)
CREATE TABLE "banned_products" (
	"product_id"	INTEGER NOT NULL,
	"reason"	TEXT NOT NULL,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY("product_id") REFERENCES "products"("id"),
	PRIMARY KEY("product_id")
)

CREATE TABLE "orders" (
	"id"	INTEGER,
	"product_id"	INTEGER,
	"buyer_id"	INTEGER,
	"offer"	DECIMAL(10, 2),
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	CONSTRAINT "uc_product_buyer" UNIQUE("product_id","buyer_id"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("product_id") REFERENCES "products"("id"),
	FOREIGN KEY("buyer_id") REFERENCES "users"("id")
)
CREATE TABLE "confirmed_orders" (
	"order_id"	INTEGER,
	"created"	DATETIME NOT NULL DEFAULT (DATETIME('now')),
	FOREIGN KEY("order_id") REFERENCES "orders"("id"),
	PRIMARY KEY("order_id")
)