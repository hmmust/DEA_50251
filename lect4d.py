import json
import pandas as pd
import pyarrow.csv as pa

customers = pd.read_csv("customers.csv", engine='pyarrow')
customers.to_parquet('customers.parquet',compression='snappy')
print(customers)