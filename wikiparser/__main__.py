import sys  
import wikiparser.pageparser as pp

def main():
    
    page = pp.parse_wiki_page("über")
    if page:
        print (page['title'])
        print (page['pageid'])
        #print (page['wikitext'])
    else:
        print ('error')
    
    
if __name__ == "__main__":
    main()