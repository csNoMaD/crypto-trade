# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:57:53 2021

@author: dvdvd
"""

#T
#V3.1


#V4

#override

#BUYSELL


import sys, time, msvcrt #override

import time
import pandas as pd



from datetime import datetime                                            #V4
from twisted.internet import task, reactor             #V4
import time                                               #V4
import random                                            #V4


class Petlja:
    
    def __init__(self):                                                                         
        self.iterator = 0
        self.buyIndicator = 0                                                  #BUYSELL
        self.sellIndicator = 1                                                       #BUYSELL
        self.timeout = 0
        self.skipIndicator = 0
    
    
    def readInput( self,caption, default, timeout = 0): #override

        timeout = self.timeout - 35                                                        #T
        start_time = time.time()
        sys.stdout.write('%s(%s):'%(caption, default))
        sys.stdout.flush()
        input = ''
        while True:
            if msvcrt.kbhit():
                byte_arr = msvcrt.getche()
                if ord(byte_arr) == 13: # enter_key
                    break
                elif ord(byte_arr) >= 32: #space_char
                    input += "".join(map(chr,byte_arr))
            if ((len(input) == 0) and ((time.time() - start_time) > timeout)):
                print(" timing out, no more time for override.")
                break
    
        print('')  # needed to move to next line
        if len(input) > 0:
            return input
        else:
            return default
        
        
    
    def Work(self, ulaz, racunanje, komunikacija, stampa, signal, binan, notif):
        
        
        
        komunikacija.Step(ulaz,racunanje,komunikacija.DataForCalc,stampa,self.iterator)                                  
            
        if (len(komunikacija.DataForCalc))>ulaz.SMAWindow:
            if (komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,3] != komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1-1,3]):
                if ((komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,3]=="+") and (komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1-1,3]=="-") and (self.buyIndicator == 1)):            #override
                    
                    if(self.skipIndicator == 1):
                    
                        self.skipIndicator=0
                        
                    else:
                
                        signal.BuySignal(racunanje, komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,1],ulaz,stampa,komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,0],binan,notif)
                        self.sellIndicator = 1                                                                                                                                                                              #override
                    
                elif ((komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,3]=="-") and (komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1-1,3]=="+") and (self.sellIndicator == 1)):         #override
                    
                    if(self.skipIndicator == 1):
                    
                        self.skipIndicator=0
                        
                    else:
                
                        signal.SellSignal(racunanje, komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,1],ulaz,stampa,komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,0],binan,notif)
                        self.buyIndicator = 1   
                                                                                                                                                                                                #override
                    
        
        
        #override---------------------------------
        
        
        
        ans = self.readInput('Type in buy, sell, skip or leave empty', '0') 
        
        if(ans =='buy'):
            
            signal.BuySignal(racunanje, komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,1],ulaz,stampa,komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,0],binan,notif)
            
            self.sellIndicator = 1
            self.buyIndicator = 0
                
        elif (ans == 'sell'):
            
            signal.SellSignal(racunanje, komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,1],ulaz,stampa,komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,0],binan,notif)
        
            self.sellIndicator = 0
            self.buyIndicator = 1
            
        elif (ans == 'skip'):
            
            if (komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,3]=="+"):
                
                self.sellIndicator = 1
                self.buyIndicator = 0
                self.skipIndicator = 1
                
            elif (komunikacija.DataForCalc.iloc[self.iterator + ulaz.SMAWindow -1,3]=="-"):
                
                self.sellIndicator = 0
                self.buyIndicator = 1
                self.skipIndicator = 1
            
            
        racunanje.NumWriten +=1
        
        self.iterator +=1
        
        #print(end - start)
        
        #time.sleep(random.randint(1,3))     

        print('-----------------------------------------------------------------------------------')                                               
    

    def PetljaStart(self,ulaz,dataSMA,racunanje,signal,komunikacija,binan, stampa , notif):
        self.iterator=0
        #self.buyIndicator=0        
        i=0              
        
        self.timeout = ulaz.PeriodSec                                                            #T
        
        #self.timeout = 20                                                                            #T
         
        
        komunikacija.Fetch(ulaz)                                                                                            #V4        
        komunikacija.DataForCalc = komunikacija.dfH                                                                         #V4        
        komunikacija.DataForCalc = komunikacija.DataForCalc.reset_index(drop = True)                                        #V4
        komunikacija.DataForCalc["Close"] = pd.to_numeric(komunikacija.DataForCalc["Close"])                                #V4
        


        
        args = (ulaz, racunanje, komunikacija, stampa, signal, binan, notif)
        
        
        l = task.LoopingCall(self.Work, *args)
        l.start(self.timeout) # call every sixty seconds

        reactor.run()
        
        
#%%     
###############################################################################################  OLD  ########################################################################################################                                                                                              

        #while i<ulaz.BrojVrednosti:            
        #while i<24:
        '''
        while True:
            
            komunikacija.Step(ulaz,racunanje,komunikacija.DataForCalc,stampa,iterator)                                  
            
            if (len(komunikacija.DataForCalc))>ulaz.SMAWindow:
                if (komunikacija.DataForCalc.iloc[iterator,3] != komunikacija.DataForCalc.iloc[iterator-1,3]):
                    if ((komunikacija.DataForCalc.iloc[iterator,3]=="+") and (komunikacija.DataForCalc.iloc[iterator-1,3]=="-")):
                        buyIndicator=1
                        
                        signal.BuySignal(racunanje, komunikacija.DataForCalc.iloc[iterator,1],ulaz,stampa,komunikacija.DataForCalc.iloc[iterator,0],binan,notif)
                        
                    elif (buyIndicator==1):
                        signal.SellSignal(racunanje, komunikacija.DataForCalc.iloc[iterator,1],ulaz,stampa,komunikacija.DataForCalc.iloc[iterator,0],binan,notif)
                        
                        
                
                #else:                                                                                              #V3.1
                #    if (racunanje.MoneyInvested!=0):                                                               #V3.1
                #        racunanje.CalculateSignNotChanged(komunikacija.DataForCalc.iloc[iterator,1],komunikacija.DataForCalc,ulaz, binan)            #V3.1
                        
            iterator +=1
            #i +=1                                           
            racunanje.NumWriten +=1
            
            #time.sleep(ulaz.PeriodSec-1)
            time.sleep(2)                          #T
            
        
                        
        #racunanje.CalculateBH(ulaz,racunanje,komunikacija.DataForCalc)                  #V3.1
        
        
        
        #signal.EndSIgnal(racunanje, stampa)                    #V3.1
        
        
        #V3.1
        #return racunanje.GainSMAMoney, racunanje.GainSMAPercent, racunanje.GainBHMoney, racunanje.GainBHPercent, racunanje.GainDifferenceMoney, racunanje.GainDifferencePercent, racunanje.NumOfTrans
        
        '''