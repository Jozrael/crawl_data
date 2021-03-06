import common
import re
from os import listdir
from collections import Counter

def get_files(pattern, callback_function):
    for filename in listdir('./morgues/{}'.format(common.username)):
        with open('./morgues/{}/{}'.format(common.username, filename)) as morgue_file:
            mf = morgue_file.read().splitlines()
            for index, line in enumerate(mf):
                if pattern in line:
                    callback_function(mf, index)
                    break

def killers():
    get_files("Began as a", callback_get_killers)

def callback_get_killers(morgue_file, index):
    if "Was " in morgue_file[index+1]:
        common.write_output(common.print_block(morgue_file, index+2))
    else:
        common.write_output(common.print_block(morgue_file, index+1))

def class_race_deity_frequency():
    global crd_data
    crd_data = []
    get_files("Began as a", callback_crd_combos)
    cnt = Counter()
    for combo in crd_data:
        cnt["{} {} of {}".format(combo[0], combo[1], combo[2])] += 1
    for combo, count in cnt.most_common():
        common.write_output("{}: {}\n".format(combo, str(count)))

def callback_crd_combos(morgue_file, index):
    char_class_race = re.search('Began as (a|an) (.*) on ', morgue_file[index].strip()).group(2)
    char_class = char_class_race.split(" ")[0]
    char_race = char_class_race[char_class_race.find(" ")+1:]
    char_deity = "None"
    if "Was " in morgue_file[index+1]:
        char_deity = re.search('(.*) of (.*).', morgue_file[index+1].strip()).group(2)
    crd_data.append([char_class,char_race,char_deity])