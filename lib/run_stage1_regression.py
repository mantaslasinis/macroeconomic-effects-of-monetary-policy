import numpy as np
import pandas as pd
import statsmodels.api as sm

def run_stage1_regression(stage1_data):
  x = np.column_stack((
      np.ones(len(stage1_data['FDBRD14'])),
      stage1_data['RateD14'], stage1_data['NIRGDPM1'], stage1_data['NIRGDP0'], stage1_data['NIRGDP1'], stage1_data['NIRGDP2'], stage1_data['NIRINFLM1'], stage1_data['NIRINFL0'], stage1_data['NIRINFL1'], stage1_data['NIRINFL2'], stage1_data['NIRDGDPM1'], stage1_data['NIRDGDP0'], stage1_data['NIRDGDP1'], stage1_data['NIRDGDP2'], stage1_data['NIRDINFLM1'], stage1_data['NIRDINFL0'], stage1_data['NIRDINFL1'], stage1_data['NIRDINFL2'], stage1_data['UNEMPM1'], stage1_data['UNEMPM2'], stage1_data['UNEMPM3']
  ))
  y = stage1_data['FDBRD14']
  model = sm.OLS(y, x)
  results = model.fit()
  
  shocks = results.resid
  
  shock_df = pd.DataFrame({
     'Date': stage1_data['Date'],
     'Shocks': shocks,
  })

  return shock_df, results
