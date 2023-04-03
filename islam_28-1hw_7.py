import sqlite3


def Create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection



def creat_table(connection,sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)



def creat_products(connection, products):
    try:
        sql = '''INSERT INTO products (product_title,price,quantity)
        VALUES (?,?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    try:
        sql = '''SELECT * FROM products '''
        cursor = connection.cursor()
        cursor.execute(sql)

        rouws = cursor.fetchall()
        for row in rouws:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_limit(connection,limit):
    try:
        sql = '''SELECT * FROM products WHERE price >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql,(limit,))

        rouws = cursor.fetchall()
        for row in rouws:
            print(row)
    except sqlite3.Error as e:
        print(e)



def ubdate_student(connection, products):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_student(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql,(id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def search_by_word(conn, word):
    try:
        sql = '''select * from products where product_title like ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


data_base_name = 'hw.db'

sgl_creat_products = '''
CREATE TABLE products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10.2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0)
'''

connection_to_db = Create_connection(data_base_name)
if connection_to_db is not None:
    print('Succesfully connected!')
    # creat_table(connection_to_db,sgl_creat_products)
    # creat_products(connection_to_db,('CocoColoa',80,3))
    # creat_products(connection_to_db,('Pepsi 1l',80,4))
    # creat_products(connection_to_db,('Asu 1l',45,2))
    # creat_products(connection_to_db,('CocoCola 1.5l',95,4))
    # creat_products(connection_to_db,('lays 150g',110,6))
    # creat_products(connection_to_db,('Legenda 1l',30,5))
    # creat_products(connection_to_db,('Гель для стирки Persill 1.5l',510,2))
    # creat_products(connection_to_db,('Faryy 900ml',180,1))
    # creat_products(connection_to_db,('мыло dalan ',55,1))
    # creat_products(connection_to_db,('кетчуп 50ml ',80,2))
    # creat_products(connection_to_db,('хлеб рыжанной ', 30,2))
    # creat_products(connection_to_db,('соль 1kg',30,1))
    # creat_products(connection_to_db,('сахар 1kg',85,1))
    # creat_products(connection_to_db,('рис кроснодар ',90,3))
    # creat_products(connection_to_db,('молоко 1l',60,4))



    # search_by_word(connection_to_db,'Coco')
    # select_products_by_price_limit(connection_to_db,60)
    # delete_student(connection_to_db,3)
    # ubdate_student(connection_to_db,(90.65,3))
    # select_all_products(connection_to_db)
    connection_to_db.close()
    print('done')




