from html.parser import HTMLParser
from requests import get
import os
from common import username, server, mode

class linkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        if ".txt" in attrs[0][1]:
            self.links.append(attrs[0][1])

def compute_data_url():
    if server not in ["crawl.akrasiac.org","crawl.berotato.org"]:
        raise Exception("server needs to be crawl.akrasiac.org, or crawl.berotato.org")
    if mode not in ["original","one-line","compact"]:
        raise Exception("mode needs to be original, one-line, or compact")
    rawdata_url = ""
    if server == "crawl.akrasiac.org":
        rawdata_url = "http://"+server+"/rawdata/"+username+"/"
    elif server == "crawl.berotato.org":
        rawdata_url = "http://"+server+"/crawl/morgue/"+username+"/"
    return rawdata_url

def compute_necessary_pulls(rawdata_url):
    rawdata = str(get(rawdata_url).content)

    parser = linkParser()
    parser.links = []
    parser.feed(rawdata)

    #Always pull your latest, we'll assume it's changed.
    to_pull = [username+".txt"]

    for link in parser.links:
        if not os.path.isfile('./morgues/'+username+'/'+link):
            to_pull.append(link)
    return to_pull


def pull_data():
    rawdata_url = compute_data_url()
    
    to_pull = compute_necessary_pulls(rawdata_url)
    
    if not os.path.exists('./morgues/'+username+'/'):
        if not os.path.exists('./morgues/'):
            os.makedirs('./morgues/')
        os.makedirs('./morgues/'+username)
        
    for link in to_pull:
        morgue_file = str(get(rawdata_url+link).content.strip(),'utf-8')

        with open("./morgues/"+username+"/"+link, "w") as f:
            f.write(morgue_file)