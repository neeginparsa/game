import sqlite3
from tkinter import *
from tkinter import messagebox


try:
    connection = sqlite3.connect("account.db")
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS accountlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        family TEXT,
        username TEXT UNIQUE,
        password TEXT
    );

    """
    cursor.execute(query)
    cursor.close()
    connection.commit()
except sqlite3.Error as err:
    print(err)
finally:
    if connection:
        connection.close()




def savedata(name,family,username,password):
    try:
            
        connection = sqlite3.connect("account.db")
        cursor = connection.cursor()

        query = """
        INSERT INTO accountlist (name,family,username,password)
        VALUES (?,?,?,?);
        """
        
        
        val = (name,family,username,password)       
        cursor.execute(query ,val)
        cursor.close()
        connection.commit()
    except sqlite3.Error as err:
        return False
    else:
        return True
    finally:
        if connection:
            connection.close()

        
    
    
    