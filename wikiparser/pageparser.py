# -*- encoding: utf-8 -*-

import re
import json
import urllib
import codecs
import wikiparser.database as db
from urllib.parse import quote  
from urllib.request import urlopen


wiki_site = site = 'https://de.wiktionary.org'
wiki_options = '/w/api.php?action=parse&format=json&prop=wikitext&disabletoc=&page='

def parse_wiki_page(word):
    x = {}
    word_uri = quote(word)
    url = wiki_site+wiki_options+word_uri
    print ("URL: {0}".format(url))
    url_fixed = urlopen(url)
    reader = codecs.getreader("utf-8")
    json_obj = json.load(reader(url_fixed))
    
    if 'error' in json_obj:
       return None
    elif 'parse' in json_obj:
       return (json_obj['parse']['title'], json_obj['parse']['pageid'], json_obj['parse']['wikitext']['*'])


def download_word(word):
    if not db.word_exists(word):
        res = parse_wiki_page(word)
        if res:
            db.add_word_to_db(res)
        else:
            print ('Word "{0}" doesn\'t exist!'.format(word))
    else:
        print ('Word {0} already exists in the database!'.format(word))
