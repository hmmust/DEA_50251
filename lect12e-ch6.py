import json
from datetime import datetime
import pandas as pd
import numpy as np
from pandas import to_datetime
#inside the pipeline if datafame is too large, read chucks and tranform then load to databases
orders = pd.read_csv("orders.csv",
                        header=0,
                        encoding='utf-8',
                        chunksize=500
                        )
orders_chucks = []
for records in orders:
    orders_chucks.append(records)

orders = pd.concat(orders_chucks,axis=0)
print(orders)