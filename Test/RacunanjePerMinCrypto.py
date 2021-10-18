# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:42:35 2021

@author: dvdvd
"""


import pandas as pd



class Racunanje:
    def __init__(self,konf):
        self.MoneyInCashStart = konf.Cash
        self.MoneyInCash=konf.Cash
        self.MoneyInvested=0
        self.Value=konf.Cash
        self.ValueBHStart=0
        self.ValueBHEnd=0
        self.MoneyBH=konf.Cash
        self.InvestedBH=0
        self.GainSMAMoney=0
        self.GainSMAPercent=0
        self.GainBHMoney=0
        self.GainBHPercent=0
        self.GainDifferenceMoney=0
        self.GainDifferencePercent=0
        self.NumOfTrans=0
        self.data=pd.DataFrame()
        
        self.RealFee=0                              # Added real fee
        self.NumBought=0                            # Added 
        self.TotalFees=0                            # Added                                
    
    def calculateSMAValue(self,iterator,ulaz,racunanje):
        
        helpData=racunanje.data.iloc[ulaz.NumberOfDaysForTest + 1 - ulaz.SMAWindow + iterator : ulaz.NumberOfDaysForTest + 1 + iterator, 1]   #da stavimo sum za kolonu umesto fo
        ukupno=helpData.sum()
        smaValue=ukupno/ulaz.SMAWindow
        
        return smaValue
        
    def calculateSign(self,price,smaValue , lastSign):
        difference=price-smaValue        
        if (difference<0):
            sign="-"
        elif (price == smaValue):
            sign = lastSign
        else:
            sign="+"
        return sign
    
    
    def CalculateSignNotChanged(self,price,dataSMA,ulaz):
        self.MoneyInvested = self.NumBought*price               #Changed
        self.Value = self.MoneyInCash + self.MoneyInvested
        
        
    def CalculateBuy(self,price,ulaz):
        
        
            
            
        self.NumBought=self.MoneyInCash/price * 0.995               #added
        self.NumBought = round(self.NumBought,3)
        
            
        self.MoneyInvested = self.NumBought*price  
        
        #probaj sa fixnim feejem
        self.RealFee=ulaz.Fee/100*self.MoneyInvested                #added
        self.TotalFees = self.TotalFees + self.RealFee
              
        self.MoneyInCash = self.MoneyInCash - self.MoneyInvested - self.RealFee
        self.Value = self.MoneyInvested + self.MoneyInCash
        self.NumOfTrans+=1
        
        
            
        
    def CalculateSell(self,price,ulaz):
        
        self.RealFee=0
        
        self.MoneyInvested = self.NumBought*price
        
        self.RealFee=ulaz.Fee/100*self.MoneyInvested                #added
        self.TotalFees = self.TotalFees + self.RealFee  
        
        self.MoneyInCash = self.MoneyInCash + self.MoneyInvested - self.RealFee
        self.MoneyInvested = 0
        self.Value = self.MoneyInvested + self.MoneyInCash
        self.NumOfTrans+=1

        self.RealFee=0    
        
    def CalculateGainSMA(self):
        self.GainSMAMoney=self.Value-self.MoneyInCashStart        
        self.GainSMAMoney=round(self.GainSMAMoney, 2)
        
        
        
        if self.Value == self.MoneyInCashStart:
            self.GainSMAPercent = 0
            
        try:
            self.GainSMAPercent = (abs(self.Value - self.MoneyInCashStart) / self.MoneyInCashStart) * 100.0            
            self.GainSMAPercent=round(self.GainSMAPercent, 2)
        
        except ZeroDivisionError:
            self.GainSMAPercent = float('inf')
            


            
    def CalculateGainBH(self):
        self.GainBHMoney=self.ValueBHEnd-self.ValueBHStart
        self.GainBHMoney=round(self.GainBHMoney, 2)
        
        
        
        if self.ValueBHEnd == self.ValueBHStart:
            self.GainBHPercent = 0
        
        try:
            self.GainBHPercent = (abs(self.ValueBHEnd - self.ValueBHStart) / self.ValueBHStart) * 100.0
            self.GainBHPercent = round(self.GainBHPercent, 2)
        
        except ZeroDivisionError:
            self.GainBHPercent = float('inf')
            
            
            
    def CalculateDifference(self):
        self.GainDifferenceMoney=self.GainSMAMoney-self.GainBHMoney
        self.GainDifferenceMoney = round(self.GainDifferenceMoney, 2)
        
        self.GainDifferencePercent=self.GainSMAPercent-self.GainBHPercent
        self.GainDifferencePercent = round(self.GainDifferencePercent, 2)   
        
    def CalculateBH(self,ulaz,racunanje):                                             #Ovo moze biti negde mnogo ranije, van klase da se ne bi svaki put izvrsavalo
        self.InvestedBH=ulaz.NumOfBuys*racunanje.data.iloc[ulaz.NumberOfDaysForTest,1]
        
        BHfee=ulaz.Fee/100*self.InvestedBH  
        
        self.MoneyBH=self.MoneyBH-self.InvestedBH-BHfee
        self.ValueBHStart=self.InvestedBH+self.MoneyBH
        
        self.MoneyBH=self.MoneyBH + ulaz.NumOfBuys*racunanje.data.iloc[-1,1]-BHfee
        self.InvestedBH=0
        self.ValueBHEnd=self.MoneyBH