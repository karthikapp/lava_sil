import pandas as pd
import numpy as np
import json
import time
from collections import defaultdict

# results = defaultdict(lambda: defaultdict(dict))
# print results
df = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/test.csv',skipinitialspace=True)
grouped = df.groupby(['Customer_ID','Product_Code','month_year'])["SO_BTN_Qty"].sum()



year = ['2014','2015','2016','2017']
year_month = ['01','02','03','04','05','06','07','08','09','10','11','12']
ym = ['012014','022014','032014','042014','052014','062014','072014','082014','092014','102014','112014','122014','012015','022015','032015','042015','052015','062015','072015','082015','092015','102015','112015','122015','012016','022016','032016','042016','052016','062016','072016','082016','092016','102016','112016','122016','012017','022017']
product_id = df['Product_Code'].unique().tolist()
customer_id = df['Customer_ID'].unique().tolist()[:20]
# ym = []
# for y in year:
# 	for m in year_month:
# 		ym.append(m+y)

# print customer_id
res = []
for customer in customer_id:
	start = time.time()
	for product in product_id:
		print product,customer
		fdf = df[(df['Product_Code'] == product) & (df['Customer_ID'] == customer)]
		# print product,customer
		# print fdf
		consumption = []
		for yms in ym:
			# time.sleep( 1 )
			
			# print fdf
			if len(fdf[fdf['month_year'] == int(yms)]) == 1:
				quantity = fdf[fdf['month_year'] == int(yms)]["SO_BTN_Qty"].values.tolist()[0]
			else:
				quantity = 0
			consumption.append(quantity)

			# for index, row in fdf.iterrows():
			# 	# print type(int(yms)),type(row["month_year"])
			# 	if int(yms) == row["month_year"]:
			# 		condition = int(yms) == row["month_year"]
			# 		print "found"
			# 		quantity = row["SO_BTN_Qty"]
			# 	else:
			# 		condition = int(yms) == row["month_year"]
			# 		quantity = 0
				
		# 	consumption.append((str(quantity) + "-" + str(yms) + str(condition) + str(int(yms))+  "-" + str(row["month_year"])))
		res.append(str(customer) + "," + str(product)+ "," + str(consumption))
		end = time.time()
		elapsed = end - start
		print elapsed
		


# print res
filepath = '/home/bharath/Desktop/dem/lavazza_pred/env/bin/res.csv'
with open(filepath, 'w') as file_handler:
    for item in res:
        file_handler.write("{}\n".format(item))

# 						# print yms
					
# 			# 		# time.sleep( 1 )
# 			# 		print yms
# 			# 		quantity = row["SO_BTN_Qty"]
# 			# 	else:
# 			# 		quantity = 0
# 			# 	time.sleep( 1 )
# 			# 	print yms,quantity

# 		# for index, row in df.iterrows():
# 		# 	if customer == row["Customer_ID"] and product == row["Product_Code"]:
# 		# 		consumption = []
# 		# 		# print customer, product
# 		# 		for yms in ym:
# 		# 			if int(yms) == row["month_year"]:
# 		# 				quantity = row["SO_BTN_Qty"]
# 		# 			else:
# 		# 				quantity = 0
# 		# 			print yms,quantity
# 		# 		consumption.append(quantity)
# 		# 	time.sleep( 1 )
# 		# 	print row
# 		# 	print "=========================================="
# 		# print product,consumption
# 			# 	print row
# 			# 	print "product and customer match"
# 			# 	consumption = []
# 			# 	for yms in ym:
# 			# 		if int(yms) == row["month_year"]:
# 			# 			quantity = row["SO_BTN_Qty"]
# 			# 		else:
# 			# 			quantity = 0
# 			# 		print yms,quantity
# 			# 	consumption.append(quantity)

# 			# print "=========================================="	
# 			# time.sleep( 1 )
# 			# 	print customer,product,consumption
# 			# 	res.append(str(customer) + "," + str(product)+ "," + str(consumption))
					



# # end = time.time()
# # elapsed = end - start
# # print elapsed
# # print res
# # filepath = '/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/res.csv'
# # with open(filepath, 'w') as file_handler:
# #     for item in res:
# #         file_handler.write("{}\n".format(item))




# # print product_id
# for index, row in df.iterrows():
# 	# for every product in product list
# 	for product in product_id:
# 		# crete an empty array
# 		consumption_list = []
# 		# if product code in row matches product code in for loop 
# 			if product == row['Item_code']:
# 				# loop 
# 				for m in month:
# 					if row['month'] == m:
# 						consumption_list.append(row['Qty'])
# 					else:
# 						consumption_list.append(0)
# 		print row['Customer_id'],product,consumption_list


