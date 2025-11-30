import pandas as pd
import json
import glob

conn_string = "postgresql://admin:admin@localhost:5433/fitdb"

s= open('./sample_data/retail_db/schemas.json')
schemas = json.load(s)
def get_column_names(schemas,ds):
    ds_schema= schemas[ds]
    ds_schema= sorted(ds_schema,key=lambda c:c['column_position'])
    cols = [ i['column_name'] for i in ds_schema]
    return cols
for s in schemas:
    cols = get_column_names(schemas,s)
    files= glob.glob(f"./sample_data/retail_db/{s}/*")
    print("loading schema:",s)
    for f in files:
        print("\tloading file:", f)
        df= pd.read_csv(f,names=cols)
        df.to_sql(s,conn_string,index=False,if_exists='append')
print("loading completed!")

