import pandas as pd
import numpy as np
import json
df2014 = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/2014_outward_derived.csv')
df2015 = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/2015_outward_derieved.csv')
df2016 = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/2016_outward_derieved.csv')
df2017 = pd.read_csv('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/2017_outward_derieved.csv')
df2014 = df2014[['Product Code','Product Desc']]
df2015 = df2015[['Product Code','Product Desc']]
df2016 = df2016[['Product Code','Product Desc']]
df2017 = df2017[['Product Code','Product Desc']]
df_all = df2014.append([df2015,df2016,df2017], ignore_index=True).drop_duplicates()
j = df_all[['Product Code','Product Desc']]
i = j[j['Product Code'] != 0].reset_index().to_json(orient='records')
print i
parsed_json = json.loads(i.decode("utf-8","ignore"))
print (json.dumps(parsed_json,indent=3))
with open('/Users/karthikappadurai/Desktop/Lavazza_pred/env/bin/data/product_master.json', 'w') as outfile:
    json.dump(parsed_json, outfile)


