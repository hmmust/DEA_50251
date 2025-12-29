import json
import pandas as pd
import numpy as np
orders = pd.read_csv("orders.csv",
                        header=0,
                        encoding='utf-8',
                        )


print(orders.groupby(['order_customer_id','order_status']).count())