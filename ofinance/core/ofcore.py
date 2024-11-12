import yfinance as yf
import pandas as pd
from . import financialsY as fy
from . import infos as cfInfo
from . import financialsYoY as fyoy
from . import cfutils as cf
from ..ofinance_defines import *

POS_MARKET = 1
DEFAULT_MARKET = "USA"

class OfCore():

    def __init__(self, ticker) -> None:

        # Definisco il mercato di riferimento
        sym_market = str.split(ticker)
        self.market = sym_market[POS_MARKET] if len(sym_market) > 1 else DEFAULT_MARKET

        # Download data
        stock = yf.Ticker(ticker)

        # Get info and financials Y and Q
        info = stock.info
        financials = stock.financials.T
        quarterly_financials = stock.quarterly_financials.T
        
        # Calculate TTM Values for financials data, it will be inserted in financials
        ttm_data = {}

        # TTM values to be processed
        metrics_to_calculate_ttm = ["Total Revenue", "Gross Profit", "Operating Income", "Net Income"]
        for metric in metrics_to_calculate_ttm:
            # Check for quarter data
            if metric in quarterly_financials.columns:
                # Calculate TTM : sum of last 4 Quarter 
                ttm_value = quarterly_financials[metric].iloc[:4].sum()
                ttm_data[metric] = ttm_value

        # TTM values to be added from info data
        current_shares = stock.info.get(Info.SharesOutstanding.value)
        ttm_data[Financials.BasicAverageShares.value] = current_shares
        ttm_data[Financials.DilutedAverageShares.value] = current_shares

        # Add TTM data, new row in "financials", first position
        ttm_series = pd.Series(ttm_data, name='TTM')
        financials = pd.concat([ttm_series.to_frame().T, financials])

        ### Section YEAR
        fy.add_revenue_per_share(financials, Financials.RevenuePerShare.value)
        fy.add_diluted_revenue_per_share(financials, Financials.DilutedRevenuePerShare.value)
        fy.add_net_margin(financials, Financials.NetMargin.value)
        fy.add_operating_margin(financials, Financials.OperatingMargin.value)

        ### Section YoY
        fyoy.add_revenue_grow_1y(financials, Financials.RevenueGrowth1Y.value)
        fyoy.add_diluted_revenue_per_share_grow_1y(financials, Financials.RevenuePerShareGrowth1Y.value)
        fyoy.add_revenue_per_share_grow_1y(financials, Financials.DilutedRevenuePerShareGrowth1Y.value)

        ### Section custom infos
        cfInfo.add_profitable_years(info, financials, Info.ProfitableYears)
        cfInfo.add_profitable_years_noTTM(info, financials, Info.ProfitableYearsNoTTM)

        self.financials = financials
        self.info = info
        self.quarterly_financials = quarterly_financials

