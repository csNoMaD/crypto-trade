# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:57:42 2021

@author: dvdvd
"""

#V3

#V4

import pandas as pd
from datetime import datetime
import requests
from binance.client import Client

import BinanCode
import sys


#override


client = Client(BinanCode.normal,BinanCode.sec)

#DataForCalc=pd.DataFrame(columns=["DateTime","Price","PriceSMA","Sign"])

class Komunikacija:
    def __init__(self):
        self.dfH = pd.DataFrame()                                                                               #V4
        self.DataForCalc = pd.DataFrame()                                                                #V4
    
        
        
    def Step(self,ulaz,racunanje,DataSMA,stampa,iterator):            
        
        tickers = client.get_ticker(symbol = 'ETHUSDC')
    
    
        dataCSV=pd.DataFrame.from_dict(tickers.items())
        
            
        priceNow=dataCSV.loc[dataCSV[0]=='askPrice']
        priceNow=priceNow.iloc[0,1]
        priceNow=float(priceNow)
        
        self.DataForCalc.loc[iterator + ulaz.SMAWindow - 1]=[None,priceNow,None,None]                        #V4
        
        now = datetime.now()    
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
     
        
        
        sma=racunanje.calculateSMAValue(self.DataForCalc,ulaz)
        sign=racunanje.calculateSign(priceNow,sma, self.DataForCalc.iloc[iterator + ulaz.SMAWindow - 1 - 1 , 3])         #V4
        
        self.DataForCalc.loc[iterator + ulaz.SMAWindow - 1]=[dt_string,priceNow,sma,sign]  
        
        stampa.PrintPriceTime(priceNow,dt_string, sma, sign)                            #override
        
        '''
        if (racunanje.NumWriten >= ulaz.SMAWindow-1):
            
            sma=racunanje.calculateSMAValue(self.DataForCalc,ulaz)
            sign=racunanje.calculateSign(priceNow,sma, self.DataForCalc.iloc[iterator + ulaz.SMAWindow - 1 - 1 , 3])         #V4
            
            self.DataForCalc.loc[iterator + ulaz.SMAWindow - 1]=[dt_string,priceNow,sma,sign]                                     #V4
            
        
        else:
            self.DataForCalc.loc[iterator + ulaz.SMAWindow - 1]=[dt_string,priceNow,None,None]                                #V4
            
            '''
            
            
    def Fetch(self, ulaz):                                                                        #V4
        
        Period = ulaz.PeriodSec / 60
        Period = round(Period)
        Window = ulaz.SMAWindow
        
        PeriodH = Period / 60
        PeriodH = round(PeriodH)

        Inter = PeriodH * (Window - 1) + 1
        
        KlinesInter = str(round(Inter)) + ' hour ago UTC'
        
        
        klinesH = client.get_historical_klines("ETHUSDC", Client.KLINE_INTERVAL_1HOUR, KlinesInter)
        
        if((len(klinesH) != Inter)):
            print("GRESKA")
            sys.exit()

        
        self.dfH = pd.DataFrame(klinesH,columns=['OpenTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'Quote', 'NumOfTrades', 'TakerBuyBase', 'TakerBuyQuote', 'Ignore'])
        
        del self.dfH['OpenTime']
        del self.dfH['Open']
        del self.dfH['High']
        del self.dfH['Low']
        del self.dfH['Volume']
        del self.dfH['CloseTime']
        del self.dfH['Quote']
        del self.dfH['NumOfTrades']
        del self.dfH['TakerBuyBase']
        del self.dfH['TakerBuyQuote']
        del self.dfH['Ignore']
        
        self.dfH = self.dfH[:-PeriodH]
        
        self.dfH = self.dfH.loc[::-PeriodH,]
        self.dfH = self.dfH.iloc[::-1]
        
        self.dfH.insert(0,"Date",None)
        self.dfH.insert(0,"xSq",None)
        self.dfH.insert(0,"Sign",None)
        
        self.dfH = self.dfH[["Date","Close","xSq","Sign"]]
        
        #return dfH
        
        
            
            
            
            
