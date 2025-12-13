import json
import pandas as pd
import numpy as np
import pyarrow.csv as pa

orders = pd.read_csv("orders.csv",
                        header=0,
                        encoding='utf-8',
                        sep=',',
                        engine='pyarrow')
orders= orders.iloc[:,1:]
orders= orders.astype({"order_date":str,'order_customer_id':str})
orders["order_date"] = pd.to_datetime(orders["order_date"],errors='coerce')
orders['order_customer_id'] = pd.to_numeric(orders['order_customer_id'],errors='coerce')
orders= orders.astype({"order_customer_id":np.int16})
print(orders.info())
