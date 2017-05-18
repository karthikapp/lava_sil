import pandas as pd
import numpy as np
import json
from collections import defaultdict
results = defaultdict(lambda: defaultdict(dict))

def getFiscalYear(dt):
    year = dt.year
    if dt.month<4: year -= 1
    return year
df = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/all_invoice_with_prod.csv',skipinitialspace=True,converters={'Customer_id': lambda x: int(x), 'Invoice_no': lambda x: str(x).strip(), 'Invoice_dt': lambda x: str(x).strip(), 'Item_code': lambda x: str(x).strip(), 'Uom': lambda x: str(x).strip()})

df["Invoice_Date"] = pd.to_datetime(df['Invoice_Date'], format='%Y-%m-%d')
df["year"] = df['Invoice_Date'].dt.year
df["month"] = df['Invoice_Date'].dt.month
# print df
df = df[(df['Zone'] == 'Karnataka')  & (df['Item_code'] == 'BC100')]
# print df['Invoice_amt'].sum()
# revenue_by_year = df.groupby(pd.DatetimeIndex(df.Invoice_Date).shift(-3,freq='m').year)['Invoice_amt'].sum().astype('int64')
grouped = df.groupby(['Customer_id'])['Invoice_amt'].sum().to_string()

revenue_by_zone_product = df.groupby(['year','month'])['Qty'].sum().to_string()
# print revenue_by_customerid
# print grouped.reset_index().set_index(['Customer_id','year','Item_code','month']).sortlevel(0).to_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/test.csv')
print revenue_by_zone_product

# for index, row in revenue_by_customerid.iterrows():
# 	print row['Customer_id']

# # print revenue_by_year
# # print revenue_by_customerid
# r = revenue_by_customerid.reset_index().to_json(orient="index")
# parsed_json = json.loads(r.decode("utf-8","ignore"))
# print (json.dumps(parsed_json,indent=3))
