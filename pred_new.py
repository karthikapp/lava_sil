import multiprocessing
import pandas as pd
import numpy as np
import json
import time
from collections import defaultdict
import ast
import json
from pprint import pprint
from pandas import ExcelWriter
import xlsxwriter

filtered = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/predicted_all_1605.csv',skipinitialspace=True, sep=',')
filtered['consumption'] = filtered['Consumption'].apply(lambda x: ast.literal_eval(x))
filtered['predicted'] = filtered['prediction'].apply(lambda x: ast.literal_eval(x)[-2:])
filtered['actual_feb'] = filtered['consumption'].apply(lambda x: (x)[35])
filtered['actual_jan'] = filtered['consumption'].apply(lambda x: (x)[34])
filtered['pred_march'] = filtered['predicted'].apply(lambda x: int((x)[0]))
filtered['pred_april'] = filtered['predicted'].apply(lambda x: int((x)[1]))

print "jan"
ddf_jan = filtered.groupby(['prod_desc','Product_ID','customer_branch'])['actual_jan'].sum().to_frame()
ddf_jan.to_excel('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/output_actual_jan.xls')

print "feb"
ddf_feb = filtered.groupby(['prod_desc','Product_ID','customer_branch'])['actual_feb'].sum().to_frame()
ddf_feb.to_excel('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/output_actual_feb.xls')

print "march"
ddf_march = filtered.groupby(['prod_desc','Product_ID','customer_branch'])['pred_march'].sum().to_frame()
ddf_march.to_excel('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/output_pred_march.xls')

print "april"
ddf_april = filtered.groupby(['prod_desc','Product_ID','customer_branch'])['pred_april'].sum().to_frame()
ddf_april.to_excel('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/output_rpred_april.xls')