import requests
from bs4 import BeautifulSoup

def print_block(morgue_file_lines, starting_index, mode):
    if mode not in ["original","one-line","compact"]:
        raise Exception("mode needs to be original, one-line, or compact")
    output = ""
    while True:
        output += morgue_file_lines[starting_index].strip()
        if mode == "original":
            output += "\n"
        if mode == "compact":
            break
        if morgue_file_lines[starting_index][len(morgue_file_lines[starting_index])-1] in ['.','!']:
            output += "\n"
            break
        starting_index += 1
    print(output)



def get_killers(filename, morgue_file_lines, mode):
    for index, line in enumerate(morgue_file_lines):
        if "2018" in line:
            if "Was " in morgue_file_lines[index+1]:
                print_block(morgue_file_lines, index+2, mode)
                break
            else:
                print_block(morgue_file_lines, index+1, mode)
                break

input_file = open("input.txt")
username = input_file.readline().split("=",1)[1].strip()
server = input_file.readline().split("=")[1].strip()
mode = input_file.readline().split("=")[1].strip()
rawdata_url = "http://"+server+"/rawdata/"+username+"/"
rawdata_page = requests.get(rawdata_url)
rawdata_soup = BeautifulSoup(rawdata_page.content, 'html.parser')
rawdata_links = rawdata_soup.find_all('a')
morgue_file_urls = []

for link in rawdata_links:
    if ".txt" in link.get("href"):
        morgue_file_urls.append(link.get("href"))
        
        #For testing purposes :)
        #break

morgue_files = {}
for url in morgue_file_urls:
    morgue_file = requests.get(rawdata_url+url)

    morgue_files[url] = str(morgue_file.content.strip(),'utf-8')

for url in morgue_files:
    get_killers(url, morgue_files[url].splitlines(), mode)