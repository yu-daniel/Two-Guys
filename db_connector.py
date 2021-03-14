import pymysql.cursors
import os

host = os.environ.get('HOST', None)
user = os.environ.get('USER', None)
passwd = os.environ.get('PASSWORD', None)
db = os.environ.get('DB', None)

print("HOST = ", host)
print("USER = ", user)
print("PASSWORD = ", passwd)
print("DB = ", db)

def connect_to_database(host=host, user=user, passwd=passwd, db=db):
    """connects to a database and returns a database objects"""
    db_connection = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
    return db_connection


def execute_query(db_connection=None, query=None, query_params=()):
    """
    executes a given SQL query on the given db connection and returns a Cursor object
    db_connection: a MySQLdb connection object created by connect_to_database()
    query: string containing SQL query
    returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
    You need to run .fetchall() or .fetchone() on that object to actually access the results.
    """

    if db_connection is None:
        return None

    if query is None or len(query.strip()) == 0:
        return None

    cursor = db_connection.cursor()

    '''
    params = tuple()
    #create a tuple of parameters to send with the query
    for q in query_params:s
        params = params + (q)
    '''
    cursor.execute(query, query_params)
    db_connection.commit()
    return cursor


if __name__ == '__main__':
    db = connect_to_database()