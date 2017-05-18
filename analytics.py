import pandas as pd
import numpy as np
import json

with open('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/customer_master.json') as data_file:    
    data = json.load(data_file)
    # print data

with open('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/product_master.json') as product_data_file:    
    product_data = json.load(product_data_file)


# function to return customer zone
def return_customer_zone(customerid):
	for item in data:
		if customerid == item['Customer ID']:
			return item['Zone']

# function to return customer name
def return_customer_name(customerid):
	for item in data:
		if customerid == item['Customer ID']:
			return item['Customer/SE']

# function to return customer name
def return_customer_branch(customerid):
	for item in data:
		if customerid == item['Customer ID']:
			return item['Branch']

# function to return customer zone
def return_product_descr(productid):
	for item in product_data:
		if productid == item['Product Code']:
			return item['Product Desc']



df = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/all_invoice.csv',skipinitialspace=True,converters={'Customer_id': lambda x: int(x), 'Invoice_no': lambda x: str(x).strip(), 'Invoice_dt': lambda x: str(x).strip(), 'Item_code': lambda x: str(x).strip(), 'Uom': lambda x: str(x).strip()})
df["Invoice_Date"] = pd.to_datetime(df['Invoice_dt'], format='%d.%m.%Y')
df = df.drop_duplicates()
def getFiscalYear(dt):
    year = dt.year
    if dt.month<4: year -= 1
    return year


df["week"] = df['Invoice_Date'].dt.week
df["year"] = df['Invoice_Date'].dt.year
df['financial_year'] = pd.DatetimeIndex(df.Invoice_Date).shift(-3,freq='m').year
df['Zone'] = df['Customer_id'].map(lambda x: return_customer_zone(x))
df['Branch'] = df['Customer_id'].map(lambda x: return_customer_branch(x))
df['Customer_Name'] = df['Customer_id'].map(lambda x: return_customer_name(x))
df['Product_Description'] = df['Item_code'].map(lambda x: return_product_descr(x))
df = df[['Customer_id','Invoice_no','Uom','Qty','Invoice_amt','Invoice_Date','Zone','Branch','Customer_Name','Product_Description','Item_code']]
df.to_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/all_invoice_with_prod.csv',sep=',', encoding='utf-8')


# print df
# revenue_by_year = df.groupby(pd.DatetimeIndex(df.Invoice_Date).shift(-3,freq='m').year)['Invoice_amt'].sum().astype('int64')
# grouped = df.groupby(df['Invoice_Date'].apply(getFiscalYear))['Invoice_amt'].sum().astype('int64')
# revenue_by_customerid = df.groupby(['Customer_id','year'])['Invoice_amt'].sum().astype('int64').reset_index().to_json(orient='records')
# # print revenue_by_year
# print grouped
