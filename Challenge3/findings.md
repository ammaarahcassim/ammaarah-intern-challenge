# Executive Summary: Sales Data Analysis

## Exploratory Analysis

### Top 5 Performing Stores

After cleaning the data and unifying store names (e.g., merging "Sandton City Mall" and "SANDTON CITY"), the top-performing stores by total revenue are:

1. Online (Top performer overall)
2. Menlyn Park
3. Canal Walk
4. Eastgate
5. Baywest Mall
6. Gateway Umhlanga (Top 5 if excluding Online)

### Best performing product category

The Electronics category generated the highest total revenue. While it experienced month-to-month fluctuations, it maintained a healthy growth trajectory with an average monthly increase of 14.30%.

### Province with highest revenue per transaction

On average, customers in Limpopo spend the most per individual transaction. This suggests that while other provinces might have higher total volume, Limpopo customers likely purchase higher-ticket items or larger baskets.

### Online VS In-store Trend

The data shows that the Online store is not just a secondary channel, but a consistent anchor for the business, maintaining a strong share of total revenue regardless of the season.

- Average Contribution: On average, the Online channel accounts for 22.7% of total monthly revenue.
- Stability during Scaling: Remarkably, as total revenue nearly doubled between October (R1.04M total) and December (R2.18M total), the Online channel maintained its share perfectly, moving from 22.05% to 25.54%. This proves the online infrastructure scales effectively with high demand.
- Monthly Variability:
  - Peak Online Dominance: In September, Online sales reached their highest proportion of the business at 29.05%.
  - Peak Physical Dominance: In July, In-Store sales were at their strongest relative to Online, which dipped to its lowest share of 16.85%.
    -The December Surge: While In-Store sales saw the largest absolute volume in December (R1.62M), the Online store also hit its record high (R557k), showing that the festive season drives a high tide for both channels.

## Predictive Model

For this analysis, I utilized Linear Regression. Given the dataset size, this model offers the best balance of simplicity and interpretability while effectively capturing the linear trends present in retail sales. Feature engineering was implemented to account for previous performance (lags), momentum (rolling averages), and seasonal cycles.

Linear Regression is a model that predicts continuous values by calculating a straight line that best fits the data, that is, it stays as close to all the data points as possible. It then uses that equation to make predictions.

### Feature Engineering

To improve the model's accuracy, I transformed the raw data into several "features":

1. Previous Month Revenue (Lag) : Captures the momentum of a store (strong performers usually stay strong).
2. Rolling 3-month average : Smooths out random monthly "noise" to identify the underlying performance trend.
3. Monthly Seasonality : Uses mathematical coordinates to help the model recognize that December and January are close in the calendar cycle, allowing it to "learn" holiday spikes.

### Training and Testing

I applied an 80/20 split, training the model on the first 80% of the chronological data. The remaining 20% was used as a "blind test" to see how well the model predicts data it hasn't seen before.

### Model Evaluation and Limitations

- Mean Absolute Error (MAE): 14,976.91
- R² Score: 0.782
- Interpretation: An R² of 0.782 means the model explains approximately 78% of the variance in monthly sales, which represents a very reliable fit for retail data. On average, predictions are off by roughly R14,976.
- An error of nearly R15 000 is relative to the size and total revenue of a particular store. The error will feel bigger on smaller stores and smaller on bigger stores. This is a standard limitation of Linear Regression, which tries to minimize the total error across the whole dataset rather than the percentage error for each individual row.

## Bonus Insight

I conducted a Customer Concentration Analysis and found that the top 10% of customers account for 33.68% of all transactions. This indicates a high level of brand loyalty, suggesting that a small group of "super-users" drives a massive portion of the business.
