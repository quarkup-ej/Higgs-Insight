import sqlite3 as sql

connection = sql.connect("store.db")
cursor = connection.cursor()

SQL_categories = '''
CREATE TABLE categories (
    id INT PRIMARY KEY,
    name TEXT NOT NULL
)
'''

SQL_products = '''
CREATE TABLE products (
    id INT PRIMARY KEY,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    id_category INT NOT NULL,
    FOREIGN KEY (id_category)
    REFERENCES categories(id)
)
'''

SQL_orders = '''
CREATE TABLE orders (
    id INT PRIMARY KEY,
    date DATE NOT NULL,
    address TEXT NOT NULL
)
'''

SQL_sales = '''
CREATE TABLE sales (
    id_order INT,
    id_product INT,
    quantity INT NOT NULL,
    PRIMARY KEY(id_order, id_product),
    FOREIGN KEY (id_order)
    REFERENCES orders(id),
    FOREIGN KEY (id_product)
    REFERENCES products(id)
)
'''

dml_list = [SQL_categories,SQL_orders,SQL_products,SQL_sales]

for SQL in dml_list:
    try:
        cursor.execute(SQL)
    except Exception as e:
        print(f"Error: {e}")
    else:
        connection.commit()
        print("Tabela criada com sucesso!")

cursor.close()
connection.close()