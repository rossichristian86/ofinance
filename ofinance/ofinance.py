import yfinance as yf
import pandas as pd
from .utils import financialsY as fy
from .utils import infos as cfInfo
from .utils import financialsYoY as fyoy
from .utils import cfutils as cf
#from .utils import defines
from .utils.defines import *

class OFinance:
    def __init__(self, ticker) -> None:

        # Scarica i dati della stock
        stock = yf.Ticker(ticker)

        # Ottieni i dati annuali e trimestrali
        financials = stock.financials.T

        quarterly_financials = stock.quarterly_financials.T

        #print(quarterly_financials)

        # Ottieni le informazioni della stock
        info = stock.info

        # Calcola TTM per ogni metrica principale e aggiungila come riga al DataFrame annuale
        ttm_data = {}

        # Elenco delle metriche principali che si vogliono calcolare in TTM
        metrics_to_calculate_ttm = ["Total Revenue", "Gross Profit", "Operating Income", "Net Income"]

        for metric in metrics_to_calculate_ttm:
            # Verifica che la metrica sia presente nei dati trimestrali
            if metric in quarterly_financials.columns:
                # Calcola il TTM come somma degli ultimi 4 trimestri
                ttm_value = quarterly_financials[metric].iloc[:4].sum()
                ttm_data[metric] = ttm_value

        # Aggiungi le azioni  dal info al TTM
        current_shares = stock.info.get(Info.SharesOutstanding.value)
        ttm_data[Financials.BasicAverageShares.value] = current_shares
        ttm_data[Financials.DilutedAverageShares.value] = current_shares

        # Aggiungi i dati TTM come una nuova riga nel DataFrame `financials` in prima posizione
        ttm_series = pd.Series(ttm_data, name='TTM')  # Crea una Series per TTM
        financials = pd.concat([ttm_series.to_frame().T, financials])  # Aggiungi in prima posizione

        ### SEZIONE CALCOLI YEAR
        fy.add_revenue_per_share(financials, Financials.RevenuePerShare.value)
        fy.add_diluted_revenue_per_share(financials, Financials.DilutedRevenuePerShare.value)
        fy.add_net_margin(financials, Financials.NetMargin.value)
        fy.add_operating_margin(financials, Financials.OperatingMargin.value)

        ### SEZIONE CALCOLI YoY
        fyoy.add_revenue_grow_1y(financials, Financials.RevenueGrowth1Y.value)
        fyoy.add_diluted_revenue_per_share_grow_1y(financials, Financials.RevenuePerShareGrowth1Y.value)
        fyoy.add_revenue_per_share_grow_1y(financials, Financials.DilutedRevenuePerShareGrowth1Y.value)

        ### SEZIONE custom infos
        cfInfo.add_profitable_years(info, financials, Info.ProfitableYears)
        cfInfo.add_profitable_years_noTTM(info, financials, Info.ProfitableYearsNoTTM)


        self.financials = financials
        self.info = info
        self.quarterly_financials = quarterly_financials


    def __repr__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\n\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    
    def __str__(self) -> str:
        out = (f"Info TTM: \n{self.info.keys()}]\nInfo annuali: \n{self.financials.columns}\n ")
        out = out + (f"\nEsempio di utilizzo: \n\tCFinanceObject.financials[\'Operating Income\'] \n\tCFinanceObject.info[\'sharesOutstanding\']")
        return out
    


if __name__ == "__main__":
    stockData = OFinance("AAPL")
    print(stockData.info[Info.ProfitableYears.value])
    print(stockData.info[Info.ProfitableYearsNoTTM.value])
