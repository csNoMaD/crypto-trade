# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:56:43 2021

@author: dvdvd
"""

#DV

import re

class Config:                                                         # Ubacio period
    def __init__(self):
                 self.Fee=0                 
                 self.SMAWindow=0                 
                 self.Period=0                
                 self.BrojVrednosti=0                 
                 self.path=''
                 self.Cash=0
                 self.NumOfBuys=0
                 
                 
                 
    def read(self):
        with open(r"E:\David\Fax\Praksa\Code\__1A\V0_6_Override\ETH\configFee.txt", "r+") as file:         #DV
    
            List = file.readlines()
            ListOfNumbers = []
            
            path = List[10]
            path = path[30: -1: ]
            
            for i in range(len(List)):
                Numbers = re.findall(r'\d+(?:\.\d+)?', List[i]) 
                ListOfNumbers.extend(Numbers)
            
            #print(ListOfNumbers)   
          
            self.Fee = float(ListOfNumbers[0])
            self.SMAWindow = int(ListOfNumbers[10])
            self.Period = float(ListOfNumbers[11])
            self.BrojVrednosti = int(ListOfNumbers[6])
            self.Cash = float(ListOfNumbers[8])
            self.NumOfBuys = float(ListOfNumbers[9])