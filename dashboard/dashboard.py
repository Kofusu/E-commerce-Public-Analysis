import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

canceled_reviews_df = pd.read_csv("dashboard/canceled_reviews.csv")
customers_geo_df = pd.read_csv("dashboard/customers_geo.csv")
last_year_income_df = pd.read_csv("dashboard/last_year_income.csv")
order_time_df = pd.read_csv("dashboard/order_time_diff.csv")
products_df = pd.read_csv("dashboard/products_df.csv")

st.write('''
         # E-Commerce Public Dataset by Hendratara Pratama
         this dataset could be found at (E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce))
         ''')

# ----------------------------

st.metric(label="Total Income", value=f"{last_year_income_df['payment_value'].sum()} R$")
# ----------------------------

st.write('''
         ## Delivery Days
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