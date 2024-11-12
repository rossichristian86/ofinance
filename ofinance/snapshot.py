from .ofinance import OFinance
import json
import pandas as pd
from .core import cfutils as cf
from .ofinance_defines import *


def read_snapshot(snapshot) -> OFinance: 
    with open(snapshot, 'r') as json_file:
        stock_data = json.load(json_file)

    # Convert Timestamp keys
    financials = cf.convert_keys_to_timestamp(stock_data['financials'])
    quarterly_financials = cf.convert_keys_to_timestamp(stock_data['quarterly_financials'])

    # Convert in dataframes
    financials_df = pd.DataFrame(financials)
    quarterly_financials_df = pd.DataFrame(quarterly_financials)

    out_obj = OFinance()
    out_obj.financials = financials_df
    out_obj.info = stock_data['info']
    out_obj.quarterly_financials = quarterly_financials_df

    return out_obj