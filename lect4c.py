import json
import pandas as pd
import pyarrow.csv as pa

toleen = { "name":"Toleen Sarayrah",'Major':'DSAI','Age':22,
           'courses':['DEA','ML','ALGO']}

#to file (toleen.json) read/write text/binary
toleen_file = open('toleen.json',mode='wt' )
json.dump(toleen,toleen_file)
toleen_file.close()
