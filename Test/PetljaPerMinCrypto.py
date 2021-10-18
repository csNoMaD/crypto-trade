# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:48:25 2021

@author: dvdvd
"""

class Petlja:
    
        
    def PetljaStart(self,ulaz,dataSMA,racunanje,signal,Stampa1,komunikacija,konfig):
        buyIndicator=0
        
        #racunanje.data=ulaz.Data.iloc[-ulaz.BrojVrednosti :]
        
        brVr = ulaz.BrojVrednosti + ulaz.NumberOfDaysForTest * ulaz.Period
        racunanje.data=ulaz.Data.iloc[-brVr :]
                
        racunanje.data=racunanje.data.iloc[::ulaz.Period, :]
        
        
        for a in range(0,len(racunanje.data.index) - ulaz.NumberOfDaysForTest):
            
            komunikacija.Step(ulaz,a,racunanje,dataSMA)                              
            
            if (len(dataSMA))>1:        
                if (dataSMA.iloc[a,3] != dataSMA.iloc[a-1,3]):                      # Has sign changed
                    if (dataSMA.iloc[a,3]=="+"):                                    # is it now +
                        buyIndicator=1
                        
                        signal.BuySignal(racunanje, dataSMA.iloc[a,1],ulaz,Stampa1,dataSMA.iloc[a,0])
                        
                    elif (buyIndicator==1):
                        signal.SellSignal(racunanje, dataSMA.iloc[a,1],ulaz,Stampa1,dataSMA.iloc[a,0])
                        
                        
                
                else:
                    if (racunanje.MoneyInvested!=0):
                        racunanje.CalculateSignNotChanged(dataSMA.iloc[a,1],dataSMA,ulaz)
                        
                if ( (buyIndicator != 0 ) and (racunanje.NumBought <= 0) ):                    
                    racunanje.NumOfTrans = -1
                    racunanje.TotalFees = -1
                    break
        
                        
        racunanje.CalculateBH(ulaz,racunanje)
        
        
        
        signal.EndSIgnal(racunanje, Stampa1)
        
        return racunanje.GainSMAMoney, racunanje.GainSMAPercent, racunanje.GainBHMoney, racunanje.GainBHPercent, racunanje.GainDifferenceMoney, racunanje.GainDifferencePercent, racunanje.NumOfTrans, racunanje.TotalFees