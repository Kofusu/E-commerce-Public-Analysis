import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

canceled_reviews_df = pd.read_csv("dashboard/canceled_reviews.csv")
customers_df = pd.read_csv("dashboard/customers.csv")
last_year_income_df = pd.read_csv("dashboard/last_year_income.csv")
order_time_df = pd.read_csv("dashboard/order_time_diff.csv")
products_df = pd.read_csv("dashboard/products_df.csv")

st.write('''
         # E-Commerce Public Dataset by Hendratara Pratama
         this dataset could be found at (E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce))
         ''')

# ----------------------------

st.metric(label="Total Income", value=f"{last_year_income_df['payment_value'].sum()} R$")

fig, ax = plt.subplots(figsize=(10, 6))
ax = last_year_income_df['payment_value'].plot(kind='line')
st.pyplot(fig)

st.dataframe(last_year_income_df['payment_value'].describe(), width=900)

# ----------------------------

st.write('''
         ## Delivery Days Totals
         ''')

days_arrive = order_time_df
fig, ax = plt.subplots(figsize=(20, 5))
sns.barplot(data=days_arrive.head(40), x='index', y='count', ax=ax)
plt.tight_layout()
plt.ylabel("Total Days")
plt.xlabel("Counts")
st.pyplot(fig)

# ----------------------------

st.write('''
         ## Canceled reviews history
         ''')

st.dataframe(data=canceled_reviews_df[['review_comment_title', 'review_comment_message']], width=900)

fig, ax = plt.subplots(figsize=(10, 6))
ax = canceled_reviews_df['review_score'].value_counts().sort_index().plot(kind='bar')
st.pyplot(fig)

# ----------------------------

fig, ax = plt.subplots(figsize=(10, 6))
ax = products_df['product_category_name_english'].value_counts().head(10).plot(kind='bar')
st.pyplot(fig)

# ----------------------------

col1, col2 = st.columns(2)

with col1:
  st.header("Top Customer City")
  fig, ax = plt.subplots(figsize=(14, 8))
  ax = customers_df['customer_city'].value_counts().sort_values(ascending=False).head().plot(kind='barh')
  st.pyplot(fig)

with col2:
  st.header("Top Customer State")
  fig, ax = plt.subplots(figsize=(14, 8))
  ax = customers_df['customer_state'].value_counts().sort_values(ascending=False).head().plot(kind='barh')
  st.pyplot(fig)

with st.sidebar:
  st.write('''
            input under construction :)
           ''')