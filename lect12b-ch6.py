import json
from datetime import datetime

import pandas
import pandas as pd
import numpy as np
from pandas import to_datetime

products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        )
random_indices = np.random.randint(0, len(products),size=20)
products.loc[random_indices, 'product_price'] = np.nan
print(products.isnull().sum())
print(products['product_price'].isnull().sum())

#products['product_price'].fillna(0, inplace=True)
#products['product_price'].fillna( products['product_price'].mean(), inplace=True)
#products['product_price'].fillna( method='ffill', inplace=True)
#products['product_price'].fillna( method='bfill', inplace=True)
#products['product_price'].ffill(inplace=True)
#products['product_price'].bfill(inplace=True)
products.pop('product_description')
products.dropna(inplace=True, axis=0)

print(products.count())

