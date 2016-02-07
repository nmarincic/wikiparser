# -*- encoding: utf-8 -*-

import re
import json
import urllib
import codecs
import urlparse

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)
    
    
def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts))
        

def parse_wiki_page(word):
    x = {}
    url = wiki_site+wiki_options+word
    uri = iriToUri(url)
    print "URL: %s" %uri
    url_fixed = urllib.urlopen(uri)
    json_obj = json.loads(url_fixed.read())
    
    if 'error' in json_obj:
       return None
    elif 'parse' in json_obj:
       x['title'] = json_obj['parse']['title']
       x['pageid'] = json_obj['parse']['pageid']
       x['wikitext'] = json_obj['parse']['wikitext']['*']
       return x


wiki_site = site = 'https://de.wiktionary.org'
wiki_options = '/w/api.php?action=parse&format=json&prop=wikitext&disabletoc=&page='
word = u"Hund"

#lines = codecs.open(words_file, "r", "utf-8")

page = parse_wiki_page(word)

if page:
    print page['title']
else:
    print 'error'
