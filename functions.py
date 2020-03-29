# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 12:26:06 2020

@author: krzys
"""

import pandas as pd
from matplotlib import pyplot as plt 

class Datasets:
    boston = 'data/Boston.csv'
    credit = 'data/Credit.csv'
    def __str__(self):
        return 'Dostępne datasety: boston, credit'

def import_data(path=Datasets.boston):
    data = pd.read_csv(path)
    return data
    
    
def plot_hist(df,column=None):
    
    if not column:
        column = df.columns[0]
        
    plt.hist(df[column])
    plt.title(column)


