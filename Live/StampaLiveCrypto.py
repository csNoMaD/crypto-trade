# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:57:24 2021

@author: dvdvd
"""


#override

class Stampa:
    
    def PrintBuy(self, MoneyInCash, MoneyInvested, Value,price,date,ulaz,NumBought,RealFee):
        print("We bought " + str(NumBought) + " stocks\crypto for a price of: " + str(price))
        print("We payed : $" + str(RealFee) + " In Fees")
        print("On a date :" + str(date))
        
        print("We invested: " + str(MoneyInvested))
        print("We have: " + str(MoneyInCash) + "$ left ")
        print("Total value of our investment is: " + str(Value))
        print("")
        
        
    def PrintSell(self, MoneyInCash, MoneyInvested, Value, price,date,RealFee):
        print("We sold for a price of: " + str(price))       
        print("We payed : $" + str(RealFee) + " In Fees")                        
        print("On a date :" + str(date))
        
        print("We have: " + str(MoneyInCash) + "$ now ")        
        print("")
        
    def PrintEnd(self,GainSMAMoney,GainSMAPercent,GainBHMoney,GainBHPercent,GainDifferenceMoney,GainDifferencePercent,NumOfTrans):
        print("")
        print("")
        print("")
        print("Using SIMPLE MOVING AVERAGE indicator we made a profit of " + str(GainSMAMoney) + "$")
        print("Valueo of our investment have risen for  " + str(GainSMAPercent) + "%")
        print("We made  " + str(NumOfTrans) + " Transactions")
        print("")
        print("")
        print("")
        #print("Using BUY AND HOLD tactic we made a profit of " + str(GainBHMoney) + "$")
        #print("Valueo of our investment have risen for  " + str(GainBHPercent) + "%")
        print("")
        print("")
        print("")
        #print("Using SIMPLE MOVING AVERAGE indicator we made " + str(GainDifferenceMoney) + "$ more/less then with BUY AND HOLD tactic")
        #print("Valueo of our investment have risen " + str(GainDifferencePercent) + "% more/less")
        print("")
        print("")
        print("")
        
    def PrintPriceTime(self,price,dt_string,SMA, sign):
        print('')
        print('Price: ' + dt_string + " is: " + str(price) + " SMAValue: " + str(round(SMA,2)) + ' Sign: ' + sign) #override
        print('')