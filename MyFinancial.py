# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:44:32 2020

@author: ascroggins
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MyFinancial:
    def __init__ (self, name):
        self._name = name
        self._df = None
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def __str__(self):
        return "Name: " + str(self._name)
    
    def payment(self,rate_per_year,num_periods, amount):
        payment = np.pmt(rate_per_year/100/12, num_periods*12, amount)
        return payment
    def futurevalue(self, rate_per_year, years, orig_investment):
        fv = np.fv(rate_per_year/100,years,0,orig_investment)
        return fv
    def presentvalue(self, rate_per_year, years,future_value):
        pv = np.pv(rate_per_year/100,years,0,future_value)
        return pv
    
    def analysis(self, file):
       df = pd.read_csv(file,index_col=0,parse_dates=True)
       self._df = df
       df.plot(y='Close')
       plt.ylabel('Closing Price')
       plt.show
 
       
       
if __name__ == '__main__':

    fin = MyFinancial("alec")
    print(fin)

    payment = fin.payment(7,36,10000)
    print(payment)
    
    future_value = fin.futurevalue(7, 10,1000)
    print(future_value)
    
    presentvalue = fin.presentvalue(7,10,1967.15)
    print(presentvalue)
    
    graph = fin.analysis('AAPL.csv')
    