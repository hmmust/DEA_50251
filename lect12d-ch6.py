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
random_orders = orders.sample(10)
random_orders2 = orders.sample(10)
random_orders_all = pd.concat([random_orders, random_orders2],axis=0)
print(random_orders_all)
