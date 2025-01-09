import pandas as pd
import numpy as np

def fractional_year_to_quarter_date(fractional_year):
    year = int(fractional_year)  # Extract the integer part as the year
    quarter = int((fractional_year - year) * 4) + 1  # Determine the quarter
    # Map quarter to end-of-quarter month
    quarter_end_month = {1: 3, 2: 6, 3: 9, 4: 12}
    month = quarter_end_month[quarter]
    return pd.Timestamp(year=year, month=month, day=1) + pd.offsets.MonthEnd(0)

def process_regression_data(monthly_data, quarterly_data):
    monthly_processed = {
        'BR': monthly_data.iloc[:, 1],
        'LogIndProd': 100 * np.log(monthly_data.iloc[:, 3]),
        'LogComPrice': 100 * np.log(monthly_data.iloc[:, 4]),
        'Inf': monthly_data.iloc[:, 7],
    }
    monthly_df = pd.DataFrame(monthly_processed)

    monthly_data_ts = monthly_data.set_index("Date")
    iop_difference = monthly_data_ts.iloc[:, 2].diff().resample("QE").mean()
    if (quarterly_data["Date"].dtypes == "float64"):
        quarterly_data["Date"] = quarterly_data["Date"].apply(fractional_year_to_quarter_date)
    quarterly_data_ts = quarterly_data.set_index("Date")

    quarterly_processed = {
        'LogGDP': 100 * np.log(quarterly_data_ts.iloc[:, 0]),
        'LogCONS': 100 * np.log(quarterly_data_ts.iloc[:, 1]),
        'LogINV': 100 * np.log(quarterly_data_ts.iloc[:, 2]),
        'LogHours': 100 * np.log(quarterly_data_ts.iloc[:, 3]),
        'Unemp': quarterly_data_ts.iloc[:, 4],
        'LogNEER': 100 * np.log(quarterly_data_ts.iloc[:, 5]),
        'LogMO': 100 * np.log(quarterly_data_ts.iloc[:, 6]),
        'RPIX12m': quarterly_data_ts.iloc[:, 7],
        'CommodityPrice': quarterly_data_ts.iloc[:, 8],
        'IoP_diff': iop_difference,
        'Money_Growth': quarterly_data_ts.iloc[:, 6].diff(),
        'ChangeFTSE': quarterly_data_ts.iloc[:, 5].pct_change(),
        
    }
    quarterly_df = pd.DataFrame(quarterly_processed)

    return monthly_df, quarterly_df
