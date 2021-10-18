# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:57:04 2021

@author: dvdvd
"""

class Ulaz:                                                         # Ubacio period
    def __init__(self,conf):
                 self.Fee=conf.Fee                
                 self.SMAWindow=conf.SMAWindow
                 self.PeriodSec=conf.Period*60
                 self.BrojVrednosti=conf.BrojVrednosti
                 self.NumOfBuys=conf.NumOfBuys