from .ofinance_defines import *
from  .core.ofcore import OfCore
import json
import pandas as pd



class OFinance(OfCore):
    def __init__(self, ticker=None, snapshotPath="") -> None:
        if ticker != None:
            super().__init__(ticker)
            if snapshotPath != "" : self.take_snapshot(snapshotPath) 


    def take_snapshot(self, snapshotsDir):
        # outFileName =  path + "/" + <market>_<symbol>_<date>_<sha>.json
        super().take_snapshot(snapshotsDir)
        

    def __repr__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\n\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    

    def __str__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    

