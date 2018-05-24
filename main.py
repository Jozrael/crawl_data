from common import init, username, mode
from pull_data import pull_data
from analyze import get_killers
import requests
import os
from lxml.html import parse

rawdata_url = init("input.txt", "output.txt")

#Ensures we pull all newest morgue files, but only pull each file once.
pull_data(rawdata_url)

get_killers()