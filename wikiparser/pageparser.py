# -*- encoding: utf-8 -*-

import re
import json
import urllib
import codecs
from urllib.parse import quote  
from urllib.request import urlopen

wiki_site = site = 'https://de.wiktionary.org'
wiki_options = '/w/api.php?action=parse&format=json&prop=wikitext&disabletoc=&page='

def parse_wiki_page(word):
    x = {}
    word_uri = quote(word)
    url = wiki_site+wiki_options+word_uri
    print ("URL: %s" %url)
    url_fixed = urlopen(url)
    reader = codecs.getreader("utf-8")
    json_obj = json.load(reader(url_fixed))
    
    if 'error' in json_obj:
       return None
    elif 'parse' in json_obj:
       x['title'] = json_obj['parse']['title']
       x['pageid'] = json_obj['parse']['pageid']
       x['wikitext'] = json_obj['parse']['wikitext']['*']
       return x


