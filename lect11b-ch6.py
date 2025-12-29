import json
import pandas as pd
import numpy as np
products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        )
def cal_tax(row):
    if row['product_category_id'] <50:
        return row['product_price']+row['product_price']*0.16
    else:
        return row['product_price'] + row['product_price'] * 0.1

products['product_price_total'] = products.apply(cal_tax,axis=1)
print(products)
print(products['product_price'].count())
print(products['product_price'].mean())