import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except ConnectionError:
        print("error")
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except SyntaxError as e:
        print(e)


def create_insulator(conn, latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code):
    """
    Create a new project into the projects table
    :param conn:
    :param insulator:
    """
    sql = ''' INSERT INTO insulators(latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    print(latitude)
    cur = conn.cursor()
    cur.execute(sql, (latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code))
    conn.commit()


def create_lightning_arrester(conn, latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code):
    """
    Create a new project into the projects table
    :param conn:
    :param lightningArrester:
    """
    sql = ''' INSERT INTO lightning_arresters(latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code))
    conn.commit()


def create_splice(conn, latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code):
    """
    Create a new project into the projects table
    :param conn:
    :param splice:
    """
    sql = ''' INSERT INTO splices(latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code))
    conn.commit()


def create_disconnect_switch(conn, latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code):
    """
    Create a new project into the projects table
    :param conn:
    :param disconnectSwitch:
    """
    sql = ''' INSERT INTO disconnect_switch(latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (latitude, longitude, subtype, image_path, created_at, percentage, street_address, city, zip_code))
    conn.commit()


def select_all_object(conn, code):

    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators")
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters")
    elif code == 3:
        cur.execute("SELECT * FROM splices")
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch")
    rows = cur.fetchall()
    return rows


def delete_object(conn, code, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the object
    :return:
    """
    if code == 1:
        sql = 'DELETE FROM insulators WHERE id=?'
    elif code == 2:
        sql = 'DELETE FROM lightning_arresters WHERE id=?'
    elif code == 3:
        sql = 'DELETE FROM splices WHERE id=?'
    elif code == 4:
        sql = 'DELETE FROM disconnect_switch WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))


def select_object_by_city(conn, code, city):
    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators WHERE city=?", (city,))
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters WHERE city=?", (city,))
    elif code == 3:
        cur.execute("SELECT * FROM splices WHERE city=?", (city,))
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch WHERE city=?", (city,))
    rows = cur.fetchall()
    return rows


def select_object_by_coord(conn, code, lat, lon):
    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators WHERE latitude=? AND longitude=?", (lat, lon))
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters latitude=? AND longitude=?", (lat, lon))
    elif code == 3:
        cur.execute("SELECT * FROM splices WHERE latitude=? AND longitude=?", (lat, lon))
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch WHERE latitude=? AND longitude=?", (lat, lon))
    rows = cur.fetchall()
    return rows


def select_object_by_percentage(conn, code, percentage):
    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators WHERE percentage>=?", (percentage,))
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters WHERE percentage>=?", (percentage,))
    elif code == 3:
        cur.execute("SELECT * FROM splices WHERE percentage>=?", (percentage,))
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch WHERE percentage>=?", (percentage,))
    rows = cur.fetchall()
    return rows


def select_object_by_subtype(conn, code, subtype):
    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators WHERE subtype=?", (subtype,))
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters WHERE subtype=?", (subtype,))
    elif code == 3:
        cur.execute("SELECT * FROM splices WHERE subtype=?", (subtype,))
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch WHERE subtype=?", (subtype,))
    rows = cur.fetchall()
    return rows


def select_object_by_zip(conn, code, zip):
    cur = conn.cursor()
    if code == 1:
        cur.execute("SELECT * FROM insulators WHERE zip_code=?", (zip,))
    elif code == 2:
        cur.execute("SELECT * FROM lightning_arresters WHERE zip_code=?", (zip,))
    elif code == 3:
        cur.execute("SELECT * FROM splices WHERE zip_code=?", (zip,))
    elif code == 4:
        cur.execute("SELECT * FROM disconnect_switch WHERE zip_code=?", (zip,))
    rows = cur.fetchall()
    return rows


def initialize_db():

    sql_create_insulators_table = """CREATE TABLE if not exists insulators (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        latitude text,
                                        longitude text,
                                        subtype text,
                                        image_path text,
                                        created_at datetime,
                                        percentage integer,
                                        street_address text,
                                        city text,
                                        zip_code text
                                );"""
    sql_create_lightningArresters_table = """ CREATE TABLE if not exists lightning_arresters (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                latitude text,
                                                longitude text,
                                                subtype text,
                                                image_path text,
                                                created_at datetime,
                                                percentage integer,
                                                street_address text,
                                                city text,
                                                zip_code text
                                        );"""
    sql_create_splices_table = """CREATE TABLE if not exists splices (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    latitude text,
                                    longitude text,
                                    subtype text,
                                    image_path text,
                                    created_at datetime,
                                    percentage integer,
                                    street_address text,
                                    city text,
                                    zip_code text
                             );"""
    sql_create_disconnectSwitch_table = """ CREATE TABLE if not exists disconnect_switch (
                                                id integer PRIMARY KEY AUTOINCREMENT,
                                                latitude text,
                                                longitude text,
                                                subtype text,
                                                image_path text,
                                                created_at datetime,
                                                percentage integer,
                                                street_address text,
                                                city text,
                                                zip_code text
                                      );"""

    conn = create_connection("equipment.db")
    if conn is not None:
        create_table(conn, sql_create_insulators_table)
        create_table(conn, sql_create_lightningArresters_table)
        create_table(conn, sql_create_splices_table)
        create_table(conn, sql_create_disconnectSwitch_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    initialize_db()