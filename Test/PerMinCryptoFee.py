# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:13:32 2021

@author: dvdvd
"""

#%%

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import math
import time
import re

#%%

import ConfigPerMinCrypto
import UlazPerMinCrypto
import RacunanjePerMinCrypto
import StampaPerMinCrypto
import SignalPerMinCrypto
import KomPerMinCrypto
import PetljaPerMinCrypto
                


#%%
#'''
                # For u foru da se isprobaju i razliciti periodi
           
DataForComp=pd.DataFrame()

DataForComp.insert(0,"Period",True)
DataForComp.insert(0,"SMA Window",True)
DataForComp.insert(0,"SMA Money",True)
DataForComp.insert(0,"SMA Percent",True)
DataForComp.insert(0,"BH Money",True)
DataForComp.insert(0,"BH Percent",True)
DataForComp.insert(0,"Diff Money",True)
DataForComp.insert(0,"Diff Percent",True)
DataForComp.insert(0,"# Of Trans",True)
DataForComp.insert(0,"TotalFees",True)

DataForComp=DataForComp[["Period","SMA Window","SMA Money","SMA Percent","BH Money","BH Percent","Diff Money","Diff Percent","# Of Trans","TotalFees"]]



#%%
# def __init__(self, Fee, Data, SMAWindow, Period, BrojVrednosti,NumberOfDaysForTest ):


konf=ConfigPerMinCrypto.Config()
konf.read()

konf.Data = pd.read_csv (konf.path)    
konf.Data.columns = ["Unix","Date","Symbol","Open","High","Low","Close","VolumeETH","VolumeUSDT","TradeCount"]
konf.Data = konf.Data.iloc[::-1]
del konf.Data['Unix']
del konf.Data['Symbol']
del konf.Data['Open']
del konf.Data['High']
del konf.Data['Low']
del konf.Data['VolumeETH']
del konf.Data['VolumeUSDT']
del konf.Data['TradeCount']

for b in range (konf.PeriodStart,konf.PeriodEnd,konf.PeriodKorak):
    
    for a in range (konf.SMAWindowStart,konf.SMAWindowEnd+1):                 #for a in range (2,U.NumberOfDaysForTest+1):  
        
        print("#######################################################################################")
        print("")
        print("")
        print("")
        print("Period now is: " + str(b))
        print("Window now is: " + str(a))
        print("")
        
        #time.sleep(1)
        
        
        
        DataForCalc=pd.DataFrame()    
        DataForCalc.insert(0,"Date",True)        
        DataForCalc.insert(0,"Price",True)
        DataForCalc.insert(0,"PriceSMA",True)
        DataForCalc.insert(0,"Sign",True)        
        DataForCalc=DataForCalc[["Date","Price","PriceSMA","Sign"]]
        
        
        UlazTest = UlazPerMinCrypto.Ulaz(konf,a,b)
        Racunanje1=RacunanjePerMinCrypto.Racunanje(konf)
        Stampa1=StampaPerMinCrypto.Stampa()
        Signal1=SignalPerMinCrypto.Signal()
        Komunikacija1=KomPerMinCrypto.Komunikacija(DataForCalc)
        Petlja1=PetljaPerMinCrypto.Petlja()
        
        
        GainSMAMoney,GainSMAPercent, GainBHMoney, GainBHPercent, GainDifferenceMoney, GainDifferencePercent , NumOFTrans, TotalFees = Petlja1.PetljaStart(UlazTest, DataForCalc, Racunanje1, Signal1,Stampa1,Komunikacija1,konf)
        
        DataForComp = DataForComp.append({'Period': b, 'SMA Window': a, 'SMA Money': GainSMAMoney,'SMA Percent': GainSMAPercent, 'BH Money': GainBHMoney, 'BH Percent': GainBHPercent,'Diff Money': GainDifferenceMoney, 'Diff Percent': GainDifferencePercent, '# Of Trans': NumOFTrans, 'TotalFees' : TotalFees}, ignore_index=True)
        
        #DataForComp.loc[b,a]=[b,a,GainSMAMoney,GainSMAPercent,GainBHMoney,GainBHPercent,GainDifferenceMoney,GainDifferencePercent, NumOFTrans]
    
    
DataSorted = DataForComp.sort_values(by='SMA Money')

Best = DataSorted.tail(1)

print("")
print("")
print("")
print("")
print("")
print("")
print("We got the best results when Period is: " + str(math.trunc(Best.iloc[0,0])) + " And SMAWindow is: " + str(math.trunc(Best.iloc[0,1])))
print("")

BestPeriod=Best.iloc[0,0]
BestWindow=Best.iloc[0,1]

BestPeriod=int(BestPeriod)
BestWindow=int(BestWindow)

Best.drop('Period', inplace=True, axis=1)
Best.drop('SMA Window', inplace=True, axis=1)

print(Best)
print("")
print("")
print("")
print("")
print("")
print("")


a_file = open("E:\David\Fax\Praksa\Code\PerMinCryptoFee\configFee.txt", "r")
list_of_lines = a_file.readlines()

list_of_lines[13] = list_of_lines[13][: -1: ] 
list_of_lines[13] = list_of_lines[13] + " " + str(BestWindow) +" \n"


list_of_lines[14] = list_of_lines[14] + " " + str(BestPeriod)



a_file = open("E:\David\Fax\Praksa\Code\PerMinCryptoFee\configFee.txt", "w")
a_file.writelines(list_of_lines)
a_file.close()

#'''


#%%

#'''

konf=ConfigPerMinCrypto.Config()

konf.read()

konf.Data = pd.read_csv (konf.path)    
konf.Data.columns = ["Unix","Date","Symbol","Open","High","Low","Close","VolumeETH","VolumeUSDT","TradeCount"]
konf.Data = konf.Data.iloc[::-1]
del konf.Data['Unix']
del konf.Data['Symbol']
del konf.Data['Open']
del konf.Data['High']
del konf.Data['Low']
del konf.Data['VolumeETH']
del konf.Data['VolumeUSDT']
del konf.Data['TradeCount']


DataForCalc=pd.DataFrame()
DataForCalc.insert(0,"Date",True)
DataForCalc.insert(0,"Market Price",True)
DataForCalc.insert(0,"xSq",True)
DataForCalc.insert(0,"Sign",True)
DataForCalc=DataForCalc[["Date","Market Price","xSq","Sign"]]


UlazTest = UlazPerMinCrypto.Ulaz(konf,BestWindow,BestPeriod)
Racunanje1=RacunanjePerMinCrypto.Racunanje(konf)
Stampa1=StampaPerMinCrypto.Stampa()
Signal1=SignalPerMinCrypto.Signal()
Komunikacija1=KomPerMinCrypto.Komunikacija(DataForCalc)
Petlja1=PetljaPerMinCrypto.Petlja()

Petlja1.PetljaStart(UlazTest, DataForCalc, Racunanje1, Signal1,Stampa1,Komunikacija1,konf)

DataForCalc.plot() 
plt.xlabel('Step ' + '(' + str(round(BestPeriod/60)) + 'h)' )
plt.ylabel('Market Price in $')
plt.title('')

#'''

#%%
'''
konf=ConfigPerMinCrypto.Config()
konf.read()
konf.Data = pd.read_csv (konf.path)    
konf.Data.columns = ["Unix","Date","Symbol","Open","High","Low","Close","VolumeETH","VolumeUSDT","TradeCount"]
konf.Data = konf.Data.iloc[::-1]
del konf.Data['Unix']
del konf.Data['Symbol']
del konf.Data['Open']
del konf.Data['High']
del konf.Data['Low']
del konf.Data['VolumeETH']
del konf.Data['VolumeUSDT']
del konf.Data['TradeCount']



DataForCalc=pd.DataFrame()

DataForCalc.insert(0,"Date",True)
DataForCalc.insert(0,"Price",True)
DataForCalc.insert(0,"PriceSMA",True)
DataForCalc.insert(0,"Sign",True)

DataForCalc=DataForCalc[["Date","Price","PriceSMA","Sign"]]


UlazTest = UlazPerMinCrypto.Ulaz(konf,43,1080)
Racunanje1=RacunanjePerMinCrypto.Racunanje(konf)
Stampa1=StampaPerMinCrypto.Stampa()
Signal1=SignalPerMinCrypto.Signal()
Komunikacija1=KomPerMinCrypto.Komunikacija(DataForCalc)
Petlja1=PetljaPerMinCrypto.Petlja()


Petlja1.PetljaStart(UlazTest, DataForCalc, Racunanje1, Signal1,Stampa1,Komunikacija1,konf)


DataForCalc.plot()
'''

#%%


