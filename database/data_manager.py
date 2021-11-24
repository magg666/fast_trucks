from database.db_connect import connect


# In this project I omitted passing the parameters into queries, but proper way is to use parametrised queries
# for example:
# def get_something(parameter):
#     db = connect()
#     cursor = db.cursor()
#     cursor.execute("SELECT shortcut, country FROM countries WHERE parameter=%(parameter )s", {'parameter': parameter})
#     result = cursor.fetchall()
#     return result


def get_all_shortcuts_of_countries():
    """
    Function grabs results from datatable where countries are stored.
    :return:list of strings (shortcuts for countries)
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT shortcut FROM countries")
    result = cursor.fetchall()
    all_shortcuts = []
    for record in result:
        all_shortcuts.append(record.get("shortcut"))

    return all_shortcuts


def get_all_roads():
    """
    Function grabs all connections between countries
    :return:list of dictionaries
    """
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT start, end, distance FROM distances")
    result = cursor.fetchall()
    return result
