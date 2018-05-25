import common
import re
from os import listdir
from collections import Counter

def get_files(pattern, callback_function):
    for file in listdir('./morgues/'+common.username):
        with open('./morgues/'+common.username+'/'+file) as morgue_file:
            mf = morgue_file.read().splitlines()
            for index, line in enumerate(mf):
                if pattern in line:
                    callback_function(mf, index)
                    break

def get_killers():
    get_files("Began as a", callback_get_killers)

def callback_get_killers(morgue_file, index):
    if "Was " in morgue_file[index+1]:
        common.write_output(common.print_block(morgue_file, index+2))
    else:
        common.write_output(common.print_block(morgue_file, index+1))

def get_class_race_deity_combos():
    global cdr_data
    cdr_data = []
    get_files("Began as a", callback_crd_combos)
    cnt = Counter()
    for combo in cdr_data:
        cnt[combo[0] + " "+combo[1] + " of "+combo[2]] += 1
    for combo, count in cnt.most_common():
        common.write_output(combo + ": " + str(count)+'\n')

def callback_crd_combos(morgue_file, index):
    char_class_race = re.search('Began as (a|an) (.*) on ', morgue_file[index].strip()).group(2)
    char_class = char_class_race.split(" ")[0]
    char_race = char_class_race[char_class_race.find(" ")+1:]
    char_deity = "None"
    if "Was " in morgue_file[index+1]:
        char_deity = re.search('(.*) of (.*).', morgue_file[index+1].strip()).group(2)
    cdr_data.append([char_class,char_race,char_deity])