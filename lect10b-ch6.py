import json
import pandas as pd
import numpy as np
products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        )
print(products[( (products['product_price'] > 100)
                &  (products['product_category_id'] == 2) )])

print(products.query('product_price >100 and product_category_id ==2'))
print(products[  products['product_category_id'].isin([1,2])  ])
print(products[  products['product_name'].str.startswith("A")  ])