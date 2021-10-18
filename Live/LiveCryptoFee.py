# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 18:32:48 2021

@author: dvdvd
"""

#V3.1 UNAPREDJENE PREFORMANSE

#V4

#%%

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import math
import sched, time
from datetime import datetime
import re


import requests


#%%

import ConfigLiveCrypto
import UlazLiveCrypto
import RacLiveCrypto
import SignalLiveCrypto
import KomLiveCrypto
import PetljaLiveCrypto
import BinanLiveCrypto
import StampaLiveCrypto
import Notification

#%%

pd.set_option('display.max_columns', None)
   
#%%
#############################################################################################################################################






config=ConfigLiveCrypto.Config()
config.read()

Ulaz1= UlazLiveCrypto.Ulaz(config)

Racunanje1=RacLiveCrypto.Racunanje(config)

Stampa1 = StampaLiveCrypto.Stampa()

Signal1=SignalLiveCrypto.Signal()

Komunikacija1=KomLiveCrypto.Komunikacija()

Komunikacija1.DataForCalc=pd.DataFrame(columns=["DateTime","Price","PriceSMA","Sign"])   #V4

Petlja1=PetljaLiveCrypto.Petlja()

Binan1 = BinanLiveCrypto.Binan()

Notif1 = Notification.Notif()         # added notif

Petlja1.PetljaStart(Ulaz1,Komunikacija1.DataForCalc,Racunanje1,Signal1,Komunikacija1,Binan1,Stampa1, Notif1)





########################################################
#%%





#DataForCalcPrint=Komunikacija1.DataForCalc.iloc[Ulaz1.SMAWindow:]
#DataForCalcPrint.plot()



#%%

#Komunikacija1.DataForCalc.info()
