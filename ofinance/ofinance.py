from .ofinance_defines import *
from  .core.ofcore import OfCore


class OFinance(OfCore):
    def __init__(self, ticker, snapshotPath="") -> None:
        super().__init__(ticker)
        if snapshotPath != "" : self.take_snapshot(snapshotPath) 


    def take_snapshot(path):
        # outFileName =  path + "/" + <market>_<symbol>_<date>_<sha>.json
        pass


    def __repr__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\n\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    

    def __str__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
