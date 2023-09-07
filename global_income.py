import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("synthetic_income_data.csv")

st.title("Income Levels in Different Countries")

# Display the dataset
st.write(df)

# Bar chart for Average Income
st.subheader("Average Income by Country")
fig, ax = plt.subplots()
df.plot(x='Country', y='Average Income (USD)', kind='bar', legend=False, ax=ax)
ax.set_ylabel("Average Income (USD)")
st.pyplot(fig)
st.write("This bar chart displays the average income of individuals in various countries. It provides insights into the economic prosperity and living standards of each nation.")

# Bar chart for Median Income
st.subheader("Median Income by Country")
fig, ax = plt.subplots()
df.plot(x='Country', y='Median Income (USD)', kind='bar', color='green', legend=False, ax=ax)
ax.set_ylabel("Median Income (USD)")
st.pyplot(fig)
st.write("Median income gives a central value, eliminating extreme outliers. It's a good measure to understand the typical income of citizens.")

# Scatter Plot for Gini Coefficient vs Poverty Rate
st.subheader("Gini Coefficient vs. Poverty Rate")
fig, ax = plt.subplots()
df.plot(x='Gini Coefficient', y='Poverty Rate (%)', kind='scatter', legend=False, ax=ax)
ax.set_xlabel("Gini Coefficient")
ax.set_ylabel("Poverty Rate (%)")
st.pyplot(fig)
st.write("A higher Gini coefficient indicates greater income inequality. This scatter plot helps in understanding the relationship between income inequality and poverty rate in various countries.")

# Interactive map for Population
# Interactive map for Population
st.subheader("Population by Country")
map_data = df[["Latitude", "Longitude", "Population"]].copy()
map_data.columns = ["lat", "lon", "Population"]
st.map(map_data)
st.write("The interactive map showcases the population of various countries. The size of each circle corresponds to the population of the country.")

st.sidebar.title("Filters")
selected_country = st.sidebar.selectbox("Select a country for detailed insights:", df["Country"].unique())
country_data = df[df["Country"] == selected_country]
st.sidebar.write(country_data)
