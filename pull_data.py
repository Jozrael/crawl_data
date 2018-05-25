from html.parser import HTMLParser
import os
from requests import get

import common

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        if ".txt" in attrs[0][1]:
            self.links.append(attrs[0][1])

def compute_data_url():
    if common.server not in ["crawl.akrasiac.org", "crawl.berotato.org"]:
        raise ValueError("server needs to be crawl.akrasiac.org, or crawl.berotato.org")
    if common.mode not in ["original", "one-line", "compact"]:
        raise ValueError("mode needs to be original, one-line, or compact")
    rawdata_url = ""
    if common.server == "crawl.akrasiac.org":
        rawdata_url = "http://"+common.server+"/rawdata/"+common.username+"/"
    elif common.server == "crawl.berotato.org":
        rawdata_url = "http://"+common.server+"/crawl/morgue/"+common.username+"/"
    return rawdata_url

def compute_necessary_pulls(rawdata_url):
    rawdata = str(get(rawdata_url).content)

    parser = LinkParser()
    parser.links = []
    parser.feed(rawdata)

    #Always pull your latest, we'll assume it's changed.
    to_pull = [common.username+".txt"]

    for link in parser.links:
        if not os.path.isfile('./morgues/'+common.username+'/'+link):
            to_pull.append(link)
    return to_pull


def pull_data():
    rawdata_url = compute_data_url()

    to_pull = compute_necessary_pulls(rawdata_url)

    #Make sure there's a landing zone for the pulled morgue files.
    if not os.path.exists('./morgues/'+common.username+'/'):
        if not os.path.exists('./morgues/'):
            os.makedirs('./morgues/')
        os.makedirs('./morgues/'+common.username)

    #Pull and write em
    for link in to_pull:
        morgue_file = str(get(rawdata_url+link).content.strip(), 'utf-8')

        with open("./morgues/"+common.username+"/"+link, "w") as f:
            f.write(morgue_file)
