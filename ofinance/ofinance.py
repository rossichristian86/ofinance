from .ofinance_defines import *
from  .core.ofcore import OfCore
import json
import pandas as pd


DEFAULT_ORIGIN = "DEF"

class OFinance(OfCore):
    def __init__(self, ticker=None, snapshotPath="") -> None:
        if ticker != None:
            super().__init__(ticker)
            if snapshotPath != "" : self.take_snapshot(snapshotPath, DEFAULT_ORIGIN) 


    def take_snapshot(self, snapshotsDir, origin=DEFAULT_ORIGIN):
        super().take_snapshot(snapshotsDir,origin)
        

    def __repr__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\n\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    

    def __str__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    

