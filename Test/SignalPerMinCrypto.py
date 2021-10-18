# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:46:32 2021

@author: dvdvd
"""

class Signal:
    
    
    
    def BuySignal(self,racunanje, price,ulaz,stampa,date):
        racunanje.CalculateBuy(price,ulaz)
        #stampa.PrintBuy(racunanje.MoneyInCash,racunanje.MoneyInvested,racunanje.Value,price,date,ulaz,racunanje.NumBought,racunanje.RealFee)
        
        
    def SellSignal(self,racunanje, price,ulaz,stampa,date):
        racunanje.CalculateSell(price,ulaz)
        #stampa.PrintSell(racunanje.MoneyInCash,racunanje.MoneyInvested,racunanje.Value,price,date)
        
    def EndSIgnal(self,racunanje,stampa):
        racunanje.CalculateGainSMA()
        
        racunanje.CalculateGainBH()
        
        racunanje.CalculateDifference()
        
        stampa.PrintEnd(racunanje.GainSMAMoney,racunanje.GainSMAPercent,racunanje.GainBHMoney,racunanje.GainBHPercent,racunanje.GainDifferenceMoney,racunanje.GainDifferencePercent,racunanje.TotalFees)