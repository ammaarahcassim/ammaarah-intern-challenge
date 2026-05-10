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

#change column names
df.rename(columns={
    "datum": "date",
    "kategorie": "category",
    "bedrag": "amount"
}, inplace=True)

print("\nUpdated columns:")
print(df.columns.tolist())

#uniform date format
df['date'] = pd.to_datetime(df['date'], format = 'mixed').dt.strftime('%Y-%m-%d')

#store names 
MOTN = ['MOTN', 'mall of the north', 'Mall of North']
sandton = ['sandton city', 'Sandton city', 'SANDTON CITY', 'Sandton City Mall']
eastgate = ['eastgate', 'Eastgate Mall', 'East Gate']
water = ['V&A waterfront', 'VA Waterfront', 'V and A Waterfront','V&A']
bay = ['Baywest', 'baywest mall', 'Bay West Mall']
gate = ['Gateway', 'gateway umhlanga', 'Gateway Mall Umhlanga']
menlyn = ['Menlyn', 'menlyn park', 'Menlyn Park Mall']
canal = ['Canal walk', 'canal walk', 'Canal Walk Mall']

df['store'] = df['store'].replace(MOTN, 'Mall of the North')
df['store'] = df['store'].replace(sandton, 'Sandton City')
df['store'] = df['store'].replace(eastgate, 'Eastgate')
df['store'] = df['store'].replace(water, 'V&A Waterfront')
df['store'] = df['store'].replace(bay, 'Baywest Mall')
df['store'] = df['store'].replace(gate, 'Gateway Umhlanga')
df['store'] = df['store'].replace(menlyn, 'Menlyn Park')
df['store'] = df['store'].replace(canal, 'Canal Walk')

#province names
ec = ['EC', 'E. Cape', 'eastern cape']
gauteng = ['GP', 'gauteng', 'Gauteng Province', 'GAUTENG']
kzn = ['KZN', 'Kwazulu-Natal', 'kwazulu natal', 'KwaZulu Natal']
limpopo = ['LP', 'limpopo', 'Limpopo Province']
wc = ['WC', 'W. Cape', 'western cape', 'Western cape']

df['province'] = df['province'].replace(ec, 'Eastern Cape')
df['province'] = df['province'].replace(gauteng, 'Gauteng')
df['province'] = df['province'].replace(kzn, 'KwaZulu-Natal')
df['province'] = df['province'].replace(limpopo, 'Limpopo')
df['province'] = df['province'].replace(wc, 'Western Cape')

#missing province
df.loc[(df['store'] == 'Mall of the North') & (df['province'].isna()), 'province'] = 'Limpopo'
df.loc[(df['store'] == 'Sandton City') & (df['province'].isna()), 'province'] = 'Gauteng'
df.loc[(df['store'] == 'Menlyn Park') & (df['province'].isna()), 'province'] = 'Gauteng'
df.loc[(df['store'] == 'Eastgate') & (df['province'].isna()), 'province'] = 'Gauteng'
df.loc[(df['store'] == 'V&A Waterfront') & (df['province'].isna()), 'province'] = 'Western Cape'
df.loc[(df['store'] == 'Canal Walk') & (df['province'].isna()), 'province'] = 'Western Cape'
df.loc[(df['store'] == 'Baywest Mall') & (df['province'].isna()), 'province'] = 'Eastern Cape'
df.loc[(df['store'] == 'Gateway Umhlanga') & (df['province'].isna()), 'province'] = 'KwaZulu-Natal'

#categories
clothes = ['Clothing', 'clothing', 'Clothes', 'CLOTHING', 'Apparel']
food = ['Food & Beverage', 'Food', 'food & beverage', 'F&B', 'Food and Beverage']
home = ['Home & Living', 'Home and Living', 'home & living', 'Home', 'H&L']
elect = ['Electronics', 'electronics', 'Elec.', 'ELECTRONICS', 'Tech']
sport = ['Sports', 'sports', 'SPORTS', 'Sports & Outdoors', 'Sport']
beauty = ['Beauty', 'beauty', 'BEAUTY', 'Beauty & Health', 'Cosmetics']

df['category'] = df['category'].replace(clothes, 'Clothing')
df['category'] = df['category'].replace(food, 'Food & Beverage')
df['category'] = df['category'].replace(home, 'Home & Living')
df['category'] = df['category'].replace(elect, 'Electronics')
df['category'] = df['category'].replace(sport, 'Sports')
df['category'] = df['category'].replace(beauty, 'Beauty')

print(df)


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
