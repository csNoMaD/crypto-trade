# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:42:43 2021

@author: dvdvd
"""

# V3 
#T
#V3.1

#ETH

import pandas as pd
from datetime import datetime

from binance.client import Client
from binance.enums import *

import BinanCode

import telegram_send                       #V3.1

class Binan:
    
    
    def __init__(self):
        
        self.balanceETH = 0                                     #ETH
        self.balanceUSDC = 0
        
        self.kupi=0
        self.prodaj=0
    
    def buy(self,racunanje, price, date):                       #V3.1
    
        client = Client(BinanCode.normal,BinanCode.sec)
        
        self.RetriveUSDC() 
        self.RetriveETH()                                           #ETH                              
        self.kupi = self.balanceUSDC / price * 0.98           #T
        self.kupi = 10000 / price * 0.98                     #T
        self.kupi=round(self.kupi,3)
        
        
        if (self.kupi >= 0.0001):
            
            order = client.create_test_order(                                                   #T
            symbol='ETHUSDC',                                                                   #ETH  
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            
            quantity=self.kupi
            )
            
            print('')
            print(order)
            print('')
            #V3.1
            print('WE BOUGHT')
            print('')
            
            #V3.1
            #ETH  
            message = "We bought " + str(self.kupi) + " ETH" + '\n' + "For a price of: $" + str(round(price,3)) + '\n' + "On a date :" + str(date) + '\n' + "We invested: $" + str(round(self.kupi * price,3)) + '\n' + "ETHbalance: " + str(round(self.balanceETH,3))  + '\n' + "USDCbalance: " + str(round(self.balanceUSDC,3)) + '\n'
            print(message)
            #telegram_send.send(messages=[message])                                                  #T
            #return order
            
        else:
            print('')
            print('cant buy less than 0.0001')
            print('')
        
        
        
        
    def sell(self,racunanje , date , price):      #V3.1
    
        client = Client(BinanCode.normal,BinanCode.sec)
        
        self.RetriveETH()                                               #ETH   
        self.RetriveUSDC()                               
        self.prodaj = 0.98 * self.balanceETH                        #T  
        #self.prodaj = 0.98 * 5                                       #T                    
        self.prodaj=round(self.prodaj,3)
        
        if (self.prodaj >= 0.0001):
            
            order = client.create_test_order(                                           #T
            symbol='ETHUSDC',                                                           #ETH  
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            
            quantity=self.prodaj
            )
            
            
            print('')
            print(order)
            print('')
            #V3.1
            print('WE SOLD')
            print('')
            
            #V3.1
            #ETH  
            message = "We sold " + str(self.prodaj) + " ETH" + '\n' + "For a price of: $" + str(round(price,3)) + '\n' + "On a date :" + str(date) + '\n' + "ETHbalance: " + str(round(self.balanceETH,3))  + '\n' + "USDCbalance: " + str(round(self.balanceUSDC,3)) + '\n'
            print(message)
            #telegram_send.send(messages=[message])                                             #T
            
            #return order
            
        else:
            print('')
            print('cant sell less than 0.0001')
            print('')
        
        
        
    def RetriveUSDC(self):                                                #added
        client = Client(BinanCode.normal,BinanCode.sec)
        
        self.balanceUSDC = client.get_asset_balance(asset='USDC')
        self.balanceUSDC=pd.DataFrame.from_dict(self.balanceUSDC.items())
        self.balanceUSDC=self.balanceUSDC.loc[self.balanceUSDC[0]=='free']
        self.balanceUSDC=self.balanceUSDC.iloc[0,1]
        self.balanceUSDC = float(self.balanceUSDC)
        self.balanceUSDC = round(self.balanceUSDC,3) 

        #return self.balanceUSDC                                                                #V3.1

    def RetriveETH(self):                                                #ETH  
        client = Client(BinanCode.normal,BinanCode.sec)
        
        self.balanceETH = client.get_asset_balance(asset='ETH')
        self.balanceETH=pd.DataFrame.from_dict(self.balanceETH.items())
        self.balanceETH=self.balanceETH.loc[self.balanceETH[0]=='free']
        self.balanceETH=self.balanceETH.iloc[0,1]
        self.balanceETH = float(self.balanceETH)
        self.balanceETH = round(self.balanceETH,3)

        #return self.balanceETH                                                     #V3.1    
        