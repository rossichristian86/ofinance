import yfinance as yf
import pandas as pd
import statistics
from ..ofinance_defines import *
import math

## questo metodo  prende info e ci aggiunge label
def add_custom_info(obj_infos, obj_financials):

    # ProfitableYears
    net_income_senza_nan = [x for x in obj_financials[Financials.NetIncome.value] if not (isinstance(x, float) and math.isnan(x))]
    profitYears = len([x for x in net_income_senza_nan if x > 0])
    nYears = len(net_income_senza_nan)
    obj_infos[Info.ProfitableYears.value] = f"{profitYears}/{nYears}"

    # ProfitableYearsNoTTM
    net_income_senza_TTM = obj_financials[Financials.NetIncome.value][1:]
    net_income_senza_nan = [x for x in net_income_senza_TTM if not (isinstance(x, float) and math.isnan(x))]
    profitYears = len([x for x in net_income_senza_nan if x > 0])
    nYears = len(net_income_senza_nan)
    obj_infos[Info.ProfitableYearsNoTTM.value] = f"{profitYears}/{nYears}"

    
    # NetMarginMean
    net_margin_senza_TTM = obj_financials[Financials.NetMargin.value][1:]
    obj_infos[Info.NetMarginMean.value] = float(round(net_margin_senza_TTM.mean(),3))

    # NetMarginMean1YNegativeExcluded
    net_margin_senza_TTM = list(obj_financials[Financials.NetMargin.value][1:])
    net_margin_senza_TTM = [x for x in net_margin_senza_TTM if x is not None]
    # Skip first negative number
    for i, num in enumerate(net_margin_senza_TTM):
        if num < 0:
            del net_margin_senza_TTM[i]
            break
    
    if len(net_margin_senza_TTM) > 0:
        obj_infos[Info.NetMarginMean1YNegativeExcluded.value] = round(statistics.mean(net_margin_senza_TTM),3)

    obj_infos[Info.EnterpriseValueCalculated.value] = round(float(obj_infos[Info.MarketCap.value]) + float(obj_infos[Info.TotalDebt.value]) - float(obj_infos[Info.TotalCash.value]),3)

    revenue = obj_financials[Financials.OperatingRevenue.value]["TTM"] if obj_financials[Financials.OperatingRevenue.value]["TTM"] > 0 else obj_financials[Financials.Revenues.value]["TTM"]

    # NetMarginMeanRevenuesToEv
    try:
        NetMarginMeanRevenuesToEv_local = (revenue*obj_infos[Info.NetMarginMean.value])/float(obj_infos[Info.EnterpriseValueCalculated.value])
        #print(f"NetMarginMeanRevenuesToEv_local {NetMarginMeanRevenuesToEv_local} revenue {revenue} obj_infos[Info.NetMarginMean.value] {obj_infos[Info.NetMarginMean.value]}")
        obj_infos[Info.NetMarginMeanRevenuesToEv.value] = f"{round(NetMarginMeanRevenuesToEv_local,3)}"
    except:
        print("ERROR: Info.NetMarginMeanRevenuesToEv something wrong")
        obj_infos[Info.NetMarginMeanRevenuesToEv.value] = f"{0}"

    # NetMarginMean1YNegativveExcludedRevenuesToEv
    try:
        NetMarginMean1YNegativveExcludedRevenuesToEv_local = (revenue*obj_infos[Info.NetMarginMean1YNegativeExcluded.value])/float(obj_infos[Info.EnterpriseValueCalculated.value])
        #print(f"NetMarginMean1YNegativveExcludedRevenuesToEv_local {NetMarginMean1YNegativveExcludedRevenuesToEv_local} obj_infos[Info.NetMarginMean.value] {obj_infos[Info.NetMarginMean.value]}")
        obj_infos[Info.NetMarginMean1YNegativveExcludedRevenuesToEv.value] = f"{round(NetMarginMean1YNegativveExcludedRevenuesToEv_local,3)}"
    except:
        print("ERROR: Info.NetMarginMean1YNegativveExcludedRevenuesToEv something wrong")
        obj_infos[Info.NetMarginMean1YNegativveExcludedRevenuesToEv.value] = f"{0}"

    # DebtToNetMarginRevenues
    try:
        DebtToNetMarginRevenues_local = float(obj_infos[Info.TotalDebt.value])/(revenue*obj_infos[Info.NetMarginMean.value])
        #print(f"NetMarginMeanRevenuesToEv_local {NetMarginMeanRevenuesToEv_local} revenue {revenue} obj_infos[Info.NetMarginMean.value] {obj_infos[Info.NetMarginMean.value]}")
        obj_infos[Info.DebtToNetMarginRevenues.value] = f"{round(DebtToNetMarginRevenues_local,2)}"
    except:
        print("ERROR: Info.DebtToNetMarginRevenues something wrong")
        obj_infos[Info.DebtToNetMarginRevenues.value] = f"{0}"
    