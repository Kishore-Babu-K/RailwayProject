import mysql.connector

__cnx = None

def make_sql_connection():
  print("Making mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='stark', database='railwaydbs')

  return __cnx