import json
import pandas as pd
import pyarrow.csv as pa

customers = pd.read_csv("customers.csv", engine='pyarrow')
customers['customer_fullname'] = customers['customer_fname'] + " " + customers['customer_lname']
customers.drop(['customer_fname','customer_lname'],axis=1, inplace=True)
customers.to_csv('customers_filtered.csv',index=False)
customers.to_json('customers_filtered.json',index=False,orient="records")

print(customers)