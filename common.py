from os import remove

def init(in_file, out_file):
    global username
    global mode
    input_file = open(in_file)
    username = input_file.readline().split("=",1)[1].strip()
    server = input_file.readline().split("=")[1].strip()
    mode = input_file.readline().split("=")[1].strip()
    if server not in ["crawl.akrasiac.org","crawl.berotato.org"]:
        raise Exception("server needs to be crawl.akrasiac.org, or crawl.berotato.org")
    if mode not in ["original","one-line","compact"]:
        raise Exception("mode needs to be original, one-line, or compact")
    rawdata_url = ""
    if server == "crawl.akrasiac.org":
        rawdata_url = "http://"+server+"/rawdata/"+username+"/"
    elif server == "crawl.berotato.org":
        rawdata_url = "http://"+server+"/crawl/morgue/"+username+"/"
    remove(out_file)
    return rawdata_url

def print_block(morgue_file_lines, starting_index):
    output = ""
    while True:
        output += morgue_file_lines[starting_index].strip()
        if mode in ["original", "compact"]:
            output += "\n"
        if mode == "compact":
            break
        if morgue_file_lines[starting_index][len(morgue_file_lines[starting_index])-1] in ['.','!']:
            output += "\n"
            break
        starting_index += 1
    with open("output.txt", "a") as o:
            o.write(output)