# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 03:49:53 2021

@author: dvdvd
"""

    # notif
    
    
import telegram_send

class Notif:

    def NotificationSell(self,price, RealFee, date, MoneyInCash):
            
            message = "We sold for a price of: $" + str(round(price,3)) + '\n' + "We payed : $" + str(round(RealFee,3)) + " In Fees" + '\n' "On a date :" + str(date) + '\n' + "We have: $" + str(round(MoneyInCash,3)) + " now "
            
            telegram_send.send(messages=[message])
            
            
            
    def NotificationBuy(self,NumBought,price,RealFee,date,MoneyInvested,MoneyInCash,Value):
            
            message = "We bought " + str(NumBought) + " stocks\crypto" + '\n' + "For a price of: $" + str(round(price,3)) + '\n' "We payed : $" + str(round(RealFee,3)) + " In Fees" + '\n' + "On a date :" + str(date) + '\n' + "We invested: $" + str(round(MoneyInvested,3)) + '\n' + "We have: $" + str(round(MoneyInCash,3)) + " left " + '\n' + "Total value of our investment is: $" + str(round(Value,3))
                        
            
            
            
            telegram_send.send(messages=[message])