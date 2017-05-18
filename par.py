import multiprocessing
import pandas as pd
import numpy as np
import json
import time
from collections import defaultdict

# split a list into evenly sized chunks
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
df = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/test.csv',skipinitialspace=True)
customer_id = df['Customer_ID'].unique().tolist()[:2]
# customer_id = [8226,1186,24848,20178,19839,8689,1254]


def do_job(job_id, customer_id):
        # results = defaultdict(lambda: defaultdict(dict))
    # print results
    df = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/test.csv',skipinitialspace=True)
    grouped = df.groupby(['Customer_ID','Product_Code','month_year'])["SO_BTN_Qty"].sum()



    year = ['2014','2015','2016','2017']
    year_month = ['01','02','03','04','05','06','07','08','09','10','11','12']
    ym = ['012014','022014','032014','042014','052014','062014','072014','082014','092014','102014','112014','122014','012015','022015','032015','042015','052015','062015','072015','082015','092015','102015','112015','122015','012016','022016','032016','042016','052016','062016','072016','082016','092016','102016','112016','122016','012017','022017']
    product_id = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/data/item_codes.csv',skipinitialspace=True)["Item Code"].tolist()
    customer_id = customer_id
    # ym = []
    # for y in year:
    #   for m in year_month:
    #       ym.append(m+y)

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
                #   # print type(int(yms)),type(row["month_year"])
                #   if int(yms) == row["month_year"]:
                #       condition = int(yms) == row["month_year"]
                #       print "found"
                #       quantity = row["SO_BTN_Qty"]
                #   else:
                #       condition = int(yms) == row["month_year"]
                #       quantity = 0
                    
            #   consumption.append((str(quantity) + "-" + str(yms) + str(condition) + str(int(yms))+  "-" + str(row["month_year"])))
            res.append(str(customer) + "~" + str(product)+ "~" + str(consumption))
            end = time.time()
            elapsed = end - start
            print elapsed
    filepath = '/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/res'+str(job_id)+'.txt'
    with open(filepath, 'w') as file_handler:
        for item in res:
            file_handler.write("{}\n".format(item))
            


def dispatch_jobs(data, job_number):
    total = len(data)
    chunk_size = total / job_number
    slice = chunks(data, chunk_size)
    jobs = []

    for i, s in enumerate(slice):
        j = multiprocessing.Process(target=do_job, args=(i, s))
        jobs.append(j)
    for j in jobs:
        j.start()


if __name__ == "__main__":
    data = customer_id
    dispatch_jobs(data, 3)
    
    # filepath = '/home/bharath/Desktop/dem/lavazza_pred/env/bin/res1.csv'
    # with open(filepath, 'w') as file_handler:
    #     for item in res:
    #         file_handler.write("{}\n".format(item))