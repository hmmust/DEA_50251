import json
import pandas as pd
import numpy as np
products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        )
def cal_tax(price):
    return price+price*0.16

products['product_price_total'] = (products['product_price']
                                   .map(cal_tax))
#products['product_name2'] = products['product_name'].map(str.upper)
categories = {1:"A",2:"B",3:"C"}
products['category'] = products["product_category_id"].map(categories,na_action='ignore')
print(products)