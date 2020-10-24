# -*- coding: utf-8 -*-

import wikiparser.db_low as db
import os
from os.path import expanduser
from os.path import exists


def create_database():    
    if create_db_folder(install_path):
        # folder created
        if db.create_database(db_path):
            # database created
            if create_tables(db_path, table_name):
                # tables created
                pass
    else:
        # folder already exists
        if db.create_database(db_path):
            # database created
            if create_tables(db_path, table_name):
                # tables created
                pass
        else:
            # database already exists
            if table_exists(db_path, table_name):
                # table already exists
                pass
            else:
                # table does not exist
                if create_tables(db_path, table_name):
                    # tables created
                    pass

    print ("All done!") 
    return db_path


def create_db_folder(the_path):
    if not exists(the_path):
        os.makedirs(the_path)
        print ("Database folder created at: {0}".format(the_path))
        return True
    else:      
        print ("Database folder already exists at: {0} !".format(the_path))
        return None

def get_install_path():
    home = expanduser("~")
    db_folder = "/.wikiparser"
    return home+db_folder

def create_tables(db_path, table_name):
    conn = db.connect_to_database(db_path)
    db.create_table(conn, table_name)
    print ('Table "{0}" created sucessfully'.format(table_name))
    db.close_connection(conn)
    return True

def table_exists(db_path, table_name):
    conn = db.connect_to_database(db_path)
    if db.has_table(conn, table_name):
        db.close_connection(conn)
        return True
    return None

def add_word_to_db(word):
    conn = db.connect_to_database(db_path)
    db.insert_word_data(conn, table_name, word)
    print ("Word '{0}' inserted sucessfully!".format(word[0]))
    db.close_connection(conn)

def word_exists(word):
    print (db_path)
    conn = db.connect_to_database(db_path)
    if db.word_exists(conn, table_name, word):
        db.close_connection(conn)
        return True
    db.close_connection(conn)
    return False

def print_database():
    conn = db.connect_to_database(db_path)
    words = db.get_all_words(conn, table_name)
    print ("Existing words")
    print ("="*20)
    for word in words:
        print (word+", ",end='')
    print ("\n")
    db.close_connection(conn)

def get_all_records():
    conn = db.connect_to_database(db_path)
    records = db.get_all_records(conn, table_name)
    db.close_connection(conn)
    return records


    
db_name = 'wiki_database.db'
install_path = get_install_path()
db_path = install_path+"/"+db_name
table_name = "words"

