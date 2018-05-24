from common import print_block
from os import listdir

def get_killers(mode,username):
    for file in listdir('./morgues/'+username):
        with open('./morgues/'+username+'/'+file) as morgue_file:
            mf = morgue_file.read().splitlines()
            for index, line in enumerate(mf):
                if ", 20" in line:
                    if "Was " in mf[index+1]:
                        print_block(mf, index+2, mode)
                        break
                    else:
                        print_block(mf, index+1, mode)
                        break