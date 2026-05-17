import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv(
    "API_SM.POP.TOTL_DS2_en_csv_v2_114970.csv",
    skiprows=4
)

# Select country and 2024 data
data = df[['Country Name', '2024']].dropna()

# Remove 'World'
data = data[data['Country Name'] != 'World']

# Top 10 values
top10 = data.sort_values(by='2024', ascending=False).head(10)

# Bigger figure
plt.figure(figsize=(12,6))

# Bar chart
plt.bar(top10['Country Name'], top10['2024'])

# Title and labels
plt.title("Top 10 Population Values (2024)")
plt.xlabel("Country")
plt.ylabel("Population")

# Rotate names
plt.xticks(rotation=60)

# Adjust spacing
plt.tight_layout()

plt.show()