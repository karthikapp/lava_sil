import pandas as pd
import numpy as np

import json
from pprint import pprint

with open('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/customer_master.json') as data_file:    
    data = json.load(data_file)
    # print data

def return_customer_zone(customerid):
	for item in data:
		if customerid == item['Customer ID']:
			return item['Zone']
	

	
print return_customer_zone(20073)