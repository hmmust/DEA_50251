import json
import pandas as pd
import numpy as np
products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        )
products.sort_values(by=['product_price'],inplace=True)
products.sort_values(by=['product_price'],ascending=False,inplace=True)
products.sort_values(by=['product_price','product_id'],
                     ascending=False,inplace=True)
products.sort_values(by=['product_price','product_id'],
                     ascending=[False,True],inplace=True)
products['product_price_rank']= (products['product_price'].
                                 rank(method='first',ascending=True))

print(products)
print(products.nsmallest(10,'product_price'))
print(products.nlargest(10,'product_price'))