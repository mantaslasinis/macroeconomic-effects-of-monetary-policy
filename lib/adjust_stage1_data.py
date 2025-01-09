import numpy as np

def adjust_stage1_data(data):
  start = 3
  end = len(data)
  adjusted_stage1_data = {
        "Date": data.iloc[start:end, 0], "RateD14": data.iloc[start:end, 1], "FDBRD14": data.iloc[start:end, 2], "NIRGDPM1": data.iloc[start:end, 24], "NIRGDP0": data.iloc[start:end, 25], "NIRGDP1": data.iloc[start:end, 26], "NIRGDP2": data.iloc[start:end, 27], "NIRDGDPM1": data.iloc[start:end, 29], "NIRDGDP0": data.iloc[start:end, 30], "NIRDGDP1": data.iloc[start:end, 31], "NIRDGDP2": data.iloc[start:end, 32], "NIRINFLM1": data.iloc[start:end, 34], "NIRINFL0": data.iloc[start:end, 35], "NIRINFL1": data.iloc[start:end, 36], "NIRINFL2": data.iloc[start:end, 37], "NIRDINFLM1": data.iloc[start:end, 39], "NIRDINFL0": data.iloc[start:end, 40], "NIRDINFL1": data.iloc[start:end, 41], "NIRDINFL2": data.iloc[start:end, 42], "UNEMPM1": data.iloc[start:end, 43], "UNEMPM2": data.iloc[start:end, 44], "UNEMPM3": data.iloc[start:end, 45],
  }

  return adjusted_stage1_data