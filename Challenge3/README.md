# Challenge 3: Make Sense of This Mess

## The Scenario

You've just joined **ShopRite Analytics** (fictional), the data team for a mid-size South African retail chain. They have 8 physical stores across the country plus an online channel.

The previous analyst exported 12 months of sales data into a CSV before leaving. Unfortunately, the data was pulled from three different systems that don't talk to each other, and nobody cleaned it up.

Your manager says: *"We need to understand how the business is doing. The board meeting is next week. Can you make sense of this data and tell us something useful?"*

Your job: **Clean the data, explore it, answer business questions, and build a simple forecast.**

---

## Setup

### Requirements

```bash
pip install -r requirements.txt
```

### Generate the dataset

```bash
python generate_dataset.py
```

This creates `data/sales_data.csv` — 12 months of messy retail transaction data (~5,000 records).

### Optional starter script

```bash
python starter_analysis.py
```

This gives you a skeleton to work from. You don't have to use it — work however you prefer (notebook, script, or both).

---

## Your Task

### Part 1: Data Cleaning (the hard part)

The data is messy. Before you can analyse anything, you need to fix it. Document every cleaning decision you make and why.

**Expect to find:**
- Inconsistent formatting
- Missing values (some are random, some are systematic — figure out which is which)
- Duplicates that aren't obvious
- Values that don't make sense

### Part 2: Exploratory Analysis

Answer these business questions:

1. **Which are our top 5 stores by total revenue?** (after cleaning)
2. **What's our best-performing product category, and is it growing or shrinking?**
3. **Is there a seasonal pattern in sales?** Show it visually.
4. **Which province generates the most revenue per transaction?**
5. **What's the trend in online vs in-store sales?**

For each answer: show your working (code + output) and write a 1-2 sentence business interpretation.

### Part 3: Prediction

Build a simple model to **predict next month's total revenue per store**.

You can use any approach — linear regression, time series, even a well-justified average. We care more about your reasoning than the model complexity.

Show:
- What features you used and why
- How you evaluated the model
- What the model's limitations are

### Part 4: One Insight the Business Doesn't Know

Find **one interesting pattern or anomaly** in the data that wasn't asked about in Part 2. Present it as if you're telling your manager in a 2-minute standup.

---

## What We're Evaluating

| Criteria | What we're looking for |
|----------|----------------------|
| Data cleaning | Did you find and fix the issues? Did you document your decisions? |
| Analysis correctness | Are your answers right? Do they make business sense? |
| Visualisations | Clear, labelled, useful — do they tell a story? |
| Prediction approach | Sensible method with honest evaluation of limitations |
| Prompt log | How did you use AI to explore and understand the data? |

> Remember: you'll walk us through your submission in an interview. Make sure you can explain every cleaning decision and analysis choice you made.  

---

## Hints

- Look at the data before you write any analysis code. `df.head()`, `df.info()`, `df.describe()` are your friends.
- Not all missing values mean the same thing. Some are errors; some are telling you something about the data.
- If a number looks wrong, check if it's actually wrong or if you're misunderstanding the format.
- Simple visualisations that tell a clear story beat complex ones that confuse.
- A linear regression that you understand beats an XGBoost that you can't explain.
- Show your thinking. "I chose to drop these rows because..." is more valuable than silently dropping them.

---

## Files

- `generate_dataset.py` — Dataset generator (you can read this to understand the data, but the challenge is to figure it out from the data itself)
- `starter_analysis.py` — Optional skeleton to get you started
- `requirements.txt` — Python dependencies
- `data/` — Generated after running `generate_dataset.py`

---

## Deliverables

1. **Your analysis** — Jupyter notebook OR Python script(s) that run end-to-end
2. **A short report** — `findings.md` — Your answers to Parts 2-4, written for a non-technical manager (1-2 pages max)
3. **prompt_log.md** — Your complete AI interaction history
4. **reflection.md** — Half-page: What was hardest? What would you do with more time?

---

## Time Expectation

This should take **4-6 hours**. If you're spending more than 8 hours, you're overcomplicating it. A clean, simple analysis that works is better than an elaborate one that doesn't.
