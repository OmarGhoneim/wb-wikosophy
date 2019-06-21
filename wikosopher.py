import requests
from bs4 import BeautifulSoup
import regex
import time

def get_to_philosophy(url, cache = []):

    #saved for later to detect any loop
    cache.append(url)

    #names of certain classes and ids to be removed (red, external, /link/, [link], footnote, country coordinates)
    excluded_classes = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    excluded_ids = ["coordinates"]

    #avioding heavy load
    time.sleep(0.5)

    #make a request, get the response text and bs nested data structure
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt, 'lxml')

    #flag to indicate articles with no wikilinks
    no_wikilinks = True

    #find all paragraphs in the needed class, exclude all unwanted classes and ids, remove italic tags and parentheses
    for p in soup.find(class_ = 'mw-parser-output').find_all('p', recursive = False):
        for c in p.find_all(class_ = excluded_classes):
            c.extract()
        for i in p.find_all(id = excluded_ids):
            i.extract()
        p = BeautifulSoup(regex.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(p)), features="lxml")
        for italic in p.find_all('i'):
            italic.extract()
        #continue untill finding the first link in an edited paragraph and only then toggle the flag off
        try:
            link_suffix = p.a.get('href')
        except:
            continue
        no_wikilinks = False
        break

    #assign the next full link unless having reached a dead end page
    if(no_wikilinks):
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
        link = "https://en.wikipedia.org" + link_suffix
        print(link)

    #the fuction calls itself over again untill getting to philosophy or detecting a loop from a previous link
    if(link == "https://en.wikipedia.org/wiki/Philosophy"):
        print("Wikosopher found it, Just as expected !")
        return link
    elif(link in cache):
        print("Stuck in a loop !")
        return link
    else:
        return(get_to_philosophy(link, cache))


#try it with a random Wikipidia article
random_url = "https://en.wikipedia.org/wiki/Special:Random"
get_to_philosophy(random_url)
