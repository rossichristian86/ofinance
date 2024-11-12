from ofinance import *

# Data download
stockData = OFinance("MCRI")

print(stockData.info)

print(stockData.financials[Financials.RevenuePerShareGrowth1Y.value])
print(stockData.financials[Financials.RevenueGrowth1Y.value])
print(stockData.financials[Financials.BasicAverageShares.value])
print(stockData.financials[Financials.Revenues.value])
print(stockData.financials[Financials.OperatingIncome.value])
print(stockData.financials[Financials.NetIncome.value])
print(stockData.financials[Financials.NetMargin.value])
print(stockData.financials[Financials.OperatingMargin.value])