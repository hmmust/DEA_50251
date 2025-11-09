import requests
import pandas as pd

customers_file = requests.get('https://raw.githubusercontent.com/hmmust/PDSSection3_20242/refs/heads/main/customers.json')
if customers_file.status_code==200:
    print(customers_file.content) #string
    customers_json= customers_file.json()
    customers_df = pd.DataFrame(customers_json)
    print(customers_df)