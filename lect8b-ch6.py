import json
import pandas as pd
import pyarrow.csv as pa

customers = pd.read_csv("customers.csv",
                        header=0,
                        encoding='utf-8',
                        sep=',',
                        engine='pyarrow')
print(customers.iloc[0:3,:])
print(customers.iloc[[0,1,3],:])
print(customers.iloc[0:3,0:2])
print(customers.iloc[0:3,[0,1]])
print(customers.loc[0:3,['customer_id','customer_fname']])
print(customers.at[0,'customer_id'])
print(customers.iat[0,0])
print(customers['customer_fname'])
customers['customer_married'] = False
customers['customer_fullname'] = customers['customer_fname']+ ' ' + customers['customer_lname']

customers['customer_serial'] = [ i for i in range(1,12436)]
#del customers['customer_married']
customers.pop(('customer_married'))
print(customers)
