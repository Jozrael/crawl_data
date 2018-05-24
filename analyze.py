import common
from os import listdir

def get_files(pattern, callback_function):
    for file in listdir('./morgues/'+common.username):
        with open('./morgues/'+common.username+'/'+file) as morgue_file:
            mf = morgue_file.read().splitlines()
            for index, line in enumerate(mf):
                if pattern in line:
                    callback_function(mf, index)
                    break

def callback_get_killers(morgue_file, index):
    if "Was " in morgue_file[index+1]:
        common.print_block(morgue_file, index+2)
    else:
        common.print_block(morgue_file, index+1)

def get_killers():
    get_files("Began as a", callback_get_killers)

def get_class_race_deity_combos():

    return