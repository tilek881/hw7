import sqlite3


def create_database():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    );
    """)

    conn.commit()
    conn.close()


def add_products():
    products = [
        ("Мыло жидкое", 50.0, 10),
        ("Шампунь", 200.0, 5),
        ("Зубная паста", 100.0, 20),
        ("Крем для рук", 150.0, 7),
        ("Мыло детское", 60.0, 15),
        ("Бальзам для волос", 300.0, 3),
        ("Пена для бритья", 250.0, 8),
        ("Мыло хозяйственное", 40.0, 25),
        ("Гель для душа", 180.0, 12),
        ("Туалетная бумага", 35.0, 50),
        ("Порошок стиральный", 450.0, 10),
        ("Пятновыводитель", 500.0, 2),
        ("Салфетки влажные", 70.0, 30),
        ("Мочалка", 25.0, 40),
        ("Щетка для волос", 120.0, 6),
    ]

    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?);", products)
    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?;", (new_quantity, product_id))
    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?;", (new_price, product_id))
    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?;", (product_id,))
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products;")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


def get_products_by_limit(price_limit, quantity_limit):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM products
    WHERE price < ? AND quantity > ?;
    """, (price_limit, quantity_limit))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


def search_products(keyword):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM products
    WHERE product_title LIKE ?;
    """, (f"%{keyword}%",))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)


# if __name__ == "__main__":
#     create_database()
#     add_products()
#     print("Все товары:")
#     get_all_products()
#
#     print("\nОбновляем количество товара id=1 до 50:")
#     update_quantity(1, 50)
#     get_all_products()
#
#     print("\nОбновляем цену товара id=2 до 250.5:")
#     update_price(2, 250.5)
#     get_all_products()
#
#     print("\nУдаляем товар с id=3:")
#     delete_product(3)
#     get_all_products()
#
#     print("\nТовары дешевле 100 сомов и с количеством больше 5:")
#     get_products_by_limit(100, 5)
#
#     print("\nПоиск товаров с ключевым словом 'мыло':")
#     search_products("мыло")
