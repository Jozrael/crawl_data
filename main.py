from common import init
from pull_data import pull_data
from analyze import get_killers
import requests
import os
from lxml.html import parse

#Sets global variables 'username', 'server', and 'mode'
init("input.txt", "output.txt")

#Ensures we pull all newest morgue files, but only pull each file once.
pull_data()

get_killers()