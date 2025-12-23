import json
import pandas as pd
import numpy as np
products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        )
products['product_price_total'] = (products['product_price']
                                   .map(lambda p: p+p*0.16))
products['product_price_check'] = (products['product_price']
                                   .map(lambda p: True if p>=100 else False))
print(products)