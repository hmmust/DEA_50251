import pandas as pd
import json
import glob

conn_string = "postgresql://admin:admin@localhost:5433/fitdb"

files= glob.glob("./sample_data/retail_db/customers/*")
print(files)

s= open('./sample_data/retail_db/schemas.json')
schemas = json.load(s)
print(schemas['customers'])
customers_schema= schemas['customers']
customers_schema= sorted(customers_schema,key=lambda c:c['column_position'])
cols = [ i['column_name'] for i in customers_schema]
customers= pd.read_csv('./sample_data/retail_db/customers/part-00000',
                       names=cols)
customers.to_sql('customers',conn_string,index=False,if_exists='replace')
print(customers)