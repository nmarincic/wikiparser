# -*- coding: utf-8 -*-

import sqlite3
from os import remove as rm
from os.path import exists


class DatabaseError(Exception):
    pass
    
# DATABASE CREATION & MANAGEMENT
    
def create_database(path):
    if exists(path):
        message = "Database '%s' already exists. No databases created!" %path
        raise DatabaseError(message)
        return None
    else:
        sqlite3.connect(path)
        print ("Succesfully created the database '%s'." %path)
        return connect_to_database(path)
        
        
def connect_to_database(path):
    if exists(path):
        conn = sqlite3.connect(path)
        print ("Succesfully connected to the database '%s'" %path)
        return conn
    else:
        message = "Database '%s' does not exist. Cannot connect" %path
        raise DatabaseError(message)
        return None


def close_connection(db):
    db.close()
    print ("Connection to the database closed!")

def delete_database(path):
    if exists(path):
        rm(path)
        print ("Database '%s' deleted." %path)
    else:
        message = "Database '%s' does not exist" %path
        raise DatabaseError(message)


# TABLE CREATION & MANAGEMENT
          
def get_tables(conn):
    table_names = []
    cursor = conn.cursor()
    cursor.execute("select name from sqlite_master where type='table';")
    tables = cursor.fetchall()
    if tables == []:
        print ("No tables in the database!")
        return []
    for i in range(len(tables)):
        name = tables[i][0]
        table_names.append(name)
    return table_names

 
def has_table(conn, table_name):
    tables = get_tables(conn)
    if tables:
        if table_name in tables:
            print ("Table '%s' exists." %table_name)
            return tables 
    print ("Table '%s' doesn't exists." %table_name)
    return None


def create_tables(conn, table_name):
    if not has_table(conn, table_name):
        conn.execute('''create table %s
               (title    char(50) primary key  not null,
               page_id   char(10) not null,
               wikitext  text     not null
               );''' %table_name)
        print ("Table %s created sucessfully" %table_name)
        return conn


def print_tables(conn):
    tables = get_tables(conn)
    if tables:
        print ("Tables:")
        for table in tables:
            print (table)
                    
            
def drop_table(conn, tableName):
    if has_table(conn, tableName):
        cursor = conn.cursor()
        line = "DROP TABLE %s" %tableName
        cursor.execute(line)
        conn.commit()
        print ("Dropped table '%s'" %tableName)


def drop_all_tables(conn):
    tables = get_tables(conn)
    if tables:
        for table in tables:
            drop_table(conn, table)
        print ("All tables dropped!")

                   
# WORD MANAGEMENT

def word_exists(conn, table_name, word):
    line = "select exists(select 1 from %s where title=? limit 1)" %table_name
    cursor = conn.execute(line, (word,))
    result = cursor.fetchone()[0]
    if result==1:
        return True
    return False
    
                
def insert_word_data(conn, table_name, list):
    line = "insert into %s values (?,?,?)" %table_name
    conn.execute(line, (list[0], list[1], list[2]));
    conn.commit()
    print ("Records inserted successfully")


def update_word(conn, table_name, word):
    line = "update %s set page_id=?, wikitext=? where title=?" %table_name
    conn.execute(line, (word[1], word[2], word[0]))
    conn.commit()
    print ("Updated word: %s. Total number of rows deleted : %i" %(word[0],conn.total_changes))
            

def delete_word(conn, table_name, word):
    line = "delete from %s where title=?" %table_name
    conn.execute(line, (word,))
    conn.commit()
    print ("Deleted word: %s. Total number of rows deleted : %i" %(word,conn.total_changes))
    
    
def get_all_words(conn, table_name):
    words = []
    line = "select title from %s" %table_name
    cursor = conn.execute(line)
    for row in cursor:
       words.append(row[0])
    return words


# RECORD MANAGEMENT


def get_record(conn, table_name, word):
    line = "select title, page_id, wikitext  from %s where title=?" %table_name
    cursor = conn.execute(line, (word,))
    return cursor.fetchone()
    
    
def get_all_records(conn, table_name):
    records = []
    line = "select title, page_id, wikitext  from %s" %table_name
    cursor = conn.execute(line)
    return cursor.fetchall()
    

def delete_all_records(conn, table_name):
    cursor = conn.execute("DELETE from %s" %table_name)
    conn.commit()
    print ("All records deleted successfully")
    

def print_records(conn, table_name, limit):
    line = "select title, page_id, wikitext  from %s" %table_name
    cursor = conn.execute(line)
    for row in cursor:
       print ("title = ", row[0])
       print ("page_id = ", row[1])
       print ("wikitext = ", row[2][0:limit], "\n")