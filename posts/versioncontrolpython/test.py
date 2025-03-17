# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
import rich
from rich.pretty import pprint


import rich
from importlib.metadata import version

print('test.py is running')
print('version is :')
print(version('rich'))
