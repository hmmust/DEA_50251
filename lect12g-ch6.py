import json
from datetime import datetime
import pandas as pd
import numpy as np
from pandas import to_datetime

products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8')
#products['product_price'] = products['product_price'].mask(products['product_price'] > 100, 100)
products['product_category'] = pd.cut( products['product_price'],bins=[0,100,200,300,400,500,600],
                                       labels=[0,100,200,300,400,500])
products['product_category_encoded'],_ = pd.factorize( products['product_category'])
products = pd.get_dummies( products,columns = ['product_category'])

print(products)
