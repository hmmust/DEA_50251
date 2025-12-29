import json
from datetime import datetime

import pandas
import pandas as pd
import numpy as np
from pandas import to_datetime

orders = pd.read_csv("orders.csv",
                        header=0,
                        encoding='utf-8',
                        )
orders['order_date']= pd.to_datetime(orders['order_date'],errors='coerce')
orders['is_order_id_duplicated'] = orders.duplicated(subset='order_id', keep='first')
orders['is_order_date_duplicated'] = orders.duplicated(subset='order_date', keep='first')
orders['is_order_id_date_duplicated'] = orders.duplicated(subset=['order_id','order_date'], keep='first')

orders.drop_duplicates(subset='order_id', keep='first', inplace=True)
print(orders)

print(orders['order_id'].value_counts())
print(orders['order_date'].value_counts())


