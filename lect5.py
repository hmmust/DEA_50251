import pandas as pd

customers = pd.read_parquet("customers.parquet",
                            columns=['customer_fname'])
customers = pd.read_parquet("customers.parquet",
                            filters=[['customer_city','==','San Marcos']])
print(customers)