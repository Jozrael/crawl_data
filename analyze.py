import common
from os import listdir

def get_killers():
    for file in listdir('./morgues/'+common.username):
        with open('./morgues/'+common.username+'/'+file) as morgue_file:
            mf = morgue_file.read().splitlines()
            for index, line in enumerate(mf):
                if "Began as a " in line:
                    if "Was " in mf[index+1]:
                        common.print_block(mf, index+2)
                        break
                    else:
                        common.print_block(mf, index+1)
                        break

def get_class_race_deity_combos():

    return