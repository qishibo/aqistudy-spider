# encoding: utf-8
# merge json files to a single file
import os
import sys
import json

os.chdir('json')
dirs = os.listdir()
dirs.sort()

all = []

for i in dirs:
    if os.path.splitext(i)[1] == ".json":
        with open(i, 'r') as f:
            month_data = json.load(f)
            all += month_data['data']['items']

with open('../views/all.js', 'w') as f:
    f.write('var global_all = ')
    f.write(json.dumps(all))