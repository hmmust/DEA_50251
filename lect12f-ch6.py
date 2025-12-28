import json
from datetime import datetime
import pandas as pd
import numpy as np
from pandas import to_datetime
#inside the pipeline if datafame is too large, read chucks and tranform then load to databases
orders = pd.read_csv("orders.csv",
                        header=0,
                        encoding='utf-8')
customers = pd.read_csv("customers.csv",
                        header=0,
                        encoding='utf-8')
orders_customers = pd.merge(orders, customers, how='left', left_on= 'order_customer_id' ,right_on='customer_id',)
print(orders_customers.groupby(['customer_city','order_date'])['customer_id'].aggregate('count'))