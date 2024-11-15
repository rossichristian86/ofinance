from ofinance import *
from ofinance.snapshot import read_snapshot

'''
# Data download
stockData = OFinance("MCRI", snapshotPath=".out/")
print(stockData.info)
print(stockData.financials[Financials.RevenuePerShareGrowth1Y.value])
print(stockData.financials[Financials.RevenueGrowth1Y.value])
print(stockData.financials[Financials.BasicAverageShares.value])
print(stockData.financials[Financials.Revenues.value])
print(stockData.financials[Financials.OperatingIncome.value])
print(stockData.financials[Financials.NetIncome.value])
print(stockData.financials[Financials.NetMargin.value])
print(stockData.financials[Financials.OperatingMargin.value])
'''

# gira NNE

stockData = OFinance("NNE", snapshotPath=".out/")

print(stockData.info)
print(stockData.financials[Financials.Revenues.value])
#print(stockData.quarterly_financials[Quarterlyfinancials.TotalRevenue.value])
#print("\n\n")
#stockData.read_snapshot("haha")

#stockData2 = read_snapshot(".out/data.json")
#print(stockData2.quarterly_financials[Quarterlyfinancials.TotalRevenue.value])
