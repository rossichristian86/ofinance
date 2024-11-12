import yfinance as yf
import pandas as pd
from ..ofinance_defines import *
import math

## Tutti questi metodi prendono info e ci aggiungono label

# Calcola il Revenue Per Share per ogni anno e lo aggiungi al DataFrame principale
def add_profitable_years(obj_infos, obj_financials, label):

    net_income_senza_nan = [x for x in obj_financials[Financials.NetIncome.value] if not (isinstance(x, float) and math.isnan(x))]

    profitYears = len([x for x in net_income_senza_nan if x > 0])
    nYears = len(net_income_senza_nan)
    obj_infos[label.value] = f"{profitYears}/{nYears}"


def add_profitable_years_noTTM(obj_infos, obj_financials, label):

    net_income_senza_TTM = obj_financials[Financials.NetIncome.value][1:]
    net_income_senza_nan = [x for x in net_income_senza_TTM if not (isinstance(x, float) and math.isnan(x))]

    profitYears = len([x for x in net_income_senza_nan if x > 0])
    nYears = len(net_income_senza_nan)
    obj_infos[label.value] = f"{profitYears}/{nYears}"