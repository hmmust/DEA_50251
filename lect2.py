import json
import pandas as pd
import pyarrow.csv as pa
#pd.read_json()
customers_f= open("customers_filtered.json")
customers= json.load(customers_f)
customers_df = pd.DataFrame(customers)
print(customers_df)