# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:57:32 2021

@author: dvdvd
"""

 #DV
 
 #V3.1
 
class Signal:
    
    
    
    def BuySignal(self,racunanje, price,ulaz,stampa,date,binan,notif):
        
        binan.buy(racunanje, price, date)                               #V3.1
        #racunanje.CalculateBuy(price,ulaz, binan)                                                                                                          #V3.1 
        #stampa.PrintBuy(racunanje.MoneyInCash,racunanje.MoneyInvested,racunanje.Value,price,date,ulaz,racunanje.NumBought,racunanje.RealFee)               #V3.1 
        #notif.NotificationBuy(racunanje.NumBought,price,racunanje.RealFee,date,racunanje.MoneyInvested,racunanje.MoneyInCash,racunanje.Value)              #DV
        
    def SellSignal(self,racunanje, price,ulaz,stampa,date,binan,notif):
        
        binan.sell(racunanje , date , price)                                    #V3.1
        #racunanje.CalculateSell(price,ulaz, binan)                                                                                                         #V3.1 
        #stampa.PrintSell(racunanje.MoneyInCash,racunanje.MoneyInvested,racunanje.Value,price,date,racunanje.RealFee)                                       #V3.1                                        
        #notif.NotificationSell(price, racunanje.RealFee, date, racunanje.MoneyInCash)                                                              #DV
        
        
        
    def EndSIgnal(self,racunanje,stampa):
        racunanje.CalculateGainSMA()
        
        #racunanje.CalculateGainBH()
        
        #racunanje.CalculateDifference()
        
        stampa.PrintEnd(racunanje.GainSMAMoney,racunanje.GainSMAPercent,racunanje.GainBHMoney,racunanje.GainBHPercent,racunanje.GainDifferenceMoney,racunanje.GainDifferencePercent,racunanje.NumOfTrans)