import os
import re

for _file in os.listdir('.'):
    if re.search('\d{5}\.txt$', _file):
        os.remove(_file)