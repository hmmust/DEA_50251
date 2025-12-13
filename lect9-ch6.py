import json
import pandas as pd
import pyarrow.csv as pa

products = pd.read_csv("products.csv",
                        header=0,
                        encoding='utf-8',
                        sep=',',
                        engine='pyarrow')

#print(products.columns)
#products.columns= ['id', 'category_id', 'name','description', 'product_price']
products.rename(columns={"product_id":"id","product_name":"name"},inplace=True)
#products= products.iloc[:,[0,2,4,1,3]]
products= products.loc[:,['id','name','product_price','product_category_id','product_description']]
print(products.columns)
