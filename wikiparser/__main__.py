# -*- encoding: utf-8 -*-

import sys  
import wikiparser.pageparser as pp
import wikiparser.database as db

def main():
    
    # create database 
    #conn = db.create_database()
    

    # parse stuff
    pp.download_word("Brot")

    # see what's in the database
    print ('\n'*2)
    db.print_database()
    print ('\n'*2)

    #get records
    records = db.get_all_records()
    for i in records:
       print ("\n"*2)
       print (i[0])
       print ("\n"*2)
       print (i[1])
       print ("\n"*2)
       print (i[2][:500])
       print ("\n"*2)
       print ("="*50)
    

if __name__ == "__main__":
    main()