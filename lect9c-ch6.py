import json
import pandas as pd
import numpy as np
import pyarrow.csv as pa

products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        sep=',',
                        engine='pyarrow')
products['price_category'] = np.where(products['product_price']>100,'Expensive','Cheap')
conditions = [
                products['product_price']<100,
                ((products['product_price']>=100) & (products['product_price']<1000) ),
                products['product_price']>=1000
                ]
options = [
                'cheap',
                'expensive',
                'very expensive'
                ]
products['price_category'] = np.select(conditions,options,default='Unknown')
print(products['price_category'].value_counts())