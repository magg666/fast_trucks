from database.db_connect import connect


def get_all_countries():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM countries")
    result = cursor.fetchall()
    return result


def get_all_borders():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM distances")
    result = cursor.fetchall()
    return result

