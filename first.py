import pandas as pd
import numpy as np
import json
import time
from collections import defaultdict

# results = defaultdict(lambda: defaultdict(dict))
# print results
df = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/test.csv',skipinitialspace=True)
prod = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/prod.csv',skipinitialspace=True)
grouped = df.groupby(['Customer_ID','Product_Code','month_year'])["SO_BTN_Qty"].sum()



year = ['2014','2015','2016','2017']
year_month = ['01','02','03','04','05','06','07','08','09','10','11','12']
product_id = prod['Product_code'].unique().tolist()
customer_id = df['Customer_ID'].unique().tolist()
ym = []
for y in year:
	for m in year_month:
		ym.append(m+y)
start = time.time()
# print customer_id
res = []
for customer in customer_id:
	for product in product_id:
		print product,customer
		fdf = df[(df['Product_Code'] == product) & (df['Customer_ID'] == customer)]
		time.sleep( 1 )
		# print product,customer
		# print fdf
		consumption = []
		for yms in ym:
			for index, row in fdf.iterrows():
				if int(yms) == row["month_year"]:
					print "found"
					quantity = row["SO_BTN_Qty"]
				else:
					quantity = 0
				consumption.append(quantity)
		res.append(str(customer) + "-" + str(product)+ "-" + str(consumption))
		

end = time.time()
elapsed = end - start
print elapsed
print res
filepath = '/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/res.txt'
with open(filepath, 'w') as file_handler:
    for item in res:
        file_handler.write("{}\n".format(item))