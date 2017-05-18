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

df = pd.read_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/data/noida.csv',skipinitialspace=True, sep=',')
df["Consumption"] = df.apply(lambda x: [x.Jan2017, x.Feb2017,x.Mar2017,x.Apr2017 ], axis=1)
# writer = ExcelWriter('output_new_1605.xlsx')
df['prediction'] = df['Consumption'].apply(lambda x: triple_exponential_smoothing(x, 2, 0.616, 0.029, 0.993, 2))
df['predicted'] = df['prediction'].apply(lambda x: (x)[-2:])
print df[["predicted","Consumption"]].to_string()
df['predicted_may'] = df['predicted'].apply(lambda x: (abs(int((x)[0])+ int(x[0]))/2))
df['predicted_june'] = df['predicted'].apply(lambda x: (abs(int((x)[1])+ int(x[1]))/2))
print df[["prediction","predicted_may","predicted_june"]].to_string()
ddf = df[["Item Code","Item Description","predicted_may","predicted_june"]]
print ddf.to_string()
ddf.to_csv('/Users/karthikappadurai/Desktop/lavazza_pred_siva/env/bin/noida_pred.csv')
