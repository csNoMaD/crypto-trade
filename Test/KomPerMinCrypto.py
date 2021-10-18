# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:47:31 2021

@author: dvdvd
"""

class Komunikacija:
    
    def __init__(self,DataSMA):
        self.DataSMA=DataSMA
        
    def Step(self,ulaz,iterator,racunanje,DataSMA):       
        
        date=racunanje.data.iloc[ulaz.NumberOfDaysForTest + iterator,0]
        
        
        
        price=racunanje.data.iloc[ulaz.NumberOfDaysForTest + iterator,1]
        
        
        smaValue=racunanje.calculateSMAValue(iterator,ulaz,racunanje)
        
        if ((iterator > 1)):
            
            sign=racunanje.calculateSign(price, smaValue , DataSMA.iloc[iterator - 1 , 3])
        else:
            racunanje.MoneyInCashStart = price * 1.1
            racunanje.MoneyInCash = price * 1.1
            racunanje.Value = price * 1.1
            racunanje.MoneyBH = price * 1.1
            
            sign=racunanje.calculateSign(price, smaValue , None)
       
            
        DataSMA.loc[iterator]=[date,price,smaValue,sign]