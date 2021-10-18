# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:57:10 2021

@author: dvdvd
"""

# V3
# V3.1

from binance.client import Client              #added
from binance.enums import *                    #added

import BinanCode                               #added

class Racunanje:
    def __init__(self,config):
        self.MoneyInCashStart=config.Cash
        self.MoneyInCash=config.Cash
        self.MoneyInvested=0
        self.Value=config.Cash
        self.ValueBHStart=0
        self.ValueBHEnd=0
        self.MoneyBH=config.Cash
        self.InvestedBH=0
        self.GainSMAMoney=0
        self.GainSMAPercent=0
        self.GainBHMoney=0
        self.GainBHPercent=0
        self.GainDifferenceMoney=0
        self.GainDifferencePercent=0
        self.NumOfTrans=0    
        self.NumWriten=0 
        
        self.RealFee=0                              # Added real fee
        self.NumBought=0                            # Added 
        self.TotalFees=0                            # Added
    
    def calculateSMAValue(self,data,ulaz):
        
        helpData=data.iloc[-ulaz.SMAWindow:,1]   #da stavimo sum za kolonu umesto fo
        ukupno=helpData.sum()
        smaValue=ukupno/ulaz.SMAWindow
        
        return smaValue
        
    def calculateSign(self,price,smaValue, lastSign):      #v3
        difference=price-smaValue        
        if (difference<0):
            sign="-"
        elif (price == smaValue):
            sign = lastSign
        else:
            sign="+"
        return sign
    
    ######################################################################################################################################################################### #V3.1
    def CalculateSignNotChanged(self,price,dataSMA,ulaz, binan):             #added
        
        bnbBalance = binan.RetriveBNB()
        usdtBalance = binan.RetriveUSDT()
        
        self.Value = usdtBalance + bnbBalance * price         #changed
        
        
    def CalculateBuy(self,price,ulaz, binan):                                  #added
        
        
        
        self.RealFee=0
                      
        
        self.MoneyInCash = binan.RetriveUSDT()                      #added
                   
        self.NumBought = binan.kupi                                 #added
                              
        
        
        
            
        self.MoneyInvested = self.NumBought*price  
    
        self.RealFee=ulaz.Fee/100*self.MoneyInvested               
        self.TotalFees = self.TotalFees + self.RealFee
              
        
        
        self.MoneyInCash = binan.RetriveUSDT()                      # chaged
        bnbBalance = binan.RetriveBNB()
        self.Value = bnbBalance * price + self.MoneyInCash  #changed
        self.NumOfTrans+=1
        
        
        
        
    def CalculateSell(self,price,ulaz, binan):                                     #added
        self.RealFee=0
        
        self.MoneyInvested = binan.prodaj * price                               #changed
        
        
        self.RealFee=ulaz.Fee/100*self.MoneyInvested                
        self.TotalFees = self.TotalFees + self.RealFee  
        
        self.MoneyInCash = binan.RetriveUSDT()                                     #changed
        #self.MoneyInvested = 0
        bnbBalance = binan.RetriveBNB()
        self.Value = bnbBalance * price + self.MoneyInCash                      #changed
        self.NumOfTrans+=1
        
        

           


        
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
        
    def CalculateBH(self,ulaz,racunanje,dat):                                             #Ovo moze biti negde mnogo ranije, van klase da se ne bi svaki put izvrsavalo
        self.InvestedBH=ulaz.NumOfBuys*dat.iloc[ulaz.SMAWindow-1,1]
        self.MoneyBH=self.MoneyBH-self.InvestedBH-ulaz.Fee
        self.ValueBHStart=self.InvestedBH+self.MoneyBH
        
        self.MoneyBH=self.MoneyBH + ulaz.NumOfBuys*dat.iloc[-1,1]-ulaz.Fee
        self.InvestedBH=0
        self.ValueBHEnd=self.MoneyBH