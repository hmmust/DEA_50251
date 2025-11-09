import json
import pandas as pd
import pyarrow.csv as pa

toleen = { "name":"Toleen Sarayrah",'Major':'DSAI','Age':22,
           'courses':['DEA','ML','ALGO']}

toleen_json= json.dumps(toleen)
print(toleen_json)
students = [
    { "name":"Toleen Sarayrah",'Major':'DSAI','Age':22,
           'courses':['DEA','ML','ALGO']},
     { "name":"Rana ALhindi",'Major':'DSAI','Age':21,
           'courses':['DEA','ML','BDA']}
]

students_json= json.dumps(students)
print(students_json)