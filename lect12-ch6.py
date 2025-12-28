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
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders_by_status = orders.groupby(['order_status'])
print(orders_by_status['order_id'].count())
print(orders_by_status['order_id'].aggregate(['count','sum']))
print(orders_by_status.aggregate({
    "order_date":['min','max'],
    "order_id":['count','sum']}
))

orders['order_month'] = orders['order_date'].dt.strftime('%m-%Y')
orders_by_month_status = orders.groupby(['order_status','order_month'])
print(orders_by_month_status.aggregate({"order_date":['count']}))
