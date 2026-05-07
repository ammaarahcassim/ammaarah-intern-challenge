"""
Starter Analysis Script — Challenge 3: Make Sense of This Mess

This is an OPTIONAL skeleton to get you started.
You can use this, modify it, or ignore it entirely.
A Jupyter notebook is also perfectly fine.

Run: python starter_analysis.py
"""

import pandas as pd
import numpy as np
import os

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Note: matplotlib not installed. Run 'pip install -r requirements.txt' first for visualisations.")

# === LOAD DATA ===
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "data", "sales_data.csv")

print("Loading data...")
df = pd.read_csv(data_path)

print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nData types:")
print(df.dtypes)
print(f"\nMissing values:")
print(df.isnull().sum())
print(f"\nBasic stats:")
print(df.describe())


# === PART 1: DATA CLEANING ===
# TODO: Your cleaning code here
# Things to consider:
# - What do the column names mean?
# - Are the dates in a consistent format?
# - Can you convert 'bedrag' to a numeric column?
# - Are there duplicates?
# - What's going on with missing store values?


# === PART 2: EXPLORATORY ANALYSIS ===
# TODO: Answer the 5 business questions
# 1. Top 5 stores by revenue
# 2. Best product category + growth trend
# 3. Seasonal pattern (visualise it)
# 4. Province with highest avg transaction value
# 5. Online vs in-store trend


# === PART 3: PREDICTION ===
# TODO: Predict next month's revenue per store
# Keep it simple — a well-justified approach matters more than complexity


# === PART 4: BONUS INSIGHT ===
# TODO: Find something interesting that wasn't asked about


print("\n✓ Analysis complete. See output above.")
