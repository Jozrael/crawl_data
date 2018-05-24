from common import init
from pull_data import pull_data
import analyze

#Sets global variables 'username', 'server', and 'mode'
init("input.txt", "output.txt")

#Ensures we pull all newest morgue files, but only pull each file once.
pull_data()

#Run any analyzer functions you want here!
analyze.get_killers()
analyze.get_class_race_deity_combos()