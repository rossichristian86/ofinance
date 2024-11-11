# OpenFinance
A yfinance library with steroids.

### Main functionality


#### Build
```bash
python setup.py sdist bdist_wheel
```


#### Installazione
```bash
pip install dist/ofinance-<version>-py3-none-any.whl
```


#### Usage
Usage example:
```python
import ofinance as of

# Data download
stockData = of.OFinance("MCRI")
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
```

### Features


### Upcoming features

