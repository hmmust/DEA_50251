import json
import pandas as pd
import pyarrow.csv as pa

customers = pd.read_csv("customers.csv",
                        header=0,
                        encoding='utf-8',
                        sep=',',
                        engine='pyarrow')
print(customers.dtypes,customers.shape)
print(customers.head(6)) #default 5
print(customers.tail(10)) #default 5
print(customers.sample(10)) #default 1
print(customers.info())
print(customers.describe())
print(customers.describe(include=['object']))



