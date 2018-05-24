from common import parse_input
from pull_data import pull_data
from get_killers import get_killers
import requests
import os
from lxml.html import parse

username, rawdata_url, mode = parse_input("input.txt", "output.txt")

#Ensures we pull all newest morgue files, but only pull each file once.
pull_data(rawdata_url, username)

get_killers(mode,username)