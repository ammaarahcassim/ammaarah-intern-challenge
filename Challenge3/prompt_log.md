# Prompt log

## ChatGPT

1. Can you tell me what are the best models for predicting monthly revenue given previous months revenue data. Include their limitations and trade offs
2. The data comprises of 12 months of transactions. Around 5000 records
3. Is random forest more complex than LR?

## Gemini

1. these are all the different formats of dates i have in my dataset

YYYY-MM-DD

DD/MM/YYYY

DD (month in actual words) YYYY

MM-DD-YYYY
how do i consolidate them into one format?

2. how to change like one specific record

## Claude

1. how to convert MM-DD-YYYY to YYYY-MM-DD format in a dataset using python\
2. the formats are all different

when i use df['date'] = pd.to_datetime(df['date'], format = 'mixed').dt.strftime('%Y-%m-%d') i get this error:

ValueError: time data "12 Oct 2024" doesn't match format "%m-%d-%Y". You might want to try: - passing `format` if your strings have a consistent format; - passing `format='ISO8601'` if your strings are all ISO8601 but not necessarily in exactly the same format; - passing `format='mixed'`, and the format will be inferred for each element individually. You might want to use `dayfirst` alongside this.

2. is there a rename function to change column names
3. how would you search for duplicate records where 2 or more columns have the exact same values
4. how do you change a string column to float
5. how to sum values that have a certain characteristic
6. if you're trying to show a growth trend over a year do you group by each month and then calculate the percentage increase or decrease?
7. group by month and another characteristic
8. what feature engineering would you use to accrately predict monthly store revenue
9. how does the sin and cosine woek
10. Which metrics do i use to evaluate a linear regression model
11. What does negative R² mean in regression?
12. whats an insight in retail transaction data that is different from seasonality, store performance, etc
13. what does a mae of 15k mean if my monthly revenue on average is between 100k and 400k
14. what if my r2 is 0.782 but my mae is 15000
