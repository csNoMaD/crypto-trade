# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:33:40 2021

@author: dvdvd
"""



import pandas as pd
import re


class Config:                                                         # Ubacio period
    def __init__(self):
                 self.Fee=0
                 self.Data=pd.DataFrame()
                 self.SMAWindowStart=0
                 self.SMAWindowEnd=0
                 self.PeriodStart=0
                 self.PeriodEnd=0
                 self.BrojVrednosti=0
                 self.NumberOfDaysForTest=0
                 self.path=''
                 self.Cash=0
                 self.PeriodKorak=0
                 self.NumOfBuys=0
                 
                 
    def read(self):
        with open(r"E:\David\Fax\Praksa\Code\PerMinCryptoFee\configFee.txt", "r+") as file:
    
            List = file.readlines()
            ListOfNumbers = []
            
            path = List[10]
            path = path[30: -1: ]
            
            for i in range(0,10):
                Numbers = re.findall(r'\d+(?:\.\d+)?', List[i]) 
                ListOfNumbers.extend(Numbers)
            
            #print(ListOfNumbers)   
          
            Fee, SMAWindowStart, SMAWindowEnd, PeriodStart, PeriodEnd,PeriodKorak, BrojVrednosti, NumberOfDaysForTest, Cash, NumOfBuys = ListOfNumbers
            
            self.Fee = float(Fee)
            self.SMAWindowStart = int(SMAWindowStart)
            self.PeriodStart = int(PeriodStart)
            self.SMAWindowEnd = int(SMAWindowEnd)
            self.PeriodEnd = int(PeriodEnd)
            self.BrojVrednosti = int(BrojVrednosti)
            self.NumberOfDaysForTest = int(NumberOfDaysForTest)
            self.Cash = float(Cash)
            self.PeriodKorak = int(PeriodKorak)
            self.NumOfBuys = float(NumOfBuys)
            self.path=path
            
            