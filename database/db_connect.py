from dotenv import load_dotenv
import pymysql
import os

load_dotenv()


def connect():
    host = os.environ.get("HOST")
    user = os.environ.get("USER")
    password = os.environ.get("PASSWORD")
    db = os.environ.get("DBNAME")

    env_variables_defined = host and user and password and db

    if env_variables_defined:
        return pymysql.connect(host=host,
                               port=25060,
                               user=user,
                               password=password,
                               database=db,
                               cursorclass=pymysql.cursors.DictCursor)

    else:
        raise KeyError('Some necessary environment variable(s) are not defined')



