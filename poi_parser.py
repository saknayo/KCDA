# poi_parser.py

import json
import gzip
from pprint import pprint 
# test            1463988238722
ddir='battel_detail/'
fp=ddir+'1463981986467.json'
with open(fp,'r',encoding='utf-8')as f:
	dd=json.load(f)
	#pprint(dd)
fp=ddir+'1464404026885.json.gz'
with gzip.open(fp, 'rt',encoding='utf-8') as f:
    file_content = f.read()
    dd=json.loads(file_content)
