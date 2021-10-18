# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:43:44 2021

@author: dvdvd
"""

class Stampa:
    
    def PrintBuy(self, MoneyInCash, MoneyInvested, Value,price,date,ulaz,NumBought,RealFee):
        print("We bought " + str(NumBought) + " stocks\crypto for a price of: " + str(price))
        print("We payed : $" + str(RealFee) + " In Fees")
        print("On a date and time :" + str(date))
        
        print("We invested: " + str(MoneyInvested))
        print("We have: " + str(MoneyInCash) + "$ left ")
        print("Total value of our investment is: " + str(Value))
        print("")
        
        
    def PrintSell(self, MoneyInCash, MoneyInvested, Value, price,date):
        print("We sold for a price of: " + str(price))                               
        print("On a date and time :" + str(date))
        
        print("We have: " + str(MoneyInCash) + "$ now ")        
        print("")
        
    def PrintEnd(self,GainSMAMoney,GainSMAPercent,GainBHMoney,GainBHPercent,GainDifferenceMoney,GainDifferencePercent,TotalFees):
        print("")
        print("")
        print("")
        print("Using SIMPLE MOVING AVERAGE indicator we made a profit of " + str(GainSMAMoney) + "$")
        print("Valueo of our investment have risen for  " + str(GainSMAPercent) + "%")
        print("On Fees we spent : $" + str(TotalFees))
        print("")
        print("")
        print("")
        print("Using BUY AND HOLD tactic we made a profit of " + str(GainBHMoney) + "$")
        print("Valueo of our investment have risen for  " + str(GainBHPercent) + "%")
        print("")
        print("")
        print("")
        print("Using SIMPLE MOVING AVERAGE indicator we made " + str(GainDifferenceMoney) + "$ more/less then with BUY AND HOLD tactic")
        print("Valueo of our investment have risen " + str(GainDifferencePercent) + "% more/less")
        print("")
        print("")
        print("")