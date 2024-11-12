# OpenFinance
A yfinance library with steroids.

### Main class

##### OFinance
The core of the library, it provides same info as yfinance with more elaborated data.

##### Snapshot
Can upload a OFinance object from a OFinance snapshot file (method take_snapshot() in OFinance class).

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
from ofinance import *

# Data download
stockData = OFinance("MCRI")

# Print data
print(stockData.info[Info.EnterpriseValue.value])
print(stockData.info)
print(stockData.financials[Financials.RevenuePerShareGrowth1Y.value])
print(stockData.financials[Financials.RevenueGrowth1Y.value])
print(stockData.financials[Financials.BasicAverageShares.value])
print(stockData.financials[Financials.Revenues.value])
print(stockData.financials[Financials.OperatingIncome.value])
print(stockData.financials[Financials.NetIncome.value])
print(stockData.financials[Financials.NetMargin.value])
print(stockData.financials[Financials.OperatingMargin.value])

```

### Features


### Upcoming features

