import sqlite3

class DBOperations:
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    con.execute("create table lang (id integer primary key, name varchar unique)")


class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None
 
    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self
 
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()