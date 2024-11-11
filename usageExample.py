# Usage from local
from ofinance import OFinance as of

# Usage from pip package
#import ofinance as of

# Data download
stockData = of("MCRI")
print(stockData)

# Print data
print(stockData.info.keys())
print(stockData.info[of.Info.EnterpriseValue.value])
print(stockData.financials[of.Financials.RevenuePerShareGrowth1Y.value])
print(stockData.financials[of.Financials.RevenueGrowth1Y.value])
print(stockData.financials[of.Financials.BasicAverageShares.value])
print(stockData.financials[of.Financials.Revenues.value])
print(stockData.financials[of.Financials.OperatingIncome.value])
print(stockData.financials[of.Financials.NetIncome.value])
print(stockData.financials[of.Financials.NetMargin.value])
print(stockData.financials[of.Financials.OperatingMargin.value])