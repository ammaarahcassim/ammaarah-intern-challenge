# Reflections

## What I found most difficult

The most significant challenge wasn't the coding itself, but the conceptual weight of data cleaning. Initially, I viewed "messy data" as a technical hurdle to clear quickly, but I soon realized that cleaning is actually where the most important business decisions are made.

For example, I initially overlooked the missing store values, treating them as simple "errors" to be ignored. It took a deeper look at the dataset to realize these weren't mistakes; they were a signal for Online transactions. Correcting that oversight completely changed my revenue analysis. Additionally, standardizing the "Amount" column was particularly tricky—handling currency symbols, commas, and the accounting format for negative values (the parentheses) required precise string manipulation before I could even begin any math.

## What I would do with more time

If I had more time, I would focus on model competition. While Linear Regression is a great baseline for simplicity, I would have liked to implement a Random Forest or XGBoost model. These models are better at capturing "non-linear" relationships—like a sudden spike in sales that doesn't follow a straight line.

I would also refine my feature engineering. Currently, the model knows the month, but it doesn't know about specific external events. I would love to add a "Public Holiday" flag or "Payday" indicator to see if those specific days drive the spikes we see in provinces like Limpopo. Finally, I’d investigate the logistics-accounting mismatch I noted: finding out if physical stores are fulfilling online orders without getting the revenue credit, which would provide a much fairer "In-Store" performance metric.

## What did i learn that i didnt know before

I learned that data is a story told in a messy language. Before this project, I thought data science was mostly about complex algorithms. Now, I realize that 80% of the value comes from how you prepare the data and the assumptions you make during cleaning
I also gained a much better understanding of seasonal cycles. Using Sine and Cosine functions to teach a computer about the "circle" of a calendar year was a brand-new concept for me. Most importantly, I learned to look more deeply into what the data is telling you, realizing that a missing value (like a blank store name) can be just as informative as a filled-in one if you understand the business context.
