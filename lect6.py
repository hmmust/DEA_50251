import pandas as pd

conn_string = "postgresql://admin:admin@localhost:5433/fitdb"
orders= pd.read_sql("orders",conn_string)
print(orders)
query_1 = "select order_date, sum(order_item_subtotal)  from orders inner join order_items on order_id = order_item_order_id group by order_date"
order_grouped = pd.read_sql_query(query_1,conn_string)
order_grouped.to_csv("./orders_by_date.csv")
print(order_grouped)