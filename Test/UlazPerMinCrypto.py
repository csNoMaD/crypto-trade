# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:37:37 2021

@author: dvdvd
"""

class Ulaz:                                                         # Ubacio period
    def __init__(self,config, SMAWindow, Period):
                 self.Fee=config.Fee
                 self.Data=config.Data
                 self.SMAWindow=SMAWindow
                 self.Period=Period
                 self.BrojVrednosti=config.BrojVrednosti
                 self.NumberOfDaysForTest=config.NumberOfDaysForTest
                 self.NumOfBuys=config.NumOfBuys