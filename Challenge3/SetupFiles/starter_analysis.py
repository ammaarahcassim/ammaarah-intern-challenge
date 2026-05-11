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
df.rename(columns={"datum": "date", "kategorie": "category", "bedrag": "amount"}, inplace=True)

print("\nUpdated columns:")
print(df.columns.tolist())

#uniform date format
df['date'] = pd.to_datetime(df['date'], format='mixed')

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

#missing store name and uniformity for online transactions
df.loc[df['store'].isna(), 'store'] = "Online"

online = ['online', 'ONLINE', 'Online Store', 'Web']
df['store'] = df['store'].replace(online, 'Online')

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

#amount column
df["amount"] = df["amount"].str.replace(r"\((.*?)\)", r"-\1", regex=True)
df["amount"] = (
    df["amount"]
      .astype(str)
      .str.replace("R", "", regex=False)
      .str.replace(" ", "", regex=False)
      .str.replace(",", "", regex=False)
)

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

#duplicates
duplicates = df[df.duplicated(subset=['amount', 'customer_id', 'date'], keep=False)]
#
#print(duplicates)

#drop duplicates
df = df.drop_duplicates(subset=['amount', 'customer_id', 'date', 'category', 'quantity', 'payment_method'], keep='first')

#drop where amount is NaN
df = df.dropna(subset=['amount'])

print(df)

# === PART 2: EXPLORATORY ANALYSIS ===
# TODO: Answer the 5 business questions
# 1. Top 5 stores by revenue
# 2. Best product category + growth trend
# 3. Seasonal pattern (visualise it)
# 4. Province with highest avg transaction value
# 5. Online vs in-store trend

#1.TOP STORES
stores_revenue = df.groupby('store')['amount'].sum().sort_values(ascending=False).head(6)
print("Top 5 performing stores:", stores_revenue)

#2.BEST CATEGORY
best_category = df.groupby('category')['amount'].sum().sort_values(ascending=False).head(1).index[0]
print("Best product category:", best_category)

df['month'] = df['date'].dt.to_period('M')
monthly = df[df['category'] == best_category].groupby(['month', 'category'])['amount'].sum().reset_index()
monthly['percent_change'] = monthly['amount'].pct_change() * 100
slope = monthly['percent_change'].mean()
print(f"Trend: {'Growing' if slope > 0 else 'Shrinking'} (Slope: {slope:.2f})")

#4.PROVINCE WITH HIGHEST AVG TRANSACTION
p = df.groupby('province')['amount'].mean().sort_values(ascending=False).head(1).index[0]
print("Province with highest average transaction:", p)

#5.Online VS In-store trend
df['sales_type'] = df['store'].apply(lambda x: 'Online' if x == 'Online' else 'In-Store') 
comparison = df.groupby(['month', 'sales_type'])['amount'].sum().unstack() 
comparison['online percentage'] = (comparison['Online']/(comparison['Online'] + comparison['In-Store'])) * 100
print(comparison)


# === PART 3: PREDICTION ===
# TODO: Predict next month's revenue per store
# Keep it simple — a well-justified approach matters more than complexity

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

#monthly revenue per store
monthly_store = (
    df.groupby(['store', 'month'])['amount']
      .sum()
      .reset_index()
)

monthly_store = monthly_store.sort_values(['store', 'month'])

# Lag feature
monthly_store['prev_month_revenue'] = (
    monthly_store.groupby('store')['amount'].shift(1)
)

# Rolling 3-month average
monthly_store['rolling_3'] = (
    monthly_store.groupby('store')['amount']
                 .transform(lambda x: x.rolling(3).mean())
)

# Month seasonality
monthly_store['month_num'] = monthly_store['month'].dt.month
monthly_store['sin_month'] = np.sin(2 * np.pi * monthly_store['month_num'] / 12)
monthly_store['cos_month'] = np.cos(2 * np.pi * monthly_store['month_num'] / 12)

# Drop rows with missing lag/rolling values
monthly_store = monthly_store.dropna()

#split training and test data
split_idx = int(len(monthly_store) * 0.8)

train = monthly_store.iloc[:split_idx]
test = monthly_store.iloc[split_idx:]

feature_cols = [
    'prev_month_revenue',
    'rolling_3',
    'sin_month',
    'cos_month'
]

X_train = train[feature_cols]
y_train = train['amount']

X_test = test[feature_cols]
y_test = test['amount']

#train
model = LinearRegression()
model.fit(X_train, y_train)

#evaluate
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print(f"Mean Absolute Error: {mae:,.2f}")
print(f"R2 Score: {r2:.3f}")

#predict
latest = monthly_store.groupby('store').tail(1).copy()

latest_features = latest[feature_cols]

latest['predicted_next_month_revenue'] = model.predict(latest_features)

print("\nNext Month Forecast (per store)")
print(latest[['store', 'predicted_next_month_revenue']])

# === PART 4: BONUS INSIGHT ===
# TODO: Find something interesting that wasn't asked about
customer_counts = df['customer_id'].dropna().value_counts()
customer_counts = customer_counts.sort_values(ascending=False)
total_transactions = customer_counts.sum()
cumulative_share = customer_counts.cumsum() / total_transactions
top_10_cutoff = int(len(customer_counts) * 0.1)
top_10_share = customer_counts.iloc[:top_10_cutoff].sum() / total_transactions

print("\n Customer Concentration Analysis")
print(f"Total customers: {len(customer_counts)}")
print(f"Top 10% of customers account for: {top_10_share:.2%} of transactions")
print("\nMedian transactions per customer:", np.median(customer_counts))
print("Max transactions by a single customer:", customer_counts.max())

print("\n✓ Analysis complete. See output above.")
