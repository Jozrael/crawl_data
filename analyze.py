from common import print_block, username, mode
from os import listdir

def get_killers():
    for file in listdir('./morgues/'+username):
        with open('./morgues/'+username+'/'+file) as morgue_file:
            mf = morgue_file.read().splitlines()
            for index, line in enumerate(mf):
                if "Began as a " in line:
                    if "Was " in mf[index+1]:
                        print_block(mf, index+2, mode)
                        break
                    else:
                        print_block(mf, index+1, mode)
                        break

def get_class_race_deity_combos(username):

    return