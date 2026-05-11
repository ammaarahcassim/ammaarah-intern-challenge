# Prompt log

## 1. Problem understanding & model choice

### ChatGPT

- Can you tell me what are the best models for predicting monthly revenue given previous months revenue data. Include their limitations and trade offs
- The data comprises of 12 months of transactions. Around 5000 records
- Is random forest more complex than LR?

## 2.Data formatting & cleaning challenges

### Gemini

- these are all the different formats of dates i have in my dataset

YYYY-MM-DD

DD/MM/YYYY

DD (month in actual words) YYYY

MM-DD-YYYY
how do i consolidate them into one format?

- how to change like one specific record

## 3. Data Cleaning implementation issues

### Claude

- how to convert MM-DD-YYYY to YYYY-MM-DD format in a dataset using python
- the formats are all different

when i use df['date'] = pd.to_datetime(df['date'], format = 'mixed').dt.strftime('%Y-%m-%d') i get this error:

ValueError: time data "12 Oct 2024" doesn't match format "%m-%d-%Y". You might want to try: - passing `format` if your strings have a consistent format; - passing `format='ISO8601'` if your strings are all ISO8601 but not necessarily in exactly the same format; - passing `format='mixed'`, and the format will be inferred for each element individually. You might want to use `dayfirst` alongside this.

- is there a rename function to change column names
- how would you search for duplicate records where 2 or more columns have the exact same values
- how do you change a string column to float
- how to sum values that have a certain characteristic

## 4. Feature engineering & aggregation

### Claude

- What feature engineering techniques are useful for predicting monthly store revenue?
- Should I group by month and calculate percentage change to show growth trends?
- How do I group by month and another variable in pandas?

- if you're trying to show a growth trend over a year do you group by each month and then calculate the percentage increase or decrease?

- what feature engineering would you use to accrately predict monthly store revenue
- how does the sin and cosine work for seasonality
- Which metrics do i use to evaluate a linear regression model
- What does negative R² mean in regression?
- whats an insight in retail transaction data that is different from seasonality, store performance, etc
- what does a mae of 15k mean if my monthly revenue on average is between 100k and 400k
- what if my r2 is 0.782 but my mae is 15000. How would i interpret it?
