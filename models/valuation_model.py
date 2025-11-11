import numpy as np
import pandas as pd

def compute_true_value(row):
    gt = row.get("gt_interest_7d_norm", 0.0)
    wiki = row.get("wikipedia_30d_norm", 0.0)
    red = row.get("reddit_score_norm", 0.0)
    perf = row.get("perf_index", 0.0)
    value = (0.35*gt + 0.25*wiki + 0.25*red + 0.15*perf)
    return float(np.round(50000 + value*150000, 2))

def valuation_label(true_value, market_value):
    if pd.isna(market_value) or market_value == 0:
        return "Undiscovered"
    diff = (true_value - market_value) / market_value
    if diff > 0.20:   return "Undervalued"
    if diff < -0.20:  return "Overvalued"
    return "Fair"
