import pandas as pd
import random

countries = {
    "USA": (37.0902, -95.7129),
    "UK": (55.3781, -3.4360),
    "India": (20.5937, 78.9629),
    "China": (35.8617, 104.1954),
    "Brazil": (-14.2350, -51.9253),
    "Russia": (61.5240, 105.3188),
    "South Africa": (-30.5595, 22.9375),
    "Australia": (-25.2744, 133.7751),
    "Canada": (56.1304, -106.3468),
    "Germany": (51.1657, 10.4515)
}

data = {
    'Country': list(countries.keys()),
    'Latitude': [lat for lat, _ in countries.values()],
    'Longitude': [lon for _, lon in countries.values()],
    'Average Income (USD)': [random.randint(2000, 60000) for _ in countries],
    'Median Income (USD)': [random.randint(1000, 55000) for _ in countries],
    'Poverty Rate (%)': [random.uniform(0, 50) for _ in countries],
    'Gini Coefficient': [random.uniform(20, 60) for _ in countries],
    'Population': [random.randint(1e6, 1e9) for _ in countries]
}

df = pd.DataFrame(data)
df.to_csv("synthetic_income_data.csv", index=False)
