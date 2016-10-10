import sys  
import wikiparser.pageparser as pp
import wikiparser.database as db
import mwparserfromhell

def main():
        
    data_base = db.connect_to_database("../database.db")
    words = db.get_all_words(data_base, "words")

    all_records = db.get_all_records(data_base, 'words')
    
    db.print_records(data_base, "words", 10000)
    print (words)
    
    word = []
    page = pp.parse_wiki_page("über")
    if page:
        word.append(page['title'])
        word.append(page['pageid'])
        word.append(page['wikitext'])
        db.insert_word_data(data_base, "words", word)
    else:
        print ('error')

    text = word[2]
    wikicode = mwparserfromhell.parse(text)
    sections = wikicode.get_sections()
    for s in sections:
        print (s)
    db.close_connection(data_base)
    
if __name__ == "__main__":
    main()