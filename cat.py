import pandas  as pd
import numpy as np
df1 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res0.txt', sep='~')
df2 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res1.txt', sep='~')
df3 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res2.txt', sep='~')
df4 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res3.txt', sep='~')
df5 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res4.txt', sep='~')
df6 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res5.txt', sep='~')
df7 = pd.read_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/res6.txt', sep='~')


# df4 = df4[[ 'Item_code','Item_desc']]
# df4['Item_Code'] = df4['Item_code']
# df4['Item_desc'] = df4['Item_desc']
# df4 = df4[[ 'Item_Code','Item_desc']]

# # df3 = df3[[ 'Item_code','Item_desc']]
# df3['Item_Code'] = df3['Product Code']
# df3['Item_desc'] = df3['Product Desc']
# df3 = df3[[ 'Item_Code','Item_desc']]

# df2['Item_Code'] = df2['Product Code']
# df2['Item_desc'] = df2['Product Desc']
# df2 = df2[[ 'Item_Code','Item_desc']]

# df1['Item_Code'] = df1['Product Code']
# df1['Item_desc'] = df1['Product Desc']
# df1 = df1[[ 'Item_Code','Item_desc']]

newdf = df1.append([df2,df3,df4,df5,df6,df7], ignore_index=True)

newdf.to_csv('/home/bharath/Desktop/dem/lavazza_pred/env/bin/newres.csv', sep='~')
