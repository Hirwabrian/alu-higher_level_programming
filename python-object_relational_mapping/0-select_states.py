#!/usr/bin/python3
#Script to list all states from the database hbtn_0e_0_usa.
import sys
import MySQLdb

def list(username, password, database):
    """
    Function to list all states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    c = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY id ASC")
    for state in c.fetchall():
        print(state)

        # Close the cursor and database connection
        c.close()
        db.close()
