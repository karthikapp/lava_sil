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

with open('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/data/product_master.json') as data_file:    
    prod_data = json.load(data_file)
    
with open('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/data/customer_master.json') as data_file:    
    customer_data = json.load(data_file)
item_codes = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/data/item_codes.csv',skipinitialspace=True)["Item Code"].tolist()





def get_prod_desc(product_id):
    for value in prod_data:
        if value["Product Code"] == product_id:
            return value["Product Desc"]
    

def get_cust_desc(customer_id):
    for value in customer_data:
        if value["Customer ID"] == customer_id:
            return value["Customer/SE"]
       
def get_cust_branch(customer_id):
    for value in customer_data:
        if value["Customer ID"] == customer_id:
            return value["Branch"]

def get_cust_zone(customer_id):
    for value in customer_data:
        if value["Customer ID"] == customer_id:
            return value["Zone"]


df = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/new_res_16052017.csv',skipinitialspace=True, sep='~')



def weighted_average(series, weights):
    result = 0.0
    weights.reverse()
    for n in range(len(weights)):
        result += series[-n-1] * weights[n]
    return result


def exponential_smoothing(series, alpha):
    result = [series[0]] # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    return result
def double_exponential_smoothing(series, alpha, beta):
    result = [series[0]]
    for n in range(1, len(series)+1):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series): # we are forecasting
          value = result[-1]
        else:
          value = series[n]
        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)
    return result
def triple_exponential_smoothing(series, slen, alpha, beta, gamma, n_preds):
    result = []
    seasonals = initial_seasonal_components(series, slen)
    for i in range(len(series)+n_preds):
        if i == 0: # initial values
            smooth = series[0]
            trend = initial_trend(series, slen)
            result.append(series[0])
            continue
        if i >= len(series): # we are forecasting
            m = i - len(series) + 1
            result.append((smooth + m*trend) + seasonals[i%slen])
        else:
            val = series[i]
            last_smooth, smooth = smooth, alpha*(val-seasonals[i%slen]) + (1-alpha)*(smooth+trend)
            trend = beta * (smooth-last_smooth) + (1-beta)*trend
            seasonals[i%slen] = gamma*(val-smooth) + (1-gamma)*seasonals[i%slen]
            result.append(smooth+trend+seasonals[i%slen])
    return result
def initial_seasonal_components(series, slen):
    seasonals = {}
    season_averages = []
    n_seasons = int(len(series)/slen)
    # compute season averages
    for j in range(n_seasons):
        season_averages.append(sum(series[slen*j:slen*j+slen])/float(slen))
    # compute initial values
    for i in range(slen):
        sum_of_vals_over_avg = 0.0
        for j in range(n_seasons):
            sum_of_vals_over_avg += series[slen*j+i]-season_averages[j]
        seasonals[i] = sum_of_vals_over_avg/n_seasons
    return seasonals

def initial_trend(series, slen):
    sum = 0.0
    for i in range(slen):
        sum += float(series[i+slen] - series[i]) / slen
    return sum / slen

# weights = [0.1, 0.2, 0.3, 0.4]
# series = [36267,36207,41421,16233,18587,19995,20698,22144,22379,20917,20285,22441,18601,21584,22877,16323,19575,26874,29825,25398,29694,25978,32295,31191,28297,33497,34650,30554,30841,35513,36737,35974,35216,32776,35411,37703,27839,34474,34509,29493,25222,22918,16250,16229,13552,19489,15940,17056,1170,11882]
# # print exponential_smoothing(series, 0.5)
# # print weighted_average(series, weights)
# # print double_exponential_smoothing(series, alpha=0.9, beta=0.9)
# print triple_exponential_smoothing(series, 4, 0.616, 0.029, 0.993, 2)

writer = ExcelWriter('output_new_1605.xlsx')
df['prediction'] = df['Consumption'].apply(lambda x: triple_exponential_smoothing(ast.literal_eval(x), 4, 0.616, 0.029, 0.993, 3))
df['predicted'] = df['Consumption'].apply(lambda x: ast.literal_eval(x)[-2:])
print "predicting"
df['predicted_march'] = df['predicted'].apply(lambda x: (x)[0])
df['predicted_april'] = df['predicted'].apply(lambda x: (x)[1])
print "after predictions"
df['prod_desc'] = df['Product_ID'].apply(lambda x: get_prod_desc(x))
print "getting customer name"

df['customer_name'] = df['Customer_ID'].apply(lambda x: get_cust_desc(x))
print "getting customer branch"

df['customer_branch'] = df['Customer_ID'].apply(lambda x: get_cust_branch(x))
print "getting customer zone"

df['customer_zone'] = df['Customer_ID'].apply(lambda x: get_cust_zone(x))
filtered = df[df['Product_ID'].isin(item_codes)]
print "filtering products and writing csv"
filtered.to_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/predicted_all_1605.csv', encoding='utf-8')


ddf = filtered.groupby(['prod_desc','Product_ID','customer_branch'])['predicted_april'].sum().to_frame()
ddf.to_excel('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/output_new_1605.xls')
