import requests
import pandas as pd
from io import StringIO

products_file = requests.get('https://raw.githubusercontent.com/hmmust/PDSSection3_20242/refs/heads/main/products.csv')
if products_file.status_code==200:
    #print(customers_file.content) #string
    products_df = pd.read_csv(StringIO(products_file.text))
    print(products_df)