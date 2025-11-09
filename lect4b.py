import json
import pandas as pd
import pyarrow.csv as pa

toleen_json='{"name": "Toleen Sarayrah", "Major": "DSAI", "Age": 22, "married":false , "courses": ["DEA", "ML", "ALGO"]}'
toleen_object = json.loads(toleen_json) #dict
print(toleen_object['name'])